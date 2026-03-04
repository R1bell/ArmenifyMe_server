# Backend Additional Logic (Delta to Backend_TODO)

Дата: 2026-02-15
Статус: `docs/Backend_TODO.md` считаем базово реализованным. Ниже только дополнительная логика, нужная для текущего фронта (queue + dedup + retry + optimistic UI).

## 1. Цель delta
- Поддержать фронтовый контракт: `optimistic + queue + dedup + offline + auto-retry(backoff)`.
- Исключить двойной инкремент прогресса при повторах одного ответа.
- Дать фронту детерминированный серверный ответ для reconciliation.

## 2. Что обязательно добавить сверх Backend_TODO

### 2.1 `POST /api/v1/chat/answer` — idempotency
Обязательное поле запроса:
- `client_message_id` (string/uuid), уникальный ключ сообщения на фронте.

Request:
```json
{
  "client_message_id": "u-1739541289000",
  "word_id": "uuid",
  "answer": "привет"
}
```

Response (для одного и того же `client_message_id` всегда одинаковый бизнес-результат):
```json
{
  "client_message_id": "u-1739541289000",
  "server_event_id": "uuid",
  "deduplicated": false,
  "correct": true,
  "correct_count": 3,
  "threshold": 10,
  "status": "learning",
  "expected_translations": ["привет", "здравствуй"],
  "progress_version": 17,
  "processed_at": "2026-02-15T12:00:00Z"
}
```

Если запись уже обрабатывалась:
- `deduplicated: true`
- вернуть сохраненный `response_payload` без повторного изменения прогресса.

### 2.2 Таблица идемпотентности
Минимум:
- `user_id`
- `client_message_id`
- `response_payload` (jsonb)
- `created_at`
- unique index `(user_id, client_message_id)`

Опционально:
- `request_hash` для защиты от повторного использования того же ключа с другим payload.

### 2.3 Транзакционность обновления прогресса
При обработке `/chat/answer`:
1. Найти idempotency record по `(user_id, client_message_id)`.
2. Если найден — вернуть сохраненный payload.
3. Иначе открыть транзакцию.
4. Заблокировать `UserWordProgress` (`SELECT ... FOR UPDATE`).
5. Проверить ответ, обновить `correct_count/status`.
6. Сохранить прогресс + idempotency record в одной транзакции.
7. Вернуть payload.

### 2.4 Политика ошибок под фронт-очередь
- `400` — invalid payload
- `401/403` — auth
- `409` — semantic conflict (опционально)
- `5xx/timeout` — временная ошибка, фронт оставляет задачу и делает retry

Рекомендуемый формат:
```json
{
  "error_code": "CHAT_SYNC_FAILED",
  "message": "Temporary processing error"
}
```

## 3. Дополнительные версии для reconciliation (рекомендуется)

### 3.1 `progress_version`
- Поле версии в `UserWordProgress` (инкремент на каждое изменение).
- Возвращать в `POST /chat/answer`.

### 3.2 `list_version`/`updated_at`
- Для `GET /words/learning` и `GET /words/learned` вернуть верхнеуровневую версию списка.
- Упростит фронту сверку после поздних retry.

## 4. Settings: фиксируем контракт как в текущих моках фронта

Используем только `sync`-поведение:
- `PATCH /settings` сразу возвращает новые значения:
```json
{
  "correct_threshold": 12,
  "learning_list_size": 25
}
```
- пересчет статусов/списков выполняется в рамках этого же запроса (без `recalculation_job_id`).
- отдельный endpoint статуса пересчета не нужен.

Примечание:
- Если в будущем пересчет станет тяжелым, можно перейти на async-модель, но это будет отдельное изменение контракта API.

## 5. Offline/retry контракт (фиксируем)
- Фронт может повторять запрос с тем же `client_message_id` сколько угодно.
- Бек обязан гарантировать:
  - отсутствие двойного инкремента,
  - тот же бизнес-ответ для одного ключа,
  - корректную работу при конкурентных повторах.

Рекомендуемый backoff на фронте:
- `delay = min(1000 * 2^attempt, 30000)` (+ optional jitter).

## 6. Наблюдаемость
Логи:
- `user_id`, `client_message_id`, `deduplicated`, `status_code`, `latency_ms`.

Метрики:
- `chat_answer_total`
- `chat_answer_deduplicated_total`
- `chat_answer_error_total`
- `chat_answer_latency_ms`

## 7. Acceptance criteria (delta)
- Повтор с тем же `client_message_id` не меняет `correct_count` повторно.
- При сетевых сбоях retry не ломает консистентность.
- Поздний успешный retry корректно reconcile’ит фронтовый optimistic state.
- Контракт `PATCH /settings` фиксирован как `sync` и соответствует текущему поведению моков фронта.
