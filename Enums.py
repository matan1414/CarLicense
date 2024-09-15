import enum

class LastProductsIDs():
    Yad2 = 0
    AgoraCellular = 0
    AgoraCellularAccessories = 0
    AgoraElectricMisc = 0
    agoraFurnituresSaloon = 0
    AgoraFurnituresCabinets = 0

class LemesiraMainGroup(enum.IntEnum):
    General = 0
    PetahTikva = 2
    Ashdod = 4
    Yehud = 6
    BeerSheva = 8
    Eilat = 10
    Jerusalem = 18
    Haifa = 20
    Ariel = 22
    Modiin = 24
    TelAviv = 26
    Herzliya = 95
    Netanya = 97
    KfarSaba = 99
    RishonLezion = 109
    RamatHagolanGalil = 114


class URLs(enum.StrEnum):
    police_stolen_car = f'https://www.gov.il/apps/police/stolencar/'
    kones_online_cars = f'https://www.konesonline.co.il/locating/vehicles'



class AgoraURLs(enum.StrEnum):
    AgoraCellular = f'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=10015'
    AgoraCellularAccessories = f'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=10020'
    AgoraElectricMisc = f'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=10041'
    agoraFurnituresSaloon = f'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=20017'
    AgoraFurnituresCabinets = f'https://www.agora.co.il/toGet.asp?searchType=subCategory&dealType=1&iseek=20009'


class LemesiraURLs(enum.StrEnum):
    example = f'http://info.cern.ch/hypertext/WWW/TheProject.html'
    agora_main = f'https://www.agora.co.il/'
    lemesira_main = f'https://lemesira.co.il/'
    lemesira_electric = f'https://lemesira.co.il/ads-category/%d7%9e%d7%95%d7%a6%d7%a8%d7%99-%d7%97%d7%a9%d7%9e%d7%9c/'
    yad2_main = f'https://www.yad2.co.il/'
    yad2_market_main = f'https://market.yad2.co.il/'


class ChatsIds(enum.IntEnum):
    LemesiraTempGroup = -1002244922452
    LemesiraMainGroup = -1002153219780


class LemesiraTempGroupTopics(enum.IntEnum):
    General = 0
    Temp = 2


