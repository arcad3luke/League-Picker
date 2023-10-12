import random

# Dictionary of champions and their recommended item builds
champion_item_builds = {
    "Aatrox": ["Goredrinker", "Black Cleaver", "Sterak's Gage", "Guardian Angel", "Sterak's Gage", "Ravenous Hydra"],
    "Ahri": ["Everfrost", "Luden's Echo", "Zhonya's Hourglass", "Rabadon's Deathcap", "Void Staff", "Morellonomicon"],
    "Akali": ["Hextech Rocketbelt", "Lich Bane", "Zhonya's Hourglass", "Rabadon's Deathcap", "Void Staff", "Night Harvester"],
    "Alistar": ["Sunfire Aegis", "Zeke's Convergence", "Thornmail", "Gargoyle Stoneplate", "Dead Man's Plate", "Sterak's Gage"],
    "Amumu": ["Sunfire Aegis", 'Plated Steelcaps','demonic embrace','mecury\'s treads','abyssal mark','thornmail'],
    "Anivia": ['Sorcerer\'s shoes','rod of ages','Searaph\'s Embrace','Mejai\'s SoulStealer','Zhonya\'s Hourglass','Void Staff'],
    "Annie": ['Sorcerer\'s shoes','Liandry\'s Anguish','Shadowflame','Rabadon\'s Deathcap','Void Staff','Zhonya\'s Hourglass'],
    "Aphelios": ['Berseker\'s greaves','Galeforce','Bloodthirster','Infinity Edge','The Collector','Gurdian Angel'],
    "Ashe": ['Kraken Slayer','Berserker\'s Greaves','Lord Dominik\'s Regards','Infinity Edge','Phantom Dancer','Blade of the Ruined King'],
    "Aurelion Sol": ['Sorcerer\'s Shoes', 'Rod of Ages', 'Rylai\'s Crystal Scepter', 'Seraph\'s Embrace', 'Shadowflame', 'Rabadon\'s Deathcap'],
    "Azir": ['', '', '', '', '', ''],
    "Bard": ['', '', '', '', '', ''],
    "Blitzcrank": ['', '', '', '', '', ''],
    "Brand": ['', '', '', '', '', ''],
    "Braum": ['', '', '', '', '', ''],
    "Caitlyn": ['', '', '', '', '', ''],
    "Camille": ['', '', '', '', '', ''],
    "Cassiopeia": ['', '', '', '', '', ''],
    "Chogath": ['', '', '', '', '', ''],
    "Corki": ['', '', '', '', '', ''],
    "Darius": ['', '', '', '', '', ''],
    "Diana": ['', '', '', '', '', ''],
    "Draven": ['', '', '', '', '', ''],
    "DrMundo": ['', '', '', '', '', ''],
    "Ekko": ['', '', '', '', '', ''],
    "Elise": ['', '', '', '', '', ''],
    "Evelynn": ['', '', '', '', '', ''],
    "Ezreal": ['', '', '', '', '', ''],
    "Fiddlesticks": ['', '', '', '', '', ''],
    "Fiora": ['', '', '', '', '', ''],
    "Fizz": ['', '', '', '', '', ''],
    "Galio": ['', '', '', '', '', ''],
    "Gangplank": ['', '', '', '', '', ''],
    "Garen": ['', '', '', '', '', ''],
    "Gnar": ['', '', '', '', '', ''],
    "Gragas": ['', '', '', '', '', ''],
    "Graves": ['', '', '', '', '', ''],
    "Gwen": ['', '', '', '', '', ''],
    "Hecarim": ['', '', '', '', '', ''],
    "Heimerdinger": ['', '', '', '', '', ''],
    "Illaoi": ['', '', '', '', '', ''],
    "Irelia": ['', '', '', '', '', ''],
    "Ivern": ['', '', '', '', '', ''],
    "Janna": ['', '', '', '', '', ''],
    "JarvanIV": ['', '', '', '', '', ''],
    "Jax": ['', '', '', '', '', ''],
    "Jayce": ['', '', '', '', '', ''],
    "Jhin": ['', '', '', '', '', ''],
    "Jinx": ['', '', '', '', '', ''],
    "Kaisa": ['', '', '', '', '', ''],
    "Kalista": ['', '', '', '', '', ''],
    "Karma": ['', '', '', '', '', ''],
    "Karthus": ['', '', '', '', '', ''],
    "Kassadin": ['', '', '', '', '', ''],
    "Katarina": ['', '', '', '', '', ''],
    "Kayle": ['', '', '', '', '', ''],
    "Kayn": ['', '', '', '', '', ''],
    "Kennen": ['', '', '', '', '', ''],
    "Khazix": ['', '', '', '', '', ''],
    "Kindred": ['', '', '', '', '', ''],
    "Kled": ['', '', '', '', '', ''],
    "KogMaw": ['', '', '', '', '', ''],
    "Leblanc": ['', '', '', '', '', ''],
    "LeeSin": ['', '', '', '', '', ''],
    "Leona": ['', '', '', '', '', ''],
    "Lillia": ['', '', '', '', '', ''],
    "Lissandra": ['', '', '', '', '', ''],
    "Lucian": ['', '', '', '', '', ''],
    "Lulu": ['', '', '', '', '', ''],
    "Lux": ['', '', '', '', '', ''],
    "Malphite": ['', '', '', '', '', ''],
    "Malzahar": ['', '', '', '', '', ''],
    "Maokai": ['', '', '', '', '', ''],
    "MasterYi": ['', '', '', '', '', ''],
    "MissFortune": ['', '', '', '', '', ''],
    "Wukong": ['', '', '', '', '', ''],
    "Mordekaiser": ['', '', '', '', '', ''],
    "Morgana": ['', '', '', '', '', ''],
    "Nami": ['', '', '', '', '', ''],
    "Nasus": ['', '', '', '', '', ''],
    "Nautilus": ['', '', '', '', '', ''],
    "Neeko": ['', '', '', '', '', ''],
    "Nidalee": ['', '', '', '', '', ''],
    "Nocturne": ['', '', '', '', '', ''],
    "Nunu": ['', '', '', '', '', ''],
    "Olaf": ['', '', '', '', '', ''],
    "Orianna": ['', '', '', '', '', ''],
    "Ornn": ['', '', '', '', '', ''],
    "Pantheon": ['', '', '', '', '', ''],
    "Poppy": ['', '', '', '', '', ''],
    "Pyke": ['', '', '', '', '', ''],
    "Qiyana": ['', '', '', '', '', ''],
    "Quinn": ['', '', '', '', '', ''],
    "Rakan": ['', '', '', '', '', ''],
    "Rammus": ['', '', '', '', '', ''],
    "RekSai": ['', '', '', '', '', ''],
    "Rell": ['', '', '', '', '', ''],
    "Renekton": ['', '', '', '', '', ''],
    "Rengar": ['', '', '', '', '', ''],
    "Riven": ['', '', '', '', '', ''],
    "Rumble": ['', '', '', '', '', ''],
    "Ryze": ['', '', '', '', '', ''],
    "Samira": ['', '', '', '', '', ''],
    "Sejuani": ['', '', '', '', '', ''],
    "Senna": ['', '', '', '', '', ''],
    "Seraphine": ['', '', '', '', '', ''],
    "Sett": ['', '', '', '', '', ''],
    "Shaco": ['', '', '', '', '', ''],
    "Shen": ['', '', '', '', '', ''],
    "Shyvana": ['', '', '', '', '', ''],
    "Singed": ['', '', '', '', '', ''],
    "Sion": ['', '', '', '', '', ''],
    "Sivir": ['', '', '', '', '', ''],
    "Skarner": ['', '', '', '', '', ''],
    "Sona": ['', '', '', '', '', ''],
    "Soraka": ['', '', '', '', '', ''],
    "Swain": ['', '', '', '', '', ''],
    "Sylas": ['', '', '', '', '', ''],
    "Syndra": ['', '', '', '', '', ''],
    "TahmKench": ['', '', '', '', '', ''],
    "Taliyah": ['', '', '', '', '', ''],
    "Talon": ['', '', '', '', '', ''],
    "Taric": ['', '', '', '', '', ''],
    "Teemo": ['', '', '', '', '', ''],
    "Thresh": ['', '', '', '', '', ''],
    "Tristana": ['', '', '', '', '', ''],
    "Trundle": ['', '', '', '', '', ''],
    "Tryndamere": ['', '', '', '', '', ''],
    "TwistedFate": ['', '', '', '', '', ''],
    "Twitch": ['', '', '', '', '', ''],
    "Udyr": ['', '', '', '', '', ''],
    "Urgot": ['', '', '', '', '', ''],
    "Varus": ['', '', '', '', '', ''],
    "Vayne": ['', '', '', '', '', ''],
    "Veigar": ['', '', '', '', '', ''],
    "Velkoz": ['', '', '', '', '', ''],
    "Vi": ['', '', '', '', '', ''],
    "Viego": ['', '', '', '', '', ''],
    "Viktor": ['', '', '', '', '', ''],
    "Vladimir": ['', '', '', '', '', ''],
    "Volibear": ['', '', '', '', '', ''],
    "Warwick": ['', '', '', '', '', ''],
    "Xayah": ['', '', '', '', '', ''],
    "Xerath": ['', '', '', '', '', ''],
    "XinZhao": ['', '', '', '', '', ''],
    "Yasuo": ['', '', '', '', '', ''],
    "Yone": ['', '', '', '', '', ''],
    "Yorick": ['', '', '', '', '', ''],
    "Yuumi": ['', '', '', '', '', ''],
    "Zac": ['', '', '', '', '', ''],
    "Zed": ['', '', '', '', '', ''],
    "Ziggs": ['', '', '', '', '', ''],
    "Zilean": ['', '', '', '', '', ''],
    "Zoe": ['', '', '', '', '', ''],
    "Zyra": ['', '', '', '', '', '']
}

def pick_champion():
    champions = list(champion_item_builds.keys())
    return random.choice(champions)

def get_item_build(champion):
    return champion_item_builds[champion]

# Example usage
champion = pick_champion()
item_build = get_item_build(champion)

print("Champion: " + champion)
print("Item Build: " + ", ".join(item_build))
