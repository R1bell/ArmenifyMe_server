from django.core.management.base import BaseCommand

from ArmenifyMe.armenify_server.models import Word


class Command(BaseCommand):
    help = "Seed Armenian A1 words into the Word table."

    def handle(self, *args, **options):
        if Word.objects.exists():
            self.stdout.write(self.style.WARNING("Words already exist; skipping seed"))
            return

        words = [
        {
                "armenian": "մասին",
                "translations": [
                        "об",
                        "про",
                        "на"
                ],
                "transcription": "masin"
        },
        {
                "armenian": "վերեւում",
                "translations": [
                        "над",
                        "наверху",
                        "сверху"
                ],
                "transcription": "verevum"
        },
        {
                "armenian": "միջով",
                "translations": [
                        "через",
                        "сквозь"
                ],
                "transcription": "mijov"
        },
        {
                "armenian": "գործողություն",
                "translations": [
                        "действие",
                        "поступок"
                ],
                "transcription": "gortsoghut’yun"
        },
        {
                "armenian": "գործունեություն",
                "translations": [
                        "деятельность",
                        "действие"
                ],
                "transcription": "gortsuneut’yun"
        },
        {
                "armenian": "դերասան",
                "translations": [
                        "актер",
                        "артист"
                ],
                "transcription": "derasan"
        },
        {
                "armenian": "դերասանուհի",
                "translations": [
                        "актриса"
                ],
                "transcription": "derasanuhi"
        },
        {
                "armenian": "ավելացնել",
                "translations": [
                        "добавить",
                        "добавлять"
                ],
                "transcription": "avelats’nel"
        },
        {
                "armenian": "հասցե",
                "translations": [
                        "адрес",
                        "обращаться"
                ],
                "transcription": "hasts’e"
        },
        {
                "armenian": "հասուն",
                "translations": [
                        "взрослый",
                        "зрелый"
                ],
                "transcription": "hasun"
        },
        {
                "armenian": "խորհուրդ",
                "translations": [
                        "совет",
                        "наставление"
                ],
                "transcription": "khorhurd"
        },
        {
                "armenian": "վախեցած",
                "translations": [
                        "бояться",
                        "боящийся",
                        "испуганный",
                        "напуганный"
                ],
                "transcription": "vakhets’ats"
        },
        {
                "armenian": "կենդանի",
                "translations": [
                        "животное",
                        "зверь",
                        "живой"
                ],
                "transcription": "kendani"
        },
        {
                "armenian": "ուրիշ",
                "translations": [
                        "другой",
                        "иной",
                        "не такой как"
                ],
                "transcription": "urish"
        },
        {
                "armenian": "պատասխան",
                "translations": [
                        "ответ"
                ],
                "transcription": "pataskhan"
        },
        {
                "armenian": "որեւէ",
                "translations": [
                        "любой",
                        "кто-нибудь",
                        "что-нибудь"
                ],
                "transcription": "voreve"
        },
        {
                "armenian": "ամեն մեկը",
                "translations": [
                        "всякий",
                        "кто угодно",
                        "кто-либо"
                ],
                "transcription": "amen meky"
        },
        {
                "armenian": "բնակարան",
                "translations": [
                        "квартира",
                        "апартамент"
                ],
                "transcription": "bnakaran"
        },
        {
                "armenian": "խնձոր",
                "translations": [
                        "яблоко"
                ],
                "transcription": "khndzor"
        },
        {
                "armenian": "ապրիլ",
                "translations": [
                        "апрель"
                ],
                "transcription": "april"
        },
        {
                "armenian": "շրջան",
                "translations": [
                        "круг",
                        "область",
                        "район"
                ],
                "transcription": "shrjan"
        },
        {
                "armenian": "շուրջը",
                "translations": [
                        "вокруг"
                ],
                "transcription": "shurjy"
        },
        {
                "armenian": "արվեստ",
                "translations": [
                        "искусство",
                        "умение",
                        "мастерство"
                ],
                "transcription": "arvest"
        },
        {
                "armenian": "հոդված",
                "translations": [
                        "статья"
                ],
                "transcription": "hodvats"
        },
        {
                "armenian": "նկարիչ",
                "translations": [
                        "художник",
                        "живописец",
                        "художница"
                ],
                "transcription": "nkarich’"
        },
        {
                "armenian": "հարցնել",
                "translations": [
                        "спрашивать",
                        "спросить",
                        "задать"
                ],
                "transcription": "harts’nel"
        },
        {
                "armenian": "օգոստոս",
                "translations": [
                        "август"
                ],
                "transcription": "ogostos"
        },
        {
                "armenian": "մորաքույր",
                "translations": [
                        "тетя",
                        "тетка"
                ],
                "transcription": "morak’uyr"
        },
        {
                "armenian": "աշուն",
                "translations": [
                        "осень"
                ],
                "transcription": "ashun"
        },
        {
                "armenian": "մանուկ",
                "translations": [
                        "младенец",
                        "ребенок",
                        "дитя"
                ],
                "transcription": "manuk"
        },
        {
                "armenian": "ետեւ",
                "translations": [
                        "зад",
                        "задняя часть"
                ],
                "transcription": "yetev"
        },
        {
                "armenian": "վատ",
                "translations": [
                        "плохой",
                        "дурной",
                        "злой"
                ],
                "transcription": "vat"
        },
        {
                "armenian": "պայուսակ",
                "translations": [
                        "сумка",
                        "пакет",
                        "мешок"
                ],
                "transcription": "payusak"
        },
        {
                "armenian": "գունդ",
                "translations": [
                        "шар",
                        "сфера",
                        "ком"
                ],
                "transcription": "gund"
        },
        {
                "armenian": "ադամաթուզ",
                "translations": [
                        "банан"
                ],
                "transcription": "adamat’uz"
        },
        {
                "armenian": "գոտի",
                "translations": [
                        "ремень"
                ],
                "transcription": "goti"
        },
        {
                "armenian": "բանկ",
                "translations": [
                        "банк"
                ],
                "transcription": "bank"
        },
        {
                "armenian": "լոգարան",
                "translations": [
                        "ванная комната",
                        "ванная"
                ],
                "transcription": "logaran"
        },
        {
                "armenian": "լինել",
                "translations": [
                        "быть",
                        "существовать",
                        "находиться"
                ],
                "transcription": "linel"
        },
        {
                "armenian": "լողափ",
                "translations": [
                        "пляж"
                ],
                "transcription": "loghap’"
        },
        {
                "armenian": "գեղեցիկ",
                "translations": [
                        "красивый",
                        "прекрасный",
                        "изящный"
                ],
                "transcription": "geghets’ik"
        },
        {
                "armenian": "որովհետեւ",
                "translations": [
                        "потому что",
                        "ибо",
                        "ведь"
                ],
                "transcription": "vorovhetev"
        },
        {
                "armenian": "դառնալ",
                "translations": [
                        "стать",
                        "становиться",
                        "превратиться"
                ],
                "transcription": "darrnal"
        },
        {
                "armenian": "անկողին",
                "translations": [
                        "постель",
                        "кровать"
                ],
                "transcription": "ankoghin"
        },
        {
                "armenian": "ննջարան",
                "translations": [
                        "спальня"
                ],
                "transcription": "nnjaran"
        },
        {
                "armenian": "գարեջուր",
                "translations": [
                        "пиво"
                ],
                "transcription": "garejur"
        },
        {
                "armenian": "առաջ",
                "translations": [
                        "перед",
                        "до",
                        "прежде"
                ],
                "transcription": "arraj"
        },
        {
                "armenian": "սկսել",
                "translations": [
                        "начинать",
                        "начинаться",
                        "начать"
                ],
                "transcription": "sksel"
        },
        {
                "armenian": "սկիզբ",
                "translations": [
                        "начало",
                        "старт"
                ],
                "transcription": "skizb"
        },
        {
                "armenian": "ետեւից",
                "translations": [
                        "за",
                        "позади"
                ],
                "transcription": "yetevits’"
        },
        {
                "armenian": "հավատալ",
                "translations": [
                        "верить",
                        "поверить"
                ],
                "transcription": "havatal"
        },
        {
                "armenian": "ցած",
                "translations": [
                        "ниже",
                        "вниз",
                        "внизу"
                ],
                "transcription": "ts’ats"
        },
        {
                "armenian": "ամենալավ",
                "translations": [
                        "наилучший",
                        "лучший",
                        "лучше"
                ],
                "transcription": "amenalav"
        },
        {
                "armenian": "ավելի լավ",
                "translations": [
                        "лучше"
                ],
                "transcription": "aveli lav"
        },
        {
                "armenian": "միջեւ",
                "translations": [
                        "между",
                        "среди",
                        "посреди"
                ],
                "transcription": "mijev"
        },
        {
                "armenian": "հեծանիվ",
                "translations": [
                        "велосипед",
                        "велик"
                ],
                "transcription": "hetsaniv"
        },
        {
                "armenian": "մեծ",
                "translations": [
                        "большой",
                        "великий",
                        "старший"
                ],
                "transcription": "mets"
        },
        {
                "armenian": "հաշիվ",
                "translations": [
                        "счет",
                        "исчисление"
                ],
                "transcription": "hashiv"
        },
        {
                "armenian": "թռչուն",
                "translations": [
                        "птица",
                        "пташка",
                        "птах"
                ],
                "transcription": "t’rrch’un"
        },
        {
                "armenian": "ծննդյան օր",
                "translations": [
                        "день рождения",
                        "дата рождения",
                        "днюха"
                ],
                "transcription": "tsnndyan or"
        },
        {
                "armenian": "սեւ",
                "translations": [
                        "черный",
                        "вороной"
                ],
                "transcription": "sev"
        },
        {
                "armenian": "բլոգ",
                "translations": [
                        "блог"
                ],
                "transcription": "blog"
        },
        {
                "armenian": "շիկահեր",
                "translations": [
                        "блондин",
                        "блондинка"
                ],
                "transcription": "shikaher"
        },
        {
                "armenian": "կապույտ",
                "translations": [
                        "голубой",
                        "синий",
                        "лазурный"
                ],
                "transcription": "kapuyt"
        },
        {
                "armenian": "նավակ",
                "translations": [
                        "лодка",
                        "шлюпка",
                        "ладья"
                ],
                "transcription": "navak"
        },
        {
                "armenian": "մարմին",
                "translations": [
                        "тело"
                ],
                "transcription": "marmin"
        },
        {
                "armenian": "գիրք",
                "translations": [
                        "книга",
                        "книжка"
                ],
                "transcription": "girk’"
        },
        {
                "armenian": "կոշիկ",
                "translations": [
                        "обувь"
                ],
                "transcription": "koshik"
        },
        {
                "armenian": "ձանձրալի",
                "translations": [
                        "скучный",
                        "нудный",
                        "утомительный"
                ],
                "transcription": "dzandzrali"
        },
        {
                "armenian": "ծնված",
                "translations": [
                        "родиться"
                ],
                "transcription": "tsnvats"
        },
        {
                "armenian": "երկուսն էլ",
                "translations": [
                        "оба"
                ],
                "transcription": "yerkusn el"
        },
        {
                "armenian": "շիշ",
                "translations": [
                        "бутылка",
                        "сосуд"
                ],
                "transcription": "shish"
        },
        {
                "armenian": "արկղ",
                "translations": [
                        "ящик",
                        "коробка"
                ],
                "transcription": "arkgh"
        },
        {
                "armenian": "տղա",
                "translations": [
                        "мальчик",
                        "сын",
                        "юноша"
                ],
                "transcription": "tgha"
        },
        {
                "armenian": "հաց",
                "translations": [
                        "хлеб"
                ],
                "transcription": "hats’"
        },
        {
                "armenian": "կոտրել",
                "translations": [
                        "разбить",
                        "сломать",
                        "разбивать"
                ],
                "transcription": "kotrel"
        },
        {
                "armenian": "նախաճաշ",
                "translations": [
                        "завтрак"
                ],
                "transcription": "nakhachash"
        },
        {
                "armenian": "բերել",
                "translations": [
                        "принести",
                        "привести",
                        "приносить"
                ],
                "transcription": "berel"
        },
        {
                "armenian": "եղբայր",
                "translations": [
                        "брат"
                ],
                "transcription": "yeghbayr"
        },
        {
                "armenian": "շագանակագույն",
                "translations": [
                        "коричневый",
                        "каштановый",
                        "карий"
                ],
                "transcription": "shaganakaguyn"
        },
        {
                "armenian": "կառուցել",
                "translations": [
                        "строить",
                        "построить",
                        "конструировать"
                ],
                "transcription": "karruts’el"
        },
        {
                "armenian": "շենք",
                "translations": [
                        "здание",
                        "постройка",
                        "дом"
                ],
                "transcription": "shenk’"
        },
        {
                "armenian": "ավտոբուս",
                "translations": [
                        "автобус"
                ],
                "transcription": "avtobus"
        },
        {
                "armenian": "գործ",
                "translations": [
                        "работа",
                        "труд",
                        "занятие"
                ],
                "transcription": "gorts"
        },
        {
                "armenian": "զբաղված",
                "translations": [
                        "занят",
                        "занято"
                ],
                "transcription": "zbaghvats"
        },
        {
                "armenian": "բայց",
                "translations": [
                        "но",
                        "а",
                        "только"
                ],
                "transcription": "bayts’"
        },
        {
                "armenian": "յուղ",
                "translations": [
                        "масло",
                        "сливочное масло"
                ],
                "transcription": "yugh"
        },
        {
                "armenian": "գնել",
                "translations": [
                        "покупать",
                        "купить"
                ],
                "transcription": "gnel"
        },
        {
                "armenian": "հաջող",
                "translations": [
                        "пока",
                        "удачи"
                ],
                "transcription": "hajogh"
        },
        {
                "armenian": "կաֆե",
                "translations": [
                        "кафе",
                        "кафетерий",
                        "кофейня"
                ],
                "transcription": "kafe"
        },
        {
                "armenian": "տորթ",
                "translations": [
                        "торт",
                        "пирожное"
                ],
                "transcription": "tort’"
        },
        {
                "armenian": "զանգահարել",
                "translations": [
                        "звонить"
                ],
                "transcription": "zangaharel"
        },
        {
                "armenian": "տեսախցիկ",
                "translations": [
                        "камера",
                        "видеокамера"
                ],
                "transcription": "tesakhts’ik"
        },
        {
                "armenian": "կարողանալ",
                "translations": [
                        "мочь",
                        "уметь",
                        "смочь"
                ],
                "transcription": "karoghanal"
        },
        {
                "armenian": "կապիտալ",
                "translations": [
                        "капитал",
                        "столица",
                        "богатство"
                ],
                "transcription": "kapital"
        },
        {
                "armenian": "քարտ",
                "translations": [
                        "карточка",
                        "карта",
                        "плата"
                ],
                "transcription": "k’art"
        },
        {
                "armenian": "կարիերա",
                "translations": [
                        "карьера"
                ],
                "transcription": "kariyera"
        },
        {
                "armenian": "գազար",
                "translations": [
                        "морковь",
                        "морковка",
                        "морква"
                ],
                "transcription": "gazar"
        },
        {
                "armenian": "տանել",
                "translations": [
                        "нести",
                        "носить",
                        "везти"
                ],
                "transcription": "tanel"
        },
        {
                "armenian": "կատու",
                "translations": [
                        "кошка",
                        "кот"
                ],
                "transcription": "katu"
        },
        {
                "armenian": "կենտրոն",
                "translations": [
                        "центр",
                        "середина",
                        "средина"
                ],
                "transcription": "kentron"
        },
        {
                "armenian": "դար",
                "translations": [
                        "век",
                        "столетие",
                        "эра"
                ],
                "transcription": "dar"
        },
        {
                "armenian": "աթոռ",
                "translations": [
                        "стул"
                ],
                "transcription": "at’vorr"
        },
        {
                "armenian": "փոխել",
                "translations": [
                        "менять",
                        "изменять",
                        "превращать"
                ],
                "transcription": "p’vokhel"
        },
        {
                "armenian": "գծապատկեր",
                "translations": [
                        "диаграмма",
                        "схема"
                ],
                "transcription": "gtsapatker"
        },
        {
                "armenian": "էժան",
                "translations": [
                        "дешевый",
                        "недорогой"
                ],
                "transcription": "ezhan"
        },
        {
                "armenian": "ստուգել",
                "translations": [
                        "проверить",
                        "проверять"
                ],
                "transcription": "stugel"
        },
        {
                "armenian": "պանիր",
                "translations": [
                        "сыр"
                ],
                "transcription": "panir"
        },
        {
                "armenian": "հավ",
                "translations": [
                        "курица"
                ],
                "transcription": "hav"
        },
        {
                "armenian": "երեխա",
                "translations": [
                        "ребенок",
                        "дитя",
                        "малыш"
                ],
                "transcription": "yerekha"
        },
        {
                "armenian": "շոկոլադ",
                "translations": [
                        "шоколад"
                ],
                "transcription": "shokolad"
        },
        {
                "armenian": "ընտրել",
                "translations": [
                        "выбрать",
                        "выбирать",
                        "избрать"
                ],
                "transcription": "yntrel"
        },
        {
                "armenian": "կինո",
                "translations": [
                        "фильм",
                        "кино"
                ],
                "transcription": "kino"
        },
        {
                "armenian": "քաղաք",
                "translations": [
                        "город",
                        "поселок",
                        "городок"
                ],
                "transcription": "k’aghak’"
        },
        {
                "armenian": "դաս",
                "translations": [
                        "класс",
                        "урок",
                        "курс"
                ],
                "transcription": "das"
        },
        {
                "armenian": "դասարան",
                "translations": [
                        "класс",
                        "группа",
                        "классная комната"
                ],
                "transcription": "dasaran"
        },
        {
                "armenian": "մաքրել",
                "translations": [
                        "чистить",
                        "вытирать",
                        "стереть"
                ],
                "transcription": "mak’rel"
        },
        {
                "armenian": "բարձրանալ",
                "translations": [
                        "подняться",
                        "подниматься",
                        "взбираться"
                ],
                "transcription": "bardzranal"
        },
        {
                "armenian": "ժամացույց",
                "translations": [
                        "часы",
                        "наручные часы",
                        "настенные часы"
                ],
                "transcription": "zhamats’uyts’"
        },
        {
                "armenian": "փակել",
                "translations": [
                        "закрыть",
                        "закрывать",
                        "завершить"
                ],
                "transcription": "p’akel"
        },
        {
                "armenian": "հագուստ",
                "translations": [
                        "одежда",
                        "наряд",
                        "костюм"
                ],
                "transcription": "hagust"
        },
        {
                "armenian": "ակումբ",
                "translations": [
                        "клуб",
                        "ночной клуб"
                ],
                "transcription": "akumb"
        },
        {
                "armenian": "վերարկու",
                "translations": [
                        "пальто",
                        "пиджак"
                ],
                "transcription": "verarku"
        },
        {
                "armenian": "սուրճ",
                "translations": [
                        "кофе",
                        "кофейное зерно",
                        "кофейный боб"
                ],
                "transcription": "surch"
        },
        {
                "armenian": "ցուրտ",
                "translations": [
                        "холод",
                        "холодно",
                        "холодный"
                ],
                "transcription": "ts’urt"
        },
        {
                "armenian": "գույն",
                "translations": [
                        "цвет",
                        "краска",
                        "колер"
                ],
                "transcription": "guyn"
        },
        {
                "armenian": "գալ",
                "translations": [
                        "прийти",
                        "приходить",
                        "прибыть"
                ],
                "transcription": "gal"
        },
        {
                "armenian": "սովորական",
                "translations": [
                        "обычный",
                        "обыкновенный",
                        "простой"
                ],
                "transcription": "sovorakan"
        },
        {
                "armenian": "ընկերություն",
                "translations": [
                        "компания",
                        "общество"
                ],
                "transcription": "ynkerut’yun"
        },
        {
                "armenian": "համեմատել",
                "translations": [
                        "сравнить"
                ],
                "transcription": "hamematel"
        },
        {
                "armenian": "ամբողջական",
                "translations": [
                        "полный",
                        "целостный"
                ],
                "transcription": "amboghjakan"
        },
        {
                "armenian": "համակարգիչ",
                "translations": [
                        "компьютер",
                        "эвм"
                ],
                "transcription": "hamakargich’"
        },
        {
                "armenian": "համերգ",
                "translations": [
                        "концерт"
                ],
                "transcription": "hamerg"
        },
        {
                "armenian": "զրույց",
                "translations": [
                        "разговор",
                        "беседа",
                        "диалог"
                ],
                "transcription": "zruyts’"
        },
        {
                "armenian": "եփել",
                "translations": [
                        "варить",
                        "готовить",
                        "приготовить"
                ],
                "transcription": "yep’el"
        },
        {
                "armenian": "խոհարարություն",
                "translations": [
                        "кулинария"
                ],
                "transcription": "khohararut’yun"
        },
        {
                "armenian": "զով",
                "translations": [
                        "прохладный",
                        "свежий",
                        "холодноватый"
                ],
                "transcription": "zov"
        },
        {
                "armenian": "ճիշտ",
                "translations": [
                        "правильный",
                        "истинный",
                        "верный"
                ],
                "transcription": "chisht"
        },
        {
                "armenian": "ծախս",
                "translations": [
                        "стоимость",
                        "себестоимость",
                        "цена"
                ],
                "transcription": "tsakhs"
        },
        {
                "armenian": "երկիր",
                "translations": [
                        "страна",
                        "земля",
                        "государство"
                ],
                "transcription": "yerkir"
        },
        {
                "armenian": "կուրս",
                "translations": [
                        "курс",
                        "курсы",
                        "валютный курс"
                ],
                "transcription": "kurs"
        },
        {
                "armenian": "զարմիկ",
                "translations": [
                        "племянник",
                        "кузен",
                        "кузина"
                ],
                "transcription": "zarmik"
        },
        {
                "armenian": "կով",
                "translations": [
                        "корова"
                ],
                "transcription": "kov"
        },
        {
                "armenian": "սերուցք",
                "translations": [
                        "сливки",
                        "сметана"
                ],
                "transcription": "seruts’k’"
        },
        {
                "armenian": "ստեղծել",
                "translations": [
                        "сделать",
                        "основать",
                        "делать"
                ],
                "transcription": "steghtsel"
        },
        {
                "armenian": "մշակույթ",
                "translations": [
                        "культура"
                ],
                "transcription": "mshakuyt’"
        },
        {
                "armenian": "գավաթ",
                "translations": [
                        "кубок",
                        "горшок",
                        "кружка"
                ],
                "transcription": "gavat’"
        },
        {
                "armenian": "հաճախորդ",
                "translations": [
                        "клиент",
                        "покупатель",
                        "заказчик"
                ],
                "transcription": "hachakhord"
        },
        {
                "armenian": "կտրել",
                "translations": [
                        "резать",
                        "рубить",
                        "отламывать"
                ],
                "transcription": "ktrel"
        },
        {
                "armenian": "հայրիկ",
                "translations": [
                        "отец",
                        "папа"
                ],
                "transcription": "hayrik"
        },
        {
                "armenian": "պարել",
                "translations": [
                        "танцевать",
                        "плясать",
                        "потанцевать"
                ],
                "transcription": "parel"
        },
        {
                "armenian": "պարող",
                "translations": [
                        "танцор",
                        "плясунья",
                        "балерина"
                ],
                "transcription": "parogh"
        },
        {
                "armenian": "վտանգավոր",
                "translations": [
                        "опасный",
                        "рискованный"
                ],
                "transcription": "vtangavor"
        },
        {
                "armenian": "մութ",
                "translations": [
                        "темный",
                        "мрачный",
                        "темнота"
                ],
                "transcription": "mut’"
        },
        {
                "armenian": "ամսաթիվը",
                "translations": [
                        "дата"
                ],
                "transcription": "amsat’ivy"
        },
        {
                "armenian": "դուստրը",
                "translations": [
                        "дочка",
                        "дочь"
                ],
                "transcription": "dustry"
        },
        {
                "armenian": "օր",
                "translations": [
                        "день",
                        "сутки",
                        "дневное время"
                ],
                "transcription": "or"
        },
        {
                "armenian": "սիրելի",
                "translations": [
                        "дорогой",
                        "любимый",
                        "милый"
                ],
                "transcription": "sireli"
        },
        {
                "armenian": "դեկտեմբեր",
                "translations": [
                        "декабрь"
                ],
                "transcription": "dektember"
        },
        {
                "armenian": "որոշել",
                "translations": [
                        "решить",
                        "решать"
                ],
                "transcription": "voroshel"
        },
        {
                "armenian": "համեղ",
                "translations": [
                        "вкусный",
                        "прелестный",
                        "лакомый"
                ],
                "transcription": "hamegh"
        },
        {
                "armenian": "նկարագրել",
                "translations": [
                        "описать",
                        "описывать"
                ],
                "transcription": "nkaragrel"
        },
        {
                "armenian": "նկարագրությունը",
                "translations": [
                        "описание"
                ],
                "transcription": "nkaragrut’yuny"
        },
        {
                "armenian": "գրասեղան",
                "translations": [
                        "письменный стол",
                        "стол"
                ],
                "transcription": "graseghan"
        },
        {
                "armenian": "սեղան",
                "translations": [
                        "стол"
                ],
                "transcription": "seghan"
        },
        {
                "armenian": "մանրամասն",
                "translations": [
                        "подробно"
                ],
                "transcription": "manramasn"
        },
        {
                "armenian": "երկխոսություն",
                "translations": [
                        "диалог",
                        "беседа",
                        "разговор"
                ],
                "transcription": "yerkkhosut’yun"
        },
        {
                "armenian": "բառարան",
                "translations": [
                        "словарь"
                ],
                "transcription": "barraran"
        },
        {
                "armenian": "մեռնել",
                "translations": [
                        "умирать",
                        "умереть",
                        "помереть"
                ],
                "transcription": "merrnel"
        },
        {
                "armenian": "տարբերությունը",
                "translations": [
                        "остаток",
                        "разница"
                ],
                "transcription": "tarberut’yuny"
        },
        {
                "armenian": "տարբեր",
                "translations": [
                        "разный",
                        "различный",
                        "другой"
                ],
                "transcription": "tarber"
        },
        {
                "armenian": "ընթրիք",
                "translations": [
                        "ужин"
                ],
                "transcription": "ynt’rik’"
        },
        {
                "armenian": "կեղտոտ",
                "translations": [
                        "грязный",
                        "подлый",
                        "сальный"
                ],
                "transcription": "keghtot"
        },
        {
                "armenian": "քննարկել",
                "translations": [
                        "обсудить",
                        "обсуждать",
                        "дискутировать"
                ],
                "transcription": "k’nnarkel"
        },
        {
                "armenian": "պնակ",
                "translations": [
                        "тарелка",
                        "блюдо",
                        "блюдце"
                ],
                "transcription": "pnak"
        },
        {
                "armenian": "անել",
                "translations": [
                        "делать",
                        "сделать",
                        "изготовить"
                ],
                "transcription": "anel"
        },
        {
                "armenian": "բժիշկ",
                "translations": [
                        "врач",
                        "доктор",
                        "лекарь"
                ],
                "transcription": "bzhishk"
        },
        {
                "armenian": "շուն",
                "translations": [
                        "собака",
                        "пес"
                ],
                "transcription": "shun"
        },
        {
                "armenian": "դուռ",
                "translations": [
                        "дверь",
                        "двери"
                ],
                "transcription": "durr"
        },
        {
                "armenian": "ներքեւ",
                "translations": [
                        "низ",
                        "дно",
                        "нижняя часть"
                ],
                "transcription": "nerk’ev"
        },
        {
                "armenian": "նկարել",
                "translations": [
                        "рисовать",
                        "нарисовать",
                        "писать"
                ],
                "transcription": "nkarel"
        },
        {
                "armenian": "զգեստ",
                "translations": [
                        "платье",
                        "одежда",
                        "костюм"
                ],
                "transcription": "zgest"
        },
        {
                "armenian": "խմել",
                "translations": [
                        "пить",
                        "выпить",
                        "выпивать"
                ],
                "transcription": "khmel"
        },
        {
                "armenian": "քշել",
                "translations": [
                        "водить"
                ],
                "transcription": "k’shel"
        },
        {
                "armenian": "վարորդ",
                "translations": [
                        "водитель",
                        "шофер",
                        "водительница"
                ],
                "transcription": "varord"
        },
        {
                "armenian": "ընթացքում",
                "translations": [
                        "в течение",
                        "во время"
                ],
                "transcription": "ynt’ats’k’um"
        },
        {
                "armenian": "յուրաքանչյուր",
                "translations": [
                        "каждый"
                ],
                "transcription": "yurak’anch’yur"
        },
        {
                "armenian": "ականջ",
                "translations": [
                        "ухо"
                ],
                "transcription": "akanj"
        },
        {
                "armenian": "վաղ",
                "translations": [
                        "ранний",
                        "рано"
                ],
                "transcription": "vagh"
        },
        {
                "armenian": "արեւելյան",
                "translations": [
                        "восточный"
                ],
                "transcription": "arevelyan"
        },
        {
                "armenian": "հեշտ",
                "translations": [
                        "легкий",
                        "простой",
                        "легко"
                ],
                "transcription": "hesht"
        },
        {
                "armenian": "ուտել",
                "translations": [
                        "есть",
                        "кушать",
                        "поесть"
                ],
                "transcription": "utel"
        },
        {
                "armenian": "ձու",
                "translations": [
                        "яйцо"
                ],
                "transcription": "dzu"
        },
        {
                "armenian": "ութ",
                "translations": [
                        "восемь",
                        "восьмеро"
                ],
                "transcription": "ut’"
        },
        {
                "armenian": "տասնութ",
                "translations": [
                        "восемнадцать"
                ],
                "transcription": "tasnut’"
        },
        {
                "armenian": "ութսուն",
                "translations": [
                        "восемьдесят"
                ],
                "transcription": "ut’sun"
        },
        {
                "armenian": "փիղ",
                "translations": [
                        "слон",
                        "слониха"
                ],
                "transcription": "p’igh"
        },
        {
                "armenian": "տասնմեկ",
                "translations": [
                        "одиннадцать"
                ],
                "transcription": "tasnmek"
        },
        {
                "armenian": "էլի",
                "translations": [
                        "опять",
                        "снова",
                        "еще раз"
                ],
                "transcription": "eli"
        },
        {
                "armenian": "վերջ",
                "translations": [
                        "конец",
                        "край",
                        "завершение"
                ],
                "transcription": "verj"
        },
        {
                "armenian": "հաճույք",
                "translations": [
                        "удовольствие",
                        "радость",
                        "наслаждение"
                ],
                "transcription": "hachuyk’"
        },
        {
                "armenian": "բավական",
                "translations": [
                        "достаточно",
                        "довольно"
                ],
                "transcription": "bavakan"
        },
        {
                "armenian": "հավասար",
                "translations": [
                        "ровный",
                        "одинаковый",
                        "равный"
                ],
                "transcription": "havasar"
        },
        {
                "armenian": "երեկո",
                "translations": [
                        "вечер",
                        "ночь"
                ],
                "transcription": "yereko"
        },
        {
                "armenian": "պատահար",
                "translations": [
                        "происшествие",
                        "случай",
                        "событие"
                ],
                "transcription": "patahar"
        },
        {
                "armenian": "ամեն",
                "translations": [
                        "каждый",
                        "всякий"
                ],
                "transcription": "amen"
        },
        {
                "armenian": "բոլորը",
                "translations": [
                        "каждый",
                        "всякий",
                        "все"
                ],
                "transcription": "bolory"
        },
        {
                "armenian": "ամեն ինչ",
                "translations": [
                        "все",
                        "всё"
                ],
                "transcription": "amen inch’"
        },
        {
                "armenian": "քննություն",
                "translations": [
                        "экзамен",
                        "тест"
                ],
                "transcription": "k’nnut’yun"
        },
        {
                "armenian": "օրինակ",
                "translations": [
                        "пример",
                        "например",
                        "образец"
                ],
                "transcription": "orinak"
        },
        {
                "armenian": "ոգեւորված",
                "translations": [
                        "взволнованный"
                ],
                "transcription": "vogevorvats"
        },
        {
                "armenian": "հուզիչ",
                "translations": [
                        "захватывающий"
                ],
                "transcription": "huzich’"
        },
        {
                "armenian": "վարժություն",
                "translations": [
                        "упражнение",
                        "зарядка",
                        "физзарядка"
                ],
                "transcription": "varzhut’yun"
        },
        {
                "armenian": "թանկ",
                "translations": [
                        "дорогой",
                        "ценный"
                ],
                "transcription": "t’ank"
        },
        {
                "armenian": "բացատրել",
                "translations": [
                        "объяснять",
                        "объяснить"
                ],
                "transcription": "bats’atrel"
        },
        {
                "armenian": "հատկապես",
                "translations": [
                        "особенно",
                        "первоочередно",
                        "главным образом"
                ],
                "transcription": "hatkapes"
        },
        {
                "armenian": "աչք",
                "translations": [
                        "глаз",
                        "око"
                ],
                "transcription": "ach’k’"
        },
        {
                "armenian": "դեմք",
                "translations": [
                        "лицо"
                ],
                "transcription": "demk’"
        },
        {
                "armenian": "փաստ",
                "translations": [
                        "факт",
                        "доказательство"
                ],
                "transcription": "p’ast"
        },
        {
                "armenian": "ընկնել",
                "translations": [
                        "падать",
                        "упасть",
                        "пасть"
                ],
                "transcription": "ynknel"
        },
        {
                "armenian": "կեղծ",
                "translations": [
                        "фальшивый",
                        "ложный",
                        "поддельный"
                ],
                "transcription": "keghts"
        },
        {
                "armenian": "ընտանիք",
                "translations": [
                        "семья",
                        "семейство",
                        "род"
                ],
                "transcription": "yntanik’"
        },
        {
                "armenian": "նշանավոր",
                "translations": [
                        "знаменитый",
                        "известный"
                ],
                "transcription": "nshanavor"
        },
        {
                "armenian": "տարօրինակ",
                "translations": [
                        "странный",
                        "чудной",
                        "необычный"
                ],
                "transcription": "tarorinak"
        },
        {
                "armenian": "հեռու",
                "translations": [
                        "дальний",
                        "далекий",
                        "далече"
                ],
                "transcription": "herru"
        },
        {
                "armenian": "ագարակ",
                "translations": [
                        "ферма",
                        "хозяйство",
                        "усадьба"
                ],
                "transcription": "agarak"
        },
        {
                "armenian": "ֆերմեր",
                "translations": [
                        "фермер",
                        "земледелец",
                        "крестьянин"
                ],
                "transcription": "fermer"
        },
        {
                "armenian": "արագ",
                "translations": [
                        "быстро",
                        "живо",
                        "быстрый"
                ],
                "transcription": "arag"
        },
        {
                "armenian": "չաղ",
                "translations": [
                        "жир"
                ],
                "transcription": "ch’agh"
        },
        {
                "armenian": "փետրվար",
                "translations": [
                        "февраль"
                ],
                "transcription": "p’etrvar"
        },
        {
                "armenian": "զգալ",
                "translations": [
                        "чувствовать",
                        "почувствовать",
                        "ощутить"
                ],
                "transcription": "zgal"
        },
        {
                "armenian": "զգացմունք",
                "translations": [
                        "чувство",
                        "эмоция",
                        "симпатия"
                ],
                "transcription": "zgats’munk’"
        },
        {
                "armenian": "տոն",
                "translations": [
                        "праздник",
                        "фестиваль",
                        "выходной день"
                ],
                "transcription": "ton"
        },
        {
                "armenian": "քիչ",
                "translations": [
                        "мало",
                        "несколько",
                        "немного"
                ],
                "transcription": "k’ich’"
        },
        {
                "armenian": "տասնհինգ",
                "translations": [
                        "пятнадцать"
                ],
                "transcription": "tasnhing"
        },
        {
                "armenian": "հինգերորդ",
                "translations": [
                        "пятый",
                        "5-ый"
                ],
                "transcription": "hingerord"
        },
        {
                "armenian": "հիսուն",
                "translations": [
                        "пятьдесят"
                ],
                "transcription": "hisun"
        },
        {
                "armenian": "լցնել",
                "translations": [
                        "лить",
                        "наполнять",
                        "насыпать"
                ],
                "transcription": "lts’nel"
        },
        {
                "armenian": "վերջին",
                "translations": [
                        "последний",
                        "прошлый",
                        "предыдущий"
                ],
                "transcription": "verjin"
        },
        {
                "armenian": "գտնել",
                "translations": [
                        "найти",
                        "находить"
                ],
                "transcription": "gtnel"
        },
        {
                "armenian": "վերջացնել",
                "translations": [
                        "завершить",
                        "закончить",
                        "окончить"
                ],
                "transcription": "verjats’nel"
        },
        {
                "armenian": "կրակ",
                "translations": [
                        "огонь",
                        "костер",
                        "пламя"
                ],
                "transcription": "krak"
        },
        {
                "armenian": "առաջին",
                "translations": [
                        "первый",
                        "во-первых"
                ],
                "transcription": "arrajin"
        },
        {
                "armenian": "ձուկ",
                "translations": [
                        "рыба"
                ],
                "transcription": "dzuk"
        },
        {
                "armenian": "հինգ",
                "translations": [
                        "пять",
                        "пятёрка",
                        "пятеро"
                ],
                "transcription": "hing"
        },
        {
                "armenian": "հարթ",
                "translations": [
                        "гладкий",
                        "плоский",
                        "ровный"
                ],
                "transcription": "hart’"
        },
        {
                "armenian": "թռիչք",
                "translations": [
                        "полет",
                        "перелет",
                        "рейс"
                ],
                "transcription": "t’rrich’k’"
        },
        {
                "armenian": "հատակ",
                "translations": [
                        "пол"
                ],
                "transcription": "hatak"
        },
        {
                "armenian": "ծաղիկ",
                "translations": [
                        "цветок",
                        "цветы"
                ],
                "transcription": "tsaghik"
        },
        {
                "armenian": "ճանճ",
                "translations": [
                        "муха"
                ],
                "transcription": "chanch"
        },
        {
                "armenian": "հետեւել",
                "translations": [
                        "следовать",
                        "следить"
                ],
                "transcription": "hetevel"
        },
        {
                "armenian": "սնունդ",
                "translations": [
                        "пища",
                        "корм",
                        "еда"
                ],
                "transcription": "snund"
        },
        {
                "armenian": "ոտք",
                "translations": [
                        "нога",
                        "стопа",
                        "ступня"
                ],
                "transcription": "votk’"
        },
        {
                "armenian": "համար",
                "translations": [
                        "для",
                        "ради",
                        "номер"
                ],
                "transcription": "hamar"
        },
        {
                "armenian": "մոռանալ",
                "translations": [
                        "забывать",
                        "забыть"
                ],
                "transcription": "morranal"
        },
        {
                "armenian": "ձեւ",
                "translations": [
                        "форма",
                        "способ",
                        "метод"
                ],
                "transcription": "dzev"
        },
        {
                "armenian": "քառասուն",
                "translations": [
                        "сорок"
                ],
                "transcription": "k’arrasun"
        },
        {
                "armenian": "չորս",
                "translations": [
                        "четыре",
                        "четверка"
                ],
                "transcription": "ch’vors"
        },
        {
                "armenian": "տասնչորս",
                "translations": [
                        "четырнадцать"
                ],
                "transcription": "tasnch’vors"
        },
        {
                "armenian": "չորրորդ",
                "translations": [
                        "четвертый"
                ],
                "transcription": "ch’vorrord"
        },
        {
                "armenian": "ազատ",
                "translations": [
                        "свободный",
                        "вольный"
                ],
                "transcription": "azat"
        },
        {
                "armenian": "ուրբաթ",
                "translations": [
                        "пятница"
                ],
                "transcription": "urbat’"
        },
        {
                "armenian": "ընկեր",
                "translations": [
                        "друг",
                        "приятель",
                        "подруга"
                ],
                "transcription": "ynker"
        },
        {
                "armenian": "բարեկամություն",
                "translations": [
                        "дружба"
                ],
                "transcription": "barekamut’yun"
        },
        {
                "armenian": "ընկերաբար",
                "translations": [
                        "дружелюбно",
                        "дружественно",
                        "любезно"
                ],
                "transcription": "ynkerabar"
        },
        {
                "armenian": "ճակատ",
                "translations": [
                        "лоб",
                        "фасад",
                        "фронт"
                ],
                "transcription": "chakat"
        },
        {
                "armenian": "պտուղ",
                "translations": [
                        "плод",
                        "фрукт",
                        "фрукты"
                ],
                "transcription": "ptugh"
        },
        {
                "armenian": "լիքը",
                "translations": [
                        "полный"
                ],
                "transcription": "lik’y"
        },
        {
                "armenian": "զվարճանք",
                "translations": [
                        "веселье"
                ],
                "transcription": "zvarchank’"
        },
        {
                "armenian": "զվարճալի",
                "translations": [
                        "странный",
                        "чудной",
                        "необычный"
                ],
                "transcription": "zvarchali"
        },
        {
                "armenian": "ապագա",
                "translations": [
                        "будущее",
                        "будущий",
                        "грядущее"
                ],
                "transcription": "apaga"
        },
        {
                "armenian": "խաղ",
                "translations": [
                        "игра"
                ],
                "transcription": "khagh"
        },
        {
                "armenian": "պարտեզ",
                "translations": [
                        "сад",
                        "огород"
                ],
                "transcription": "partez"
        },
        {
                "armenian": "աշխարհագրություն",
                "translations": [
                        "география"
                ],
                "transcription": "ashkharhagrut’yun"
        },
        {
                "armenian": "ստանալ",
                "translations": [
                        "получить",
                        "получать",
                        "приобрести"
                ],
                "transcription": "stanal"
        },
        {
                "armenian": "աղջիկ",
                "translations": [
                        "девочка",
                        "девушка"
                ],
                "transcription": "aghjik"
        },
        {
                "armenian": "ընկերուհի",
                "translations": [
                        "подруга",
                        "девушка",
                        "друг"
                ],
                "transcription": "ynkeruhi"
        },
        {
                "armenian": "տալ",
                "translations": [
                        "давать",
                        "дать"
                ],
                "transcription": "tal"
        },
        {
                "armenian": "ապակի",
                "translations": [
                        "стекло",
                        "прозрачный",
                        "история стекла"
                ],
                "transcription": "apaki"
        },
        {
                "armenian": "գնալ",
                "translations": [
                        "идти",
                        "ходить",
                        "ехать"
                ],
                "transcription": "gnal"
        },
        {
                "armenian": "լավ",
                "translations": [
                        "хороший",
                        "хорошо",
                        "добрый"
                ],
                "transcription": "lav"
        },
        {
                "armenian": "ցտեսություն",
                "translations": [
                        "пока",
                        "до свидания",
                        "увидеться"
                ],
                "transcription": "ts’tesut’yun"
        },
        {
                "armenian": "պապիկ",
                "translations": [
                        "дед",
                        "дедушка",
                        "папа"
                ],
                "transcription": "papik"
        },
        {
                "armenian": "տատիկ",
                "translations": [
                        "бабушка",
                        "баба",
                        "бабуля"
                ],
                "transcription": "tatik"
        },
        {
                "armenian": "հիանալի",
                "translations": [
                        "здорово",
                        "клевый",
                        "потрясный"
                ],
                "transcription": "hianali"
        },
        {
                "armenian": "կանաչ",
                "translations": [
                        "зеленый",
                        "зелень",
                        "зеленый цвет"
                ],
                "transcription": "kanach’"
        },
        {
                "armenian": "մոխրագույն",
                "translations": [
                        "серый",
                        "седой",
                        "сивый"
                ],
                "transcription": "mokhraguyn"
        },
        {
                "armenian": "խումբ",
                "translations": [
                        "группа",
                        "коллектив",
                        "собрание"
                ],
                "transcription": "khumb"
        },
        {
                "armenian": "աճել",
                "translations": [
                        "расти",
                        "вырасти",
                        "вырастать"
                ],
                "transcription": "achel"
        },
        {
                "armenian": "գուշակել",
                "translations": [
                        "угадать"
                ],
                "transcription": "gushakel"
        },
        {
                "armenian": "կիթառ",
                "translations": [
                        "гитара"
                ],
                "transcription": "kit’arr"
        },
        {
                "armenian": "մարզասրահ",
                "translations": [
                        "спортивный зал",
                        "фитнес-клуб"
                ],
                "transcription": "marzasrah"
        },
        {
                "armenian": "մազեր",
                "translations": [
                        "волосы",
                        "волос",
                        "волосинка"
                ],
                "transcription": "mazer"
        },
        {
                "armenian": "կես",
                "translations": [
                        "половина"
                ],
                "transcription": "kes"
        },
        {
                "armenian": "ձեռք",
                "translations": [
                        "рука"
                ],
                "transcription": "dzerrk’"
        },
        {
                "armenian": "պատահել",
                "translations": [
                        "произойти",
                        "случиться",
                        "происходить"
                ],
                "transcription": "patahel"
        },
        {
                "armenian": "ուրախ",
                "translations": [
                        "радостный",
                        "веселый",
                        "счастливый"
                ],
                "transcription": "urakh"
        },
        {
                "armenian": "դժվար",
                "translations": [
                        "трудный",
                        "тяжелый",
                        "сложный"
                ],
                "transcription": "dzhvar"
        },
        {
                "armenian": "գլխարկ",
                "translations": [
                        "шляпа",
                        "шапка"
                ],
                "transcription": "glkhark"
        },
        {
                "armenian": "ատելություն",
                "translations": [
                        "ненависть"
                ],
                "transcription": "atelut’yun"
        },
        {
                "armenian": "ունենալ",
                "translations": [
                        "иметь",
                        "обладать",
                        "владеть"
                ],
                "transcription": "unenal"
        },
        {
                "armenian": "նա",
                "translations": [
                        "он",
                        "она"
                ],
                "transcription": "na"
        },
        {
                "armenian": "գլուխ",
                "translations": [
                        "голова",
                        "глава",
                        "мозг"
                ],
                "transcription": "glukh"
        },
        {
                "armenian": "առողջություն",
                "translations": [
                        "здоровье",
                        "будь здоров",
                        "будьте здоровы"
                ],
                "transcription": "arroghjut’yun"
        },
        {
                "armenian": "առողջ",
                "translations": [
                        "здоровый"
                ],
                "transcription": "arroghj"
        },
        {
                "armenian": "լսել",
                "translations": [
                        "слышать",
                        "слушать",
                        "услышать"
                ],
                "transcription": "lsel"
        },
        {
                "armenian": "բարև ձեզ",
                "translations": [
                        "здравствуйте"
                ],
                "transcription": "barev dzez"
        },
        {
                "armenian": "օգնություն",
                "translations": [
                        "помощь",
                        "поддержка",
                        "содействие"
                ],
                "transcription": "ognut’yun"
        },
        {
                "armenian": "այստեղ",
                "translations": [
                        "здесь",
                        "сюда",
                        "тут"
                ],
                "transcription": "aystegh"
        },
        {
                "armenian": "բարև",
                "translations": [
                        "привет"
                ],
                "transcription": "barev"
        },
        {
                "armenian": "բարձր",
                "translations": [
                        "высокий",
                        "громкий",
                        "громко"
                ],
                "transcription": "bardzr"
        },
        {
                "armenian": "նրան",
                "translations": [
                        "ее",
                        "его",
                        "ей"
                ],
                "transcription": "nran"
        },
        {
                "armenian": "նրա",
                "translations": [
                        "ее",
                        "свой",
                        "его"
                ],
                "transcription": "nra"
        },
        {
                "armenian": "պատմություն",
                "translations": [
                        "история",
                        "рассказ",
                        "повесть"
                ],
                "transcription": "patmut’yun"
        },
        {
                "armenian": "տնային աշխատանք",
                "translations": [
                        "домашнее задание",
                        "домашняя работа"
                ],
                "transcription": "tnayin ashkhatank’"
        },
        {
                "armenian": "հույս",
                "translations": [
                        "надежда"
                ],
                "transcription": "huys"
        },
        {
                "armenian": "ձի",
                "translations": [
                        "лошадь",
                        "конь"
                ],
                "transcription": "dzi"
        },
        {
                "armenian": "հիվանդանոց",
                "translations": [
                        "больница",
                        "госпиталь",
                        "клиника"
                ],
                "transcription": "hivandanots’"
        },
        {
                "armenian": "տաք",
                "translations": [
                        "горячий"
                ],
                "transcription": "tak’"
        },
        {
                "armenian": "հյուրանոց",
                "translations": [
                        "гостиница",
                        "отель",
                        "корчма"
                ],
                "transcription": "hyuranots’"
        },
        {
                "armenian": "ժամ",
                "translations": [
                        "час",
                        "время",
                        "часы"
                ],
                "transcription": "zham"
        },
        {
                "armenian": "տուն",
                "translations": [
                        "дом"
                ],
                "transcription": "tun"
        },
        {
                "armenian": "ինչպես",
                "translations": [
                        "как",
                        "каким образом"
                ],
                "transcription": "inch’pes"
        },
        {
                "armenian": "սակայն",
                "translations": [
                        "но",
                        "однако",
                        "все же"
                ],
                "transcription": "sakayn"
        },
        {
                "armenian": "հարյուր",
                "translations": [
                        "сто",
                        "сотня"
                ],
                "transcription": "haryur"
        },
        {
                "armenian": "սոված",
                "translations": [
                        "голодный"
                ],
                "transcription": "sovats"
        },
        {
                "armenian": "ամուսին",
                "translations": [
                        "муж",
                        "супруг",
                        "супруга"
                ],
                "transcription": "amusin"
        },
        {
                "armenian": "ես",
                "translations": [
                        "я"
                ],
                "transcription": "yes"
        },
        {
                "armenian": "սառույց",
                "translations": [
                        "лед"
                ],
                "transcription": "sarruyts’"
        },
        {
                "armenian": "պաղպաղակ",
                "translations": [
                        "мороженое"
                ],
                "transcription": "paghpaghak"
        },
        {
                "armenian": "գաղափար",
                "translations": [
                        "идея",
                        "мысль",
                        "концепция"
                ],
                "transcription": "gaghap’ar"
        },
        {
                "armenian": "եթե",
                "translations": [
                        "если",
                        "ежели",
                        "коли"
                ],
                "transcription": "yet’e"
        },
        {
                "armenian": "պատկերացրեք",
                "translations": [
                        "ожидать"
                ],
                "transcription": "patkerats’rek’"
        },
        {
                "armenian": "կարևոր",
                "translations": [
                        "важный",
                        "значимый"
                ],
                "transcription": "karevor"
        },
        {
                "armenian": "բարելավել",
                "translations": [
                        "улучшать",
                        "оздоровить",
                        "улучшить"
                ],
                "transcription": "barelavel"
        },
        {
                "armenian": "ներս",
                "translations": [
                        "внутрь",
                        "внутри"
                ],
                "transcription": "ners"
        },
        {
                "armenian": "ներառում",
                "translations": [
                        "содержать",
                        "включать"
                ],
                "transcription": "nerarrum"
        },
        {
                "armenian": "տեղեկատվություն",
                "translations": [
                        "информация",
                        "сведение",
                        "инфа"
                ],
                "transcription": "teghekatvut’yun"
        },
        {
                "armenian": "հետաքրքրություն",
                "translations": [
                        "интересовать"
                ],
                "transcription": "hetak’rk’rut’yun"
        },
        {
                "armenian": "հետաքրքրված",
                "translations": [
                        "заинтересованный"
                ],
                "transcription": "hetak’rk’rvats"
        },
        {
                "armenian": "հետաքրքիր",
                "translations": [
                        "интересный",
                        "занятный"
                ],
                "transcription": "hetak’rk’ir"
        },
        {
                "armenian": "ինտերնետ",
                "translations": [
                        "интернет",
                        "сеть"
                ],
                "transcription": "internet"
        },
        {
                "armenian": "հարցազրույց",
                "translations": [
                        "интервью",
                        "собеседование",
                        "интервью (журналистика)"
                ],
                "transcription": "harts’azruyts’"
        },
        {
                "armenian": "մեջ",
                "translations": [
                        "в",
                        "внутри",
                        "внутрь"
                ],
                "transcription": "mej"
        },
        {
                "armenian": "ներկայացնել",
                "translations": [
                        "вставлять",
                        "помещать"
                ],
                "transcription": "nerkayats’nel"
        },
        {
                "armenian": "կղզի",
                "translations": [
                        "остров"
                ],
                "transcription": "kghzi"
        },
        {
                "armenian": "բաճկոն",
                "translations": [
                        "куртка"
                ],
                "transcription": "bachkon"
        },
        {
                "armenian": "Հունվար",
                "translations": [
                        "январь"
                ],
                "transcription": "Hunvar"
        },
        {
                "armenian": "ջինս",
                "translations": [
                        "джинсы"
                ],
                "transcription": "jins"
        },
        {
                "armenian": "աշխատանք",
                "translations": [
                        "работа",
                        "труд",
                        "занятие"
                ],
                "transcription": "ashkhatank’"
        },
        {
                "armenian": "միանալ",
                "translations": [
                        "соединить",
                        "соединять",
                        "присоединиться"
                ],
                "transcription": "mianal"
        },
        {
                "armenian": "ճանապարհորդություն",
                "translations": [
                        "путешествие",
                        "поездка"
                ],
                "transcription": "chanaparhordut’yun"
        },
        {
                "armenian": "հյութ",
                "translations": [
                        "сок"
                ],
                "transcription": "hyut’"
        },
        {
                "armenian": "հուլիս",
                "translations": [
                        "июль"
                ],
                "transcription": "hulis"
        },
        {
                "armenian": "Հունիս",
                "translations": [
                        "июнь"
                ],
                "transcription": "Hunis"
        },
        {
                "armenian": "ուղղակի",
                "translations": [
                        "только",
                        "лишь",
                        "прямо"
                ],
                "transcription": "ughghaki"
        },
        {
                "armenian": "պահել",
                "translations": [
                        "держать",
                        "хранить",
                        "сохранить"
                ],
                "transcription": "pahel"
        },
        {
                "armenian": "բանալի",
                "translations": [
                        "ключ",
                        "клавиша",
                        "кпюч"
                ],
                "transcription": "banali"
        },
        {
                "armenian": "բարի",
                "translations": [
                        "хороший",
                        "добрый"
                ],
                "transcription": "bari"
        },
        {
                "armenian": "խոհանոց",
                "translations": [
                        "кухня"
                ],
                "transcription": "khohanots’"
        },
        {
                "armenian": "գիտենալ",
                "translations": [
                        "знать"
                ],
                "transcription": "gitenal"
        },
        {
                "armenian": "հող",
                "translations": [
                        "земля",
                        "почва",
                        "грунт"
                ],
                "transcription": "hogh"
        },
        {
                "armenian": "լեզու",
                "translations": [
                        "язык",
                        "речь",
                        "лексикон"
                ],
                "transcription": "lezu"
        },
        {
                "armenian": "վերջին",
                "translations": [
                        "последний",
                        "прошлый",
                        "предыдущий"
                ],
                "transcription": "verjin"
        },
        {
                "armenian": "ուշ",
                "translations": [
                        "поздний",
                        "после",
                        "запоздалый"
                ],
                "transcription": "ush"
        },
        {
                "armenian": "հետագայում",
                "translations": [
                        "позже",
                        "после",
                        "потом"
                ],
                "transcription": "hetagayum"
        },
        {
                "armenian": "ծիծաղել",
                "translations": [
                        "смеяться",
                        "хохотать",
                        "насмехаться"
                ],
                "transcription": "tsitsaghel"
        },
        {
                "armenian": "սովորել",
                "translations": [
                        "учиться",
                        "учить",
                        "изучать"
                ],
                "transcription": "sovorel"
        },
        {
                "armenian": "հեռանալ",
                "translations": [
                        "оставить",
                        "оставлять",
                        "покидать"
                ],
                "transcription": "herranal"
        },
        {
                "armenian": "ձախ",
                "translations": [
                        "левый"
                ],
                "transcription": "dzakh"
        },
        {
                "armenian": "թող",
                "translations": [
                        "пусть",
                        "позволять"
                ],
                "transcription": "t’vogh"
        },
        {
                "armenian": "նամակ",
                "translations": [
                        "письмо",
                        "послание"
                ],
                "transcription": "namak"
        },
        {
                "armenian": "գրադարան",
                "translations": [
                        "библиотека"
                ],
                "transcription": "gradaran"
        },
        {
                "armenian": "սուտ",
                "translations": [
                        "ложь",
                        "брехня",
                        "вранье"
                ],
                "transcription": "sut"
        },
        {
                "armenian": "կյանք",
                "translations": [
                        "жизнь",
                        "житие",
                        "живот"
                ],
                "transcription": "kyank’"
        },
        {
                "armenian": "լույս",
                "translations": [
                        "свет"
                ],
                "transcription": "luys"
        },
        {
                "armenian": "դուր է գալիս",
                "translations": [
                        "нравится"
                ],
                "transcription": "dur e galis"
        },
        {
                "armenian": "գիծ",
                "translations": [
                        "линия",
                        "черта",
                        "штрих"
                ],
                "transcription": "gits"
        },
        {
                "armenian": "առյուծ",
                "translations": [
                        "лев",
                        "львица"
                ],
                "transcription": "arryuts"
        },
        {
                "armenian": "ցուցակ",
                "translations": [
                        "список",
                        "перечень",
                        "перечислить"
                ],
                "transcription": "ts’uts’ak"
        },
        {
                "armenian": "ապրել",
                "translations": [
                        "жить",
                        "проживать",
                        "прожить"
                ],
                "transcription": "aprel"
        },
        {
                "armenian": "տեղական",
                "translations": [
                        "местный"
                ],
                "transcription": "teghakan"
        },
        {
                "armenian": "երկար",
                "translations": [
                        "длинный",
                        "долгий",
                        "долго"
                ],
                "transcription": "yerkar"
        },
        {
                "armenian": "նայիել",
                "translations": [
                        "смотреть",
                        "глядеть",
                        "посмотреть"
                ],
                "transcription": "nayiyel"
        },
        {
                "armenian": "կորցնել",
                "translations": [
                        "потерять",
                        "терять",
                        "пoтeрять"
                ],
                "transcription": "korts’nel"
        },
        {
                "armenian": "սեր",
                "translations": [
                        "любовь",
                        "любимый",
                        "любимая"
                ],
                "transcription": "ser"
        },
        {
                "armenian": "մեքենա",
                "translations": [
                        "машина",
                        "автомобиль",
                        "тачка"
                ],
                "transcription": "mek’ena"
        },
        {
                "armenian": "ամսագիր",
                "translations": [
                        "журнал",
                        "газета"
                ],
                "transcription": "amsagir"
        },
        {
                "armenian": "հիմնական",
                "translations": [
                        "основной"
                ],
                "transcription": "himnakan"
        },
        {
                "armenian": "դարձնել",
                "translations": [
                        "сделать"
                ],
                "transcription": "dardznel"
        },
        {
                "armenian": "մարդ",
                "translations": [
                        "человек",
                        "муж",
                        "супруг"
                ],
                "transcription": "mard"
        },
        {
                "armenian": "քարտեզ",
                "translations": [
                        "карта",
                        "схема",
                        "сопоставление"
                ],
                "transcription": "k’artez"
        },
        {
                "armenian": "Մարտ",
                "translations": [
                        "март",
                        "битва"
                ],
                "transcription": "Mart"
        },
        {
                "armenian": "շուկա",
                "translations": [
                        "рынок",
                        "базар",
                        "ярмарка"
                ],
                "transcription": "shuka"
        },
        {
                "armenian": "ամուսնացած",
                "translations": [
                        "женатый"
                ],
                "transcription": "amusnats’ats"
        },
        {
                "armenian": "մրցույթ",
                "translations": [
                        "конкурс",
                        "состязание",
                        "соревнование"
                ],
                "transcription": "mrts’uyt’"
        },
        {
                "armenian": "մայիս",
                "translations": [
                        "май"
                ],
                "transcription": "mayis"
        },
        {
                "armenian": "գուցե",
                "translations": [
                        "авось",
                        "возможно",
                        "может быть"
                ],
                "transcription": "guts’e"
        },
        {
                "armenian": "ինձ",
                "translations": [
                        "мне",
                        "меня",
                        "мной"
                ],
                "transcription": "indz"
        },
        {
                "armenian": "ճաշ",
                "translations": [
                        "ужин",
                        "пища",
                        "еда"
                ],
                "transcription": "chash"
        },
        {
                "armenian": "նշանակում",
                "translations": [
                        "обозначение",
                        "значит",
                        "значить"
                ],
                "transcription": "nshanakum"
        },
        {
                "armenian": "իմաստ",
                "translations": [
                        "смысл",
                        "значение",
                        "толкование"
                ],
                "transcription": "imast"
        },
        {
                "armenian": "միս",
                "translations": [
                        "мясо",
                        "мякоть"
                ],
                "transcription": "mis"
        },
        {
                "armenian": "հանդիպել",
                "translations": [
                        "встречать",
                        "встретить"
                ],
                "transcription": "handipel"
        },
        {
                "armenian": "հանդիպում",
                "translations": [
                        "собрание"
                ],
                "transcription": "handipum"
        },
        {
                "armenian": "անդամ",
                "translations": [
                        "член",
                        "участник",
                        "элемент"
                ],
                "transcription": "andam"
        },
        {
                "armenian": "հաղորդագրություն",
                "translations": [
                        "сообщение",
                        "смс"
                ],
                "transcription": "haghordagrut’yun"
        },
        {
                "armenian": "կեսգիշեր",
                "translations": [
                        "полночь"
                ],
                "transcription": "kesgisher"
        },
        {
                "armenian": "կաթ",
                "translations": [
                        "молоко"
                ],
                "transcription": "kat’"
        },
        {
                "armenian": "միլիոն",
                "translations": [
                        "миллион"
                ],
                "transcription": "milion"
        },
        {
                "armenian": "րոպե",
                "translations": [
                        "минута"
                ],
                "transcription": "rope"
        },
        {
                "armenian": "կարոտել",
                "translations": [
                        "тосковать",
                        "скучать",
                        "недоставать"
                ],
                "transcription": "karotel"
        },
        {
                "armenian": "սխալ",
                "translations": [
                        "ошибка",
                        "неправильный",
                        "неверный"
                ],
                "transcription": "skhal"
        },
        {
                "armenian": "ժամանակակից",
                "translations": [
                        "современный"
                ],
                "transcription": "zhamanakakits’"
        },
        {
                "armenian": "պահ",
                "translations": [
                        "момент",
                        "миг",
                        "мгновение"
                ],
                "transcription": "pah"
        },
        {
                "armenian": "երկուշաբթի",
                "translations": [
                        "понедельник"
                ],
                "transcription": "yerkushabt’i"
        },
        {
                "armenian": "փող",
                "translations": [
                        "деньги",
                        "валюта"
                ],
                "transcription": "p’vogh"
        },
        {
                "armenian": "ամիս",
                "translations": [
                        "месяц"
                ],
                "transcription": "amis"
        },
        {
                "armenian": "ավելին",
                "translations": [
                        "больше",
                        "еще",
                        "дополнительно"
                ],
                "transcription": "avelin"
        },
        {
                "armenian": "առավոտ",
                "translations": [
                        "утро"
                ],
                "transcription": "arravot"
        },
        {
                "armenian": "մայր",
                "translations": [
                        "мать",
                        "мама"
                ],
                "transcription": "mayr"
        },
        {
                "armenian": "լեռ",
                "translations": [
                        "гора"
                ],
                "transcription": "lerr"
        },
        {
                "armenian": "մուկ",
                "translations": [
                        "мышь",
                        "компьютерная мышь"
                ],
                "transcription": "muk"
        },
        {
                "armenian": "բերան",
                "translations": [
                        "рот"
                ],
                "transcription": "beran"
        },
        {
                "armenian": "շարժվել",
                "translations": [
                        "двигаться"
                ],
                "transcription": "sharzhvel"
        },
        {
                "armenian": "թանգարան",
                "translations": [
                        "музей"
                ],
                "transcription": "t’angaran"
        },
        {
                "armenian": "երաժշտություն",
                "translations": [
                        "музыка"
                ],
                "transcription": "yerazhshtut’yun"
        },
        {
                "armenian": "իմ",
                "translations": [
                        "мой"
                ],
                "transcription": "im"
        },
        {
                "armenian": "անուն",
                "translations": [
                        "имя",
                        "название",
                        "слава"
                ],
                "transcription": "anun"
        },
        {
                "armenian": "բնական",
                "translations": [
                        "естественный",
                        "природный",
                        "натуральный"
                ],
                "transcription": "bnakan"
        },
        {
                "armenian": "մոտ",
                "translations": [
                        "близкий",
                        "рядом",
                        "около"
                ],
                "transcription": "mot"
        },
        {
                "armenian": "պետք",
                "translations": [
                        "нужно",
                        "надо",
                        "должен"
                ],
                "transcription": "petk’"
        },
        {
                "armenian": "կարիք",
                "translations": [
                        "нужда",
                        "потребность",
                        "необходимость"
                ],
                "transcription": "karik’"
        },
        {
                "armenian": "բացասական",
                "translations": [
                        "отрицательный"
                ],
                "transcription": "bats’asakan"
        },
        {
                "armenian": "հարևան",
                "translations": [
                        "сосед",
                        "соседка"
                ],
                "transcription": "harevan"
        },
        {
                "armenian": "երբեք",
                "translations": [
                        "никогда"
                ],
                "transcription": "yerbek’"
        },
        {
                "armenian": "նոր",
                "translations": [
                        "новый"
                ],
                "transcription": "nor"
        },
        {
                "armenian": "նորություններ",
                "translations": [
                        "новости",
                        "известия"
                ],
                "transcription": "norut’yunner"
        },
        {
                "armenian": "հաջորդ",
                "translations": [
                        "следующий"
                ],
                "transcription": "hajord"
        },
        {
                "armenian": "կողքին",
                "translations": [
                        "около",
                        "рядом с",
                        "у"
                ],
                "transcription": "koghk’in"
        },
        {
                "armenian": "հաճելի",
                "translations": [
                        "приятный",
                        "желанный"
                ],
                "transcription": "hacheli"
        },
        {
                "armenian": "գիշեր",
                "translations": [
                        "ночь"
                ],
                "transcription": "gisher"
        },
        {
                "armenian": "ինը",
                "translations": [
                        "девять",
                        "девятка",
                        "девятеро"
                ],
                "transcription": "iny"
        },
        {
                "armenian": "տասնինը",
                "translations": [
                        "девятнадцать"
                ],
                "transcription": "tasniny"
        },
        {
                "armenian": "իննսուն",
                "translations": [
                        "девяносто"
                ],
                "transcription": "innsun"
        },
        {
                "armenian": "ոչ",
                "translations": [
                        "нет",
                        "не"
                ],
                "transcription": "voch’"
        },
        {
                "armenian": "ոչ ոք",
                "translations": [
                        "никто"
                ],
                "transcription": "voch’ vok’"
        },
        {
                "armenian": "հյուսիս",
                "translations": [
                        "север"
                ],
                "transcription": "hyusis"
        },
        {
                "armenian": "քիթ",
                "translations": [
                        "нос"
                ],
                "transcription": "k’it’"
        },
        {
                "armenian": "չէ",
                "translations": [
                        "нет",
                        "не"
                ],
                "transcription": "ch’e"
        },
        {
                "armenian": "նշում",
                "translations": [
                        "заметка",
                        "запись"
                ],
                "transcription": "nshum"
        },
        {
                "armenian": "ոչինչ",
                "translations": [
                        "ничто",
                        "ничего"
                ],
                "transcription": "voch’inch’"
        },
        {
                "armenian": "Նոյեմբեր",
                "translations": [
                        "ноябрь"
                ],
                "transcription": "Noyember"
        },
        {
                "armenian": "հիմա",
                "translations": [
                        "сейчас",
                        "теперь",
                        "ныне"
                ],
                "transcription": "hima"
        },
        {
                "armenian": "բուժքույր",
                "translations": [
                        "медсестра",
                        "сестра",
                        "сиделка"
                ],
                "transcription": "buzhk’uyr"
        },
        {
                "armenian": "Հոկտեմբեր",
                "translations": [
                        "октябрь"
                ],
                "transcription": "Hoktember"
        },
        {
                "armenian": "ի",
                "translations": [
                        "об",
                        "про",
                        "на"
                ],
                "transcription": "i"
        },
        {
                "armenian": "անջատված",
                "translations": [
                        "выключить"
                ],
                "transcription": "anjatvats"
        },
        {
                "armenian": "գրասենյակ",
                "translations": [
                        "офис",
                        "бюро",
                        "кабинет"
                ],
                "transcription": "grasenyak"
        },
        {
                "armenian": "հաճախ",
                "translations": [
                        "часто",
                        "зачастую",
                        "частенько"
                ],
                "transcription": "hachakh"
        },
        {
                "armenian": "Լավ",
                "translations": [
                        "хорошо",
                        "хороший"
                ],
                "transcription": "Lav"
        },
        {
                "armenian": "հին",
                "translations": [
                        "старый",
                        "древний",
                        "старинный"
                ],
                "transcription": "hin"
        },
        {
                "armenian": "վրա",
                "translations": [
                        "на",
                        "над"
                ],
                "transcription": "vra"
        },
        {
                "armenian": "մեկ անգամ",
                "translations": [
                        "когда",
                        "в то время как"
                ],
                "transcription": "mek angam"
        },
        {
                "armenian": "մեկ",
                "translations": [
                        "один",
                        "кто-то",
                        "раз"
                ],
                "transcription": "mek"
        },
        {
                "armenian": "սոխ",
                "translations": [
                        "лук"
                ],
                "transcription": "sokh"
        },
        {
                "armenian": "առցանց",
                "translations": [
                        "в сети",
                        "в интернете",
                        "онлайн"
                ],
                "transcription": "arrts’ants’"
        },
        {
                "armenian": "միայն",
                "translations": [
                        "только",
                        "лишь",
                        "всего"
                ],
                "transcription": "miayn"
        },
        {
                "armenian": "բացել",
                "translations": [
                        "открыть"
                ],
                "transcription": "bats’el"
        },
        {
                "armenian": "կարծիք",
                "translations": [
                        "мнение"
                ],
                "transcription": "kartsik’"
        },
        {
                "armenian": "հակառակ",
                "translations": [
                        "нет",
                        "против"
                ],
                "transcription": "hakarrak"
        },
        {
                "armenian": "կամ",
                "translations": [
                        "или",
                        "либо",
                        "быть"
                ],
                "transcription": "kam"
        },
        {
                "armenian": "նարնջագույն",
                "translations": [
                        "оранжевый",
                        "оранжевый цвет"
                ],
                "transcription": "narnjaguyn"
        },
        {
                "armenian": "պատվիրել",
                "translations": [
                        "заказать"
                ],
                "transcription": "patvirel"
        },
        {
                "armenian": "այլ",
                "translations": [
                        "другой",
                        "иной"
                ],
                "transcription": "ayl"
        },
        {
                "armenian": "մեր",
                "translations": [
                        "наш"
                ],
                "transcription": "mer"
        },
        {
                "armenian": "դուրս",
                "translations": [
                        "на улице",
                        "из",
                        "вне"
                ],
                "transcription": "durs"
        },
        {
                "armenian": "դրսում",
                "translations": [
                        "на улице",
                        "из",
                        "вне"
                ],
                "transcription": "drsum"
        },
        {
                "armenian": "սեփական",
                "translations": [
                        "собственный"
                ],
                "transcription": "sep’akan"
        },
        {
                "armenian": "էջ",
                "translations": [
                        "страница",
                        "лист",
                        "катет"
                ],
                "transcription": "ej"
        },
        {
                "armenian": "ներկ",
                "translations": [
                        "краска"
                ],
                "transcription": "nerk"
        },
        {
                "armenian": "նկարչություն",
                "translations": [
                        "живопись",
                        "картина"
                ],
                "transcription": "nkarch’ut’yun"
        },
        {
                "armenian": "զույգ",
                "translations": [
                        "пара",
                        "чета",
                        "четный"
                ],
                "transcription": "zuyg"
        },
        {
                "armenian": "թուղթ",
                "translations": [
                        "бумага"
                ],
                "transcription": "t’ught’"
        },
        {
                "armenian": "պարբերություն",
                "translations": [
                        "абзац",
                        "параграф",
                        "период"
                ],
                "transcription": "parberut’yun"
        },
        {
                "armenian": "ծնող",
                "translations": [
                        "родитель",
                        "родительница"
                ],
                "transcription": "tsnogh"
        },
        {
                "armenian": "այգի",
                "translations": [
                        "сад",
                        "парк",
                        "огород"
                ],
                "transcription": "aygi"
        },
        {
                "armenian": "մաս",
                "translations": [
                        "часть",
                        "доля",
                        "штука"
                ],
                "transcription": "mas"
        },
        {
                "armenian": "գործընկեր",
                "translations": [
                        "коллега",
                        "сотрудник",
                        "сослуживец"
                ],
                "transcription": "gortsynker"
        },
        {
                "armenian": "անձնագիր",
                "translations": [
                        "паспорт"
                ],
                "transcription": "andznagir"
        },
        {
                "armenian": "անցյալ",
                "translations": [
                        "прошлое"
                ],
                "transcription": "ants’yal"
        },
        {
                "armenian": "վճարել",
                "translations": [
                        "платить",
                        "заплатить",
                        "оплатить"
                ],
                "transcription": "vcharel"
        },
        {
                "armenian": "գրիչ",
                "translations": [
                        "ручка",
                        "перо",
                        "авторучка"
                ],
                "transcription": "grich’"
        },
        {
                "armenian": "մատիտ",
                "translations": [
                        "карандаш",
                        "карандащ"
                ],
                "transcription": "matit"
        },
        {
                "armenian": "մարդիկ",
                "translations": [
                        "люд",
                        "люди",
                        "народ"
                ],
                "transcription": "mardik"
        },
        {
                "armenian": "պղպեղ",
                "translations": [
                        "перец"
                ],
                "transcription": "pghpegh"
        },
        {
                "armenian": "կատարյալ",
                "translations": [
                        "совершенный",
                        "идеальный",
                        "безупречный"
                ],
                "transcription": "kataryal"
        },
        {
                "armenian": "ժամանակաշրջան",
                "translations": [
                        "период"
                ],
                "transcription": "zhamanakashrjan"
        },
        {
                "armenian": "անձնական",
                "translations": [
                        "личный",
                        "частный",
                        "персональный"
                ],
                "transcription": "andznakan"
        },
        {
                "armenian": "հեռախոս",
                "translations": [
                        "телефон"
                ],
                "transcription": "herrakhos"
        },
        {
                "armenian": "լուսանկար",
                "translations": [
                        "фотография",
                        "фото",
                        "фотокарточка"
                ],
                "transcription": "lusankar"
        },
        {
                "armenian": "լուսանկարիչ",
                "translations": [
                        "фотограф"
                ],
                "transcription": "lusankarich’"
        },
        {
                "armenian": "արտահայտություն",
                "translations": [
                        "выражение",
                        "оборот"
                ],
                "transcription": "artahaytut’yun"
        },
        {
                "armenian": "դաշնամուր",
                "translations": [
                        "фортепиано",
                        "пианино",
                        "рояль"
                ],
                "transcription": "dashnamur"
        },
        {
                "armenian": "նկար",
                "translations": [
                        "картина",
                        "изображение",
                        "фотография"
                ],
                "transcription": "nkar"
        },
        {
                "armenian": "կտոր",
                "translations": [
                        "кусок",
                        "часть"
                ],
                "transcription": "ktor"
        },
        {
                "armenian": "խոզ",
                "translations": [
                        "свинья"
                ],
                "transcription": "khoz"
        },
        {
                "armenian": "վարդագույն",
                "translations": [
                        "розовый",
                        "розавый"
                ],
                "transcription": "vardaguyn"
        },
        {
                "armenian": "տեղ",
                "translations": [
                        "место",
                        "пункт",
                        "сфера"
                ],
                "transcription": "tegh"
        },
        {
                "armenian": "պլանավորել",
                "translations": [
                        "планировать"
                ],
                "transcription": "planavorel"
        },
        {
                "armenian": "ինքնաթիռ",
                "translations": [
                        "самолет",
                        "аэроплан"
                ],
                "transcription": "ink’nat’irr"
        },
        {
                "armenian": "բույս",
                "translations": [
                        "растение",
                        "растения"
                ],
                "transcription": "buys"
        },
        {
                "armenian": "խաղալ",
                "translations": [
                        "играть",
                        "гулять",
                        "поиграть"
                ],
                "transcription": "khaghal"
        },
        {
                "armenian": "խաղացող",
                "translations": [
                        "игрок"
                ],
                "transcription": "khaghats’vogh"
        },
        {
                "armenian": "խնդրեմ",
                "translations": [
                        "пожалуйста",
                        "не за что"
                ],
                "transcription": "khndrem"
        },
        {
                "armenian": "խնդրում եմ",
                "translations": [
                        "пожалуйста",
                        "будьте добры"
                ],
                "transcription": "khndrum yem"
        },
        {
                "armenian": "կետ",
                "translations": [
                        "пункт",
                        "точка"
                ],
                "transcription": "ket"
        },
        {
                "armenian": "ոստիկանություն",
                "translations": [
                        "полиция",
                        "милиция"
                ],
                "transcription": "vostikanut’yun"
        },
        {
                "armenian": "ոստիկան",
                "translations": [
                        "полицейский",
                        "полиция",
                        "полисмен"
                ],
                "transcription": "vostikan"
        },
        {
                "armenian": "լողավազան",
                "translations": [
                        "бассейн",
                        "плавательный бассейн"
                ],
                "transcription": "loghavazan"
        },
        {
                "armenian": "աղքատ",
                "translations": [
                        "бедный",
                        "нищий",
                        "бедствующий"
                ],
                "transcription": "aghk’at"
        },
        {
                "armenian": "հանրաճանաչ",
                "translations": [
                        "народный",
                        "популярный"
                ],
                "transcription": "hanrachanach’"
        },
        {
                "armenian": "դրական",
                "translations": [
                        "положительный"
                ],
                "transcription": "drakan"
        },
        {
                "armenian": "հնարավոր",
                "translations": [
                        "возможный",
                        "вероятный"
                ],
                "transcription": "hnaravor"
        },
        {
                "armenian": "փոստ",
                "translations": [
                        "почта",
                        "почтовое отделение"
                ],
                "transcription": "p’vost"
        },
        {
                "armenian": "կարտոֆիլ",
                "translations": [
                        "картофель",
                        "картошка"
                ],
                "transcription": "kartofil"
        },
        {
                "armenian": "պարապել",
                "translations": [
                        "тренироваться",
                        "упражняться",
                        "попрактиковаться"
                ],
                "transcription": "parapel"
        },
        {
                "armenian": "նախընտրել",
                "translations": [
                        "предпочесть",
                        "предпочитать"
                ],
                "transcription": "nakhyntrel"
        },
        {
                "armenian": "պատրաստել",
                "translations": [
                        "готовить",
                        "приготовить",
                        "подготовить"
                ],
                "transcription": "patrastel"
        },
        {
                "armenian": "ներկա",
                "translations": [
                        "настоящее",
                        "настоящее время"
                ],
                "transcription": "nerka"
        },
        {
                "armenian": "գին",
                "translations": [
                        "цена",
                        "стоимость",
                        "ценность"
                ],
                "transcription": "gin"
        },
        {
                "armenian": "խնդիր",
                "translations": [
                        "проблема",
                        "задача",
                        "дополнение"
                ],
                "transcription": "khndir"
        },
        {
                "armenian": "արտադրանք",
                "translations": [
                        "изделие",
                        "продукт"
                ],
                "transcription": "artadrank’"
        },
        {
                "armenian": "ծրագիր",
                "translations": [
                        "программа",
                        "план",
                        "телепрограмма"
                ],
                "transcription": "tsragir"
        },
        {
                "armenian": "նախագիծ",
                "translations": [
                        "проект"
                ],
                "transcription": "nakhagits"
        },
        {
                "armenian": "մանուշակագույն",
                "translations": [
                        "фиолетовый",
                        "фиолетовый цвет"
                ],
                "transcription": "manushakaguyn"
        },
        {
                "armenian": "դրել",
                "translations": [
                        "класть",
                        "поставить",
                        "ставить"
                ],
                "transcription": "drel"
        },
        {
                "armenian": "հարց",
                "translations": [
                        "вопрос",
                        "проблема",
                        "задача"
                ],
                "transcription": "harts’"
        },
        {
                "armenian": "հանգիստ",
                "translations": [
                        "тихий",
                        "отдых",
                        "покой"
                ],
                "transcription": "hangist"
        },
        {
                "armenian": "բավականին",
                "translations": [
                        "полностью",
                        "обоснованно"
                ],
                "transcription": "bavakanin"
        },
        {
                "armenian": "անձրև",
                "translations": [
                        "дождь"
                ],
                "transcription": "andzrev"
        },
        {
                "armenian": "կարդալ",
                "translations": [
                        "читать",
                        "прочитать"
                ],
                "transcription": "kardal"
        },
        {
                "armenian": "ընթերցող",
                "translations": [
                        "читатель",
                        "сканер"
                ],
                "transcription": "ynt’erts’vogh"
        },
        {
                "armenian": "կարդում",
                "translations": [
                        "чтение"
                ],
                "transcription": "kardum"
        },
        {
                "armenian": "պատրաստ",
                "translations": [
                        "готовый",
                        "подготовленный"
                ],
                "transcription": "patrast"
        },
        {
                "armenian": "իրական",
                "translations": [
                        "истинный",
                        "настоящий",
                        "правдивый"
                ],
                "transcription": "irakan"
        },
        {
                "armenian": "իսկապես",
                "translations": [
                        "действительно",
                        "правда"
                ],
                "transcription": "iskapes"
        },
        {
                "armenian": "պատճառ",
                "translations": [
                        "причина",
                        "основание",
                        "резон"
                ],
                "transcription": "patcharr"
        },
        {
                "armenian": "կարմիր",
                "translations": [
                        "красный",
                        "червонный",
                        "краснота"
                ],
                "transcription": "karmir"
        },
        {
                "armenian": "հանգստանալ",
                "translations": [
                        "отдыхать",
                        "отдохнуть",
                        "успокоиться"
                ],
                "transcription": "hangstanal"
        },
        {
                "armenian": "հիշիր",
                "translations": [
                        "помнить",
                        "вспоминать",
                        "вспомнить"
                ],
                "transcription": "hishir"
        },
        {
                "armenian": "կրկնել",
                "translations": [
                        "повторить",
                        "повторять"
                ],
                "transcription": "krknel"
        },
        {
                "armenian": "արդյունք",
                "translations": [
                        "результат"
                ],
                "transcription": "ardyunk’"
        },
        {
                "armenian": "վերադարձնել",
                "translations": [
                        "вернуть",
                        "возвращать",
                        "возвратить"
                ],
                "transcription": "veradardznel"
        },
        {
                "armenian": "բրինձ",
                "translations": [
                        "рис"
                ],
                "transcription": "brindz"
        },
        {
                "armenian": "հարուստ",
                "translations": [
                        "богатый",
                        "состоятельный",
                        "зажиточный"
                ],
                "transcription": "harust"
        },
        {
                "armenian": "սահել",
                "translations": [
                        "кататься"
                ],
                "transcription": "sahel"
        },
        {
                "armenian": "աջ",
                "translations": [
                        "право",
                        "направо"
                ],
                "transcription": "aj"
        },
        {
                "armenian": "գետ",
                "translations": [
                        "река",
                        "речка"
                ],
                "transcription": "get"
        },
        {
                "armenian": "ճանապարհ",
                "translations": [
                        "дорога",
                        "путь",
                        "способ"
                ],
                "transcription": "chanaparh"
        },
        {
                "armenian": "սենյակ",
                "translations": [
                        "комната",
                        "помещение",
                        "камера"
                ],
                "transcription": "senyak"
        },
        {
                "armenian": "առօրյա",
                "translations": [
                        "обычный",
                        "обыкновенный",
                        "простой",
                        "каждодневный"
                ],
                "transcription": "arrorya"
        },
        {
                "armenian": "կանոն",
                "translations": [
                        "правило",
                        "канон",
                        "закон"
                ],
                "transcription": "kanon"
        },
        {
                "armenian": "վազել",
                "translations": [
                        "бегать",
                        "бежать",
                        "побежать"
                ],
                "transcription": "vazel"
        },
        {
                "armenian": "տխուր",
                "translations": [
                        "грустный",
                        "печальный"
                ],
                "transcription": "tkhur"
        },
        {
                "armenian": "աղցան",
                "translations": [
                        "салат"
                ],
                "transcription": "aghts’an"
        },
        {
                "armenian": "աղ",
                "translations": [
                        "соль",
                        "поваренная соль"
                ],
                "transcription": "agh"
        },
        {
                "armenian": "նույնը",
                "translations": [
                        "самый",
                        "такой же",
                        "тот же"
                ],
                "transcription": "nuyny"
        },
        {
                "armenian": "Շաբաթ",
                "translations": [
                        "суббота",
                        "неделя"
                ],
                "transcription": "Shabat’"
        },
        {
                "armenian": "ասել",
                "translations": [
                        "сказать",
                        "говорить",
                        "поведать"
                ],
                "transcription": "asel"
        },
        {
                "armenian": "դպրոց",
                "translations": [
                        "школа",
                        "учение",
                        "училище"
                ],
                "transcription": "dprots’"
        },
        {
                "armenian": "գիտություն",
                "translations": [
                        "наука",
                        "знание",
                        "дисциплина"
                ],
                "transcription": "gitut’yun"
        },
        {
                "armenian": "գիտնական",
                "translations": [
                        "ученый",
                        "эрудит"
                ],
                "transcription": "gitnakan"
        },
        {
                "armenian": "ծով",
                "translations": [
                        "море"
                ],
                "transcription": "tsov"
        },
        {
                "armenian": "երկրորդ",
                "translations": [
                        "второй"
                ],
                "transcription": "yerkrord"
        },
        {
                "armenian": "հատված",
                "translations": [
                        "сегмент",
                        "отрывок",
                        "раздел"
                ],
                "transcription": "hatvats"
        },
        {
                "armenian": "տեսնել",
                "translations": [
                        "видеть",
                        "увидеть"
                ],
                "transcription": "tesnel"
        },
        {
                "armenian": "վաճառել",
                "translations": [
                        "продавать",
                        "продать"
                ],
                "transcription": "vacharrel"
        },
        {
                "armenian": "ուղարկել",
                "translations": [
                        "послать",
                        "посылать",
                        "отправить"
                ],
                "transcription": "ugharkel"
        },
        {
                "armenian": "նախադասություն",
                "translations": [
                        "предложение",
                        "фраза"
                ],
                "transcription": "nakhadasut’yun"
        },
        {
                "armenian": "Սեպտեմբեր",
                "translations": [
                        "сентябрь"
                ],
                "transcription": "September"
        },
        {
                "armenian": "յոթ",
                "translations": [
                        "семь",
                        "семеро"
                ],
                "transcription": "yot’"
        },
        {
                "armenian": "տասնյոթ",
                "translations": [
                        "семнадцать"
                ],
                "transcription": "tasnyot’"
        },
        {
                "armenian": "յոթանասուն",
                "translations": [
                        "семьдесят"
                ],
                "transcription": "yot’anasun"
        },
        {
                "armenian": "կիսվել",
                "translations": [
                        "делиться"
                ],
                "transcription": "kisvel"
        },
        {
                "armenian": "ոչխար",
                "translations": [
                        "овца"
                ],
                "transcription": "voch’khar"
        },
        {
                "armenian": "վերնաշապիկ",
                "translations": [
                        "рубашка",
                        "сорочка"
                ],
                "transcription": "vernashapik"
        },
        {
                "armenian": "խանութ",
                "translations": [
                        "магазин",
                        "лавка",
                        "бутик"
                ],
                "transcription": "khanut’"
        },
        {
                "armenian": "կարճ",
                "translations": [
                        "короткий",
                        "краткий"
                ],
                "transcription": "karch"
        },
        {
                "armenian": "ցուցադրել",
                "translations": [
                        "показать"
                ],
                "transcription": "ts’uts’adrel"
        },
        {
                "armenian": "ցնցուղ",
                "translations": [
                        "душ",
                        "лейка"
                ],
                "transcription": "ts’nts’ugh"
        },
        {
                "armenian": "ցավել",
                "translations": [
                        "болеть",
                        "хворать"
                ],
                "transcription": "ts’avel"
        },
        {
                "armenian": "նման",
                "translations": [
                        "похожий",
                        "подобный",
                        "подобно"
                ],
                "transcription": "nman"
        },
        {
                "armenian": "երգել",
                "translations": [
                        "петь",
                        "спеть"
                ],
                "transcription": "yergel"
        },
        {
                "armenian": "երգիչ",
                "translations": [
                        "певец",
                        "вокалист",
                        "вокалистка"
                ],
                "transcription": "yergich’"
        },
        {
                "armenian": "քույր",
                "translations": [
                        "сестра",
                        "медсестра",
                        "сиделка"
                ],
                "transcription": "k’uyr"
        },
        {
                "armenian": "նստել",
                "translations": [
                        "сидеть",
                        "сесть",
                        "садиться"
                ],
                "transcription": "nstel"
        },
        {
                "armenian": "իրավիճակը",
                "translations": [
                        "ситуация"
                ],
                "transcription": "iravichaky"
        },
        {
                "armenian": "վեց",
                "translations": [
                        "шесть",
                        "шестеро"
                ],
                "transcription": "vets’"
        },
        {
                "armenian": "տասնվեց",
                "translations": [
                        "шестнадцать"
                ],
                "transcription": "tasnvets’"
        },
        {
                "armenian": "վաթսուն",
                "translations": [
                        "шестьдесят"
                ],
                "transcription": "vat’sun"
        },
        {
                "armenian": "հմտություն",
                "translations": [
                        "умение",
                        "мастерство",
                        "навык"
                ],
                "transcription": "hmtut’yun"
        },
        {
                "armenian": "շրջազգեստ",
                "translations": [
                        "юбка"
                ],
                "transcription": "shrjazgest"
        },
        {
                "armenian": "քնել",
                "translations": [
                        "спать",
                        "поспать",
                        "проспать"
                ],
                "transcription": "k’nel"
        },
        {
                "armenian": "դանդաղ",
                "translations": [
                        "медленный",
                        "медленно"
                ],
                "transcription": "dandagh"
        },
        {
                "armenian": "փոքր",
                "translations": [
                        "маленький",
                        "малый",
                        "небольшой"
                ],
                "transcription": "p’vok’r"
        },
        {
                "armenian": "օձ",
                "translations": [
                        "змея",
                        "змеи",
                        "гад"
                ],
                "transcription": "odz"
        },
        {
                "armenian": "ձյուն",
                "translations": [
                        "снег"
                ],
                "transcription": "dzyun"
        },
        {
                "armenian": "այդպես",
                "translations": [
                        "поэтому",
                        "потому",
                        "следовательно"
                ],
                "transcription": "aydpes"
        },
        {
                "armenian": "ոմանք",
                "translations": [
                        "некоторый"
                ],
                "transcription": "vomank’"
        },
        {
                "armenian": "ինչ-որ մեկը",
                "translations": [
                        "некто"
                ],
                "transcription": "inch’-vor meky"
        },
        {
                "armenian": "ինչ-որ բան",
                "translations": [
                        "несколько",
                        "некоторые",
                        "какой-то",
                        "что-то",
                        "что-нибудь"
                ],
                "transcription": "inch’-vor ban"
        },
        {
                "armenian": "երբեմն",
                "translations": [
                        "изредка",
                        "иногда",
                        "временами"
                ],
                "transcription": "yerbemn"
        },
        {
                "armenian": "որդի",
                "translations": [
                        "сын"
                ],
                "transcription": "vordi"
        },
        {
                "armenian": "երգ",
                "translations": [
                        "песня",
                        "песнь"
                ],
                "transcription": "yerg"
        },
        {
                "armenian": "շուտով",
                "translations": [
                        "скоро",
                        "вскоре"
                ],
                "transcription": "shutov"
        },
        {
                "armenian": "ներողություն",
                "translations": [
                        "извинить",
                        "извините",
                        "простите меня",
                        "простите"
                ],
                "transcription": "neroghut’yun"
        },
        {
                "armenian": "ձայն",
                "translations": [
                        "звук",
                        "голос",
                        "голосование"
                ],
                "transcription": "dzayn"
        },
        {
                "armenian": "ապուր",
                "translations": [
                        "суп",
                        "похлебка"
                ],
                "transcription": "apur"
        },
        {
                "armenian": "հարավ",
                "translations": [
                        "юг"
                ],
                "transcription": "harav"
        },
        {
                "armenian": "տիեզերք",
                "translations": [
                        "космос",
                        "вселенная"
                ],
                "transcription": "tiyezerk’"
        },
        {
                "armenian": "հատուկ",
                "translations": [
                        "особый",
                        "особенный",
                        "специальный"
                ],
                "transcription": "hatuk"
        },
        {
                "armenian": "հեգել",
                "translations": [
                        "буква",
                        "произносить",
                        "произносить по буквам"
                ],
                "transcription": "hegel"
        },
        {
                "armenian": "ծախսել",
                "translations": [
                        "расходовать"
                ],
                "transcription": "tsakhsel"
        },
        {
                "armenian": "սպորտ",
                "translations": [
                        "спорт"
                ],
                "transcription": "sport"
        },
        {
                "armenian": "գարուն",
                "translations": [
                        "весна"
                ],
                "transcription": "garun"
        },
        {
                "armenian": "կանգնել",
                "translations": [
                        "стоять",
                        "встать",
                        "вставать"
                ],
                "transcription": "kangnel"
        },
        {
                "armenian": "աստղ",
                "translations": [
                        "звезда"
                ],
                "transcription": "astgh"
        },
        {
                "armenian": "հայտարարություն",
                "translations": [
                        "утверждение"
                ],
                "transcription": "haytararut’yun"
        },
        {
                "armenian": "կայան",
                "translations": [
                        "станция",
                        "вокзал",
                        "остановка"
                ],
                "transcription": "kayan"
        },
        {
                "armenian": "մնալ",
                "translations": [
                        "оставаться",
                        "остаться"
                ],
                "transcription": "mnal"
        },
        {
                "armenian": "դեռ",
                "translations": [
                        "еще",
                        "все еще",
                        "до сих пор"
                ],
                "transcription": "derr"
        },
        {
                "armenian": "կանգ առնել",
                "translations": [
                        "остановиться"
                ],
                "transcription": "kang arrnel"
        },
        {
                "armenian": "փողոց",
                "translations": [
                        "улица"
                ],
                "transcription": "p’voghots’"
        },
        {
                "armenian": "ուժեղ",
                "translations": [
                        "сильный",
                        "мощный",
                        "могучий"
                ],
                "transcription": "uzhegh"
        },
        {
                "armenian": "ուսանող",
                "translations": [
                        "студент",
                        "студентка",
                        "учащаяся"
                ],
                "transcription": "usanogh"
        },
        {
                "armenian": "ուսումնասիրություն",
                "translations": [
                        "исследование",
                        "исследования"
                ],
                "transcription": "usumnasirut’yun"
        },
        {
                "armenian": "ոճ",
                "translations": [
                        "манера",
                        "метод",
                        "способ"
                ],
                "transcription": "voch"
        },
        {
                "armenian": "առարկա",
                "translations": [
                        "объект",
                        "предмет",
                        "тема"
                ],
                "transcription": "arrarka"
        },
        {
                "armenian": "հաջողություն",
                "translations": [
                        "успех",
                        "до свидания",
                        "удача"
                ],
                "transcription": "hajoghut’yun"
        },
        {
                "armenian": "շաքար",
                "translations": [
                        "сахар"
                ],
                "transcription": "shak’ar"
        },
        {
                "armenian": "ամառ",
                "translations": [
                        "лето"
                ],
                "transcription": "amarr"
        },
        {
                "armenian": "արև",
                "translations": [
                        "солнце"
                ],
                "transcription": "arev"
        },
        {
                "armenian": "կիրակի",
                "translations": [
                        "воскресенье"
                ],
                "transcription": "kiraki"
        },
        {
                "armenian": "հաստատ",
                "translations": [
                        "уверенный"
                ],
                "transcription": "hastat"
        },
        {
                "armenian": "սվիտեր",
                "translations": [
                        "свитер",
                        "джемпер",
                        "кофта"
                ],
                "transcription": "sviter"
        },
        {
                "armenian": "լողալ",
                "translations": [
                        "плавать",
                        "плыть"
                ],
                "transcription": "loghal"
        },
        {
                "armenian": "լող",
                "translations": [
                        "плавание"
                ],
                "transcription": "logh"
        },
        {
                "armenian": "վերցնել",
                "translations": [
                        "брать",
                        "взять",
                        "захватить"
                ],
                "transcription": "verts’nel"
        },
        {
                "armenian": "խոսել",
                "translations": [
                        "говорить",
                        "разговаривать",
                        "беседовать"
                ],
                "transcription": "khosel"
        },
        {
                "armenian": "բարձրահասակ",
                "translations": [
                        "высокий",
                        "рослый"
                ],
                "transcription": "bardzrahasak"
        },
        {
                "armenian": "թեյ",
                "translations": [
                        "чай"
                ],
                "transcription": "t’ey"
        },
        {
                "armenian": "սովորեցնել",
                "translations": [
                        "учить",
                        "обучать",
                        "преподавать"
                ],
                "transcription": "sovorets’nel"
        },
        {
                "armenian": "ուսուցիչ",
                "translations": [
                        "учитель",
                        "преподаватель",
                        "учительница"
                ],
                "transcription": "usuts’ich’"
        },
        {
                "armenian": "թիմ",
                "translations": [
                        "команда",
                        "группа"
                ],
                "transcription": "t’im"
        },
        {
                "armenian": "դեռահաս",
                "translations": [
                        "подросток",
                        "юноша",
                        "девушка"
                ],
                "transcription": "derrahas"
        },
        {
                "armenian": "հեռուստատեսություն",
                "translations": [
                        "телевидение",
                        "тв"
                ],
                "transcription": "herrustatesut’yun"
        },
        {
                "armenian": "պատմել",
                "translations": [
                        "рассказать",
                        "рассказывать"
                ],
                "transcription": "patmel"
        },
        {
                "armenian": "տասը",
                "translations": [
                        "десять",
                        "десятка",
                        "десятеро"
                ],
                "transcription": "tasy"
        },
        {
                "armenian": "սարսափելի",
                "translations": [
                        "мерзкий",
                        "гнусный",
                        "отвратительный"
                ],
                "transcription": "sarsap’eli"
        },
        {
                "armenian": "քան",
                "translations": [
                        "чем",
                        "нежели"
                ],
                "transcription": "k’an"
        },
        {
                "armenian": "շնորհակալություն",
                "translations": [
                        "спасибо",
                        "благодарю",
                        "благодарить"
                ],
                "transcription": "shnorhakalut’yun"
        },
        {
                "armenian": "դա",
                "translations": [
                        "это",
                        "он",
                        "она"
                ],
                "transcription": "da"
        },
        {
                "armenian": "այն",
                "translations": [
                        "тот",
                        "та",
                        "то"
                ],
                "transcription": "ayn"
        },
        {
                "armenian": "թատրոն",
                "translations": [
                        "театр"
                ],
                "transcription": "t’atron"
        },
        {
                "armenian": "իրենց",
                "translations": [
                        "им",
                        "их",
                        "они"
                ],
                "transcription": "irents’"
        },
        {
                "armenian": "նրանց",
                "translations": [
                        "их"
                ],
                "transcription": "nrants’"
        },
        {
                "armenian": "ապա",
                "translations": [
                        "после",
                        "потом",
                        "затем"
                ],
                "transcription": "apa"
        },
        {
                "armenian": "այնտեղ",
                "translations": [
                        "там",
                        "туда"
                ],
                "transcription": "ayntegh"
        },
        {
                "armenian": "նրանք",
                "translations": [
                        "они"
                ],
                "transcription": "nrank’"
        },
        {
                "armenian": "բան",
                "translations": [
                        "вещь",
                        "предмет",
                        "нечто"
                ],
                "transcription": "ban"
        },
        {
                "armenian": "մտածել",
                "translations": [
                        "думать",
                        "мыслить",
                        "размышлять"
                ],
                "transcription": "mtatsel"
        },
        {
                "armenian": "երրորդ",
                "translations": [
                        "третий",
                        "треть",
                        "3-ий"
                ],
                "transcription": "yerrord"
        },
        {
                "armenian": "ծարավ",
                "translations": [
                        "жажда",
                        "жаждущий",
                        "хотеть пить"
                ],
                "transcription": "tsarav"
        },
        {
                "armenian": "տասներեք",
                "translations": [
                        "тринадцать"
                ],
                "transcription": "tasnerek’"
        },
        {
                "armenian": "երեսուն",
                "translations": [
                        "тридцать"
                ],
                "transcription": "yeresun"
        },
        {
                "armenian": "սա",
                "translations": [
                        "этот",
                        "эта",
                        "эти"
                ],
                "transcription": "sa"
        },
        {
                "armenian": "հազար",
                "translations": [
                        "тысяча",
                        "салат латук"
                ],
                "transcription": "hazar"
        },
        {
                "armenian": "երեք",
                "translations": [
                        "три",
                        "тройка",
                        "трое"
                ],
                "transcription": "yerek’"
        },
        {
                "armenian": "միջոցով",
                "translations": [
                        "через"
                ],
                "transcription": "mijots’ov"
        },
        {
                "armenian": "Հինգշաբթի",
                "translations": [
                        "четверг",
                        "пятница"
                ],
                "transcription": "Hingshabt’i"
        },
        {
                "armenian": "տոմս",
                "translations": [
                        "билет"
                ],
                "transcription": "toms"
        },
        {
                "armenian": "ժամանակ",
                "translations": [
                        "время",
                        "час"
                ],
                "transcription": "zhamanak"
        },
        {
                "armenian": "հոգնած",
                "translations": [
                        "устать"
                ],
                "transcription": "hognats"
        },
        {
                "armenian": "տիտղոս",
                "translations": [
                        "титул",
                        "звание"
                ],
                "transcription": "titghos"
        },
        {
                "armenian": "դեպի",
                "translations": [
                        "к",
                        "навстречу",
                        "для"
                ],
                "transcription": "depi"
        },
        {
                "armenian": "այսօր",
                "translations": [
                        "сегодня",
                        "сегодняшний день",
                        "теперь"
                ],
                "transcription": "aysor"
        },
        {
                "armenian": "միասին",
                "translations": [
                        "вместе",
                        "сообща",
                        "совместно"
                ],
                "transcription": "miasin"
        },
        {
                "armenian": "զուգարան",
                "translations": [
                        "туалет",
                        "уборная",
                        "унитаз"
                ],
                "transcription": "zugaran"
        },
        {
                "armenian": "լոլիկ",
                "translations": [
                        "помидор",
                        "томат"
                ],
                "transcription": "lolik"
        },
        {
                "armenian": "վաղը",
                "translations": [
                        "завтра"
                ],
                "transcription": "vaghy"
        },
        {
                "armenian": "նաև",
                "translations": [
                        "также",
                        "тоже",
                        "и"
                ],
                "transcription": "nayev"
        },
        {
                "armenian": "ատամ",
                "translations": [
                        "зуб"
                ],
                "transcription": "atam"
        },
        {
                "armenian": "թեմա",
                "translations": [
                        "тема",
                        "предмет"
                ],
                "transcription": "t’ema"
        },
        {
                "armenian": "զբոսաշրջիկ",
                "translations": [
                        "турист",
                        "путешественник"
                ],
                "transcription": "zbosashrjik"
        },
        {
                "armenian": "երթևեկություն",
                "translations": [
                        "движение",
                        "трафик"
                ],
                "transcription": "yert’evekut’yun"
        },
        {
                "armenian": "գնացք",
                "translations": [
                        "поезд",
                        "паровоз"
                ],
                "transcription": "gnats’k’"
        },
        {
                "armenian": "ծառ",
                "translations": [
                        "дерево",
                        "древо"
                ],
                "transcription": "tsarr"
        },
        {
                "armenian": "ուղևորություն",
                "translations": [
                        "путешествие",
                        "поездка"
                ],
                "transcription": "ughevorut’yun"
        },
        {
                "armenian": "տաբատ",
                "translations": [
                        "брюки",
                        "штаны"
                ],
                "transcription": "tabat"
        }
]

        Word.objects.all().delete()
        Word.objects.bulk_create(
            [
                Word(
                    armenian=w["armenian"],
                    translations=w["translations"],
                    transcription=w["transcription"],
                    level="A1",
                )
                for w in words
            ]
        )
        self.stdout.write(self.style.SUCCESS(f"Inserted {len(words)} words"))
