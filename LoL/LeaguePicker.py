import random
import time as t
import champ as champ

champions = {
    'top': ['Aatrox', 'Camille', 'Cho\'Gath', 'Darius', 'Dr. Mundo', 'Fiora', 'Garen', 'Gnar', 'Gwen', 'Illaoi', 'Irelia', 'Jayce', 'Kayle', 'Kennen', 'Kled', 'K\'Sante', 'Malphite', 'Mordekaiser', 'Nasus', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Riven', 'Rumble', 'Sett', 'Shen', 'Singed', 'Sion', 'Takhm Kench', 'Teemo'],
    'mid': ['Ahri', 'Akali', 'Aksham', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Cassiopeia', 'Corki', 'Diana', 'Fizz', 'Galio', 'Kassadin', 'Katarina', 'Kayle', 'LeBlanc', 'Lissandra', 'Lux', 'Malzahar', 'Neeko', 'Orianna', 'Qiyana', 'Ryze', 'Samira', 'Syndra', 'Sylas', 'Tallyah', 'Talon'],
    'bot': ['Apelios', 'Caitlin', 'Draven', 'Ezreal', 'Jhin', 'Jinx', 'Kai\'Sa', 'Kastra', 'Kog\'Maw', 'Lucian', 'Miss Fortune', 'Nilah', 'Samira', 'Sivir'],
    'support': ['Astrar', 'Ashe', 'Bard', 'Blitzcrank', 'Brand', 'Braum', 'Heimerdinger', 'Janna', 'Karma', 'Leona', 'Lulu', 'Lux', 'Maokai', 'Milio', 'Morgana', 'Nami', 'Nautilus', 'Pyke', 'Rakan', 'Rell', 'Renata Glasc', 'Senna', 'Seraphine', 'Sona', 'Soraka', 'Swain', 'Taric'],
    'jungle': ['Amumu', 'Bel\'Veth', 'Diana', 'Ekko', 'Elise', 'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan IV', 'Kayn', 'Kha\'Zix', 'Kindred', 'Lee Sin', 'Lillia', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Rammus', 'Rek\'Sai', 'Sejuani', 'Shaco', 'Shyvana', 'Skarner', 'Sylas'],
}

role = {
    'assassin': ['Ahri', 'Akali', 'Akhsan', 'Ekko', 'Evelynn', 'Fiora', 'Fizz', 'Gwen', 'Irelia', 'Jax', 'Kassadin', 'Katarina', 'Kayn', 'Kha\'Zix', 'LeBlanc', 'Lee Sin', 'Malzahar', 'Master Yi', 'Nidalee', 'Nilah', 'Nocturne', 'Pantheon', 'Pyke', 'Qiyana', 'Quinn', 'Rengar', 'Riven', 'Shaco', 'Sylas', 'Talon', 'Teemo', 'Tristana', 'Tryndamere', 'Twitch', 'Vayne', 'Vi', 'Viego', 'Xin Zhao', 'Yasuo', 'Yone', 'Zed'],
    'fighter': ['Aatrox', 'Bel\'Veth', 'Blitzcrank', 'Camille', 'Darius', 'Diana', 'Dr. Mundo', 'Ekko', 'Elise', 'Fiora', 'Fizz', 'Gangplank', 'Garen', 'Gnar', 'Gragas', 'Gwen', 'Hecarim', 'Illaoi', 'Irelia', 'Jarvan IV', 'Jax', 'Jayce', 'Kayle', 'Kayn', 'Kled', 'K\'Sante', 'Lee Sin', 'Lillia', 'Malphite', 'Master Yi', 'Mordekaiser', 'Nasus', 'Nilah', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Ornn', 'Panetheon', 'Poppy', 'Qiyana', 'Rammus', 'Rek\'Sai', 'Renekton', 'Rengar', 'Riven', 'Rumble', 'Ryze', 'Sejuani', 'Sett', 'Shyvana', 'Singed', 'Sion', 'Skarner', 'Swain', 'Taric', 'Thresh', 'Trundle', 'Tryndamere', 'Udyr', 'Urgot', 'Vi', 'Viego', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Yasuo', 'Yone', 'Yorick', 'Zac'],
    'mage': ['Ahri', 'Amumu', 'Anivia', 'Annie', 'Aurelion Sol', 'Azir', 'Bard', 'Brand', 'Cassopeia', 'Cho\'Gath', 'Diana', 'Elise', 'Evelynn', 'Ezreal', 'Fiddlesticks', 'Galio', 'Gragas', 'Heimerdinger', 'Ivern', 'Janna', 'Jhin', 'Karma', 'Karthus', 'Kassadin', 'Katarina', 'Kennen', 'Kog\'Maw', 'LeBlanc', 'Lillia', 'Lissandra', 'Lulu', 'Lux', 'Malzahar', 'Maokai', 'Morgana', 'Nami', 'Neeko', 'Nidalee', 'Orianna', 'Renata Glasc', 'Rumble', 'Ryze', 'Seraphine', 'Sona', 'Soraka', 'Swain', 'Sylas', 'Syndra', 'Tallyah', 'Twisted Fate', 'Varus', 'Veigar', 'Vel\'Koz', 'Vex', 'Viktor', 'Vladimir', 'Xerath', 'Yuumi', 'Ziggs', 'Zilean', 'Zoe', 'Zyra'],
    'marksman': ['Akshan', 'Aphelios', 'Ashe', 'Azir', 'Caitlin', 'Corki', 'Draven', 'Ezreal', 'Graves', 'Jayce', 'Jhin', 'Jinx', 'Kai\'Sa', 'Kastra', 'Kennen', 'Kindred', 'Kog\'Maw', 'Lucian', 'Miss Fortune', 'Quinn', 'Samira', 'Senna', 'Sivir', 'Teemo', 'Tristana', 'Twitch', 'Varus', 'Vayne', 'Xayah', 'Zeri'],
    'support': ['Astrar', 'Anivia', 'Ashe', 'Bard', 'Braum', 'Fiddlesticks', 'Heimerdinger', 'Ivern', 'Janna', 'Karma', 'Kayle', 'Leona', 'Lulu', 'Lux', 'Milio', 'Morgana', 'Nami', 'Nautilus', 'Neeko', 'Orianna', 'Pyke', 'Rakan', 'Rell', 'Renata Glasc', 'Senna', 'Seraphine', 'Sona', 'Soraka', 'Tahm Kench', 'Tallyah', 'Taric', 'Thresh', 'Yuumi', 'Zilean', 'Zoe', 'Zyra'],
    'tank': ['Aatrox', 'Astrar', 'Amumu', 'Blitzcrank', 'Braum', 'Camille', 'Cho\'Gath', 'Darius', 'Dr. Mundo', 'Galio', 'Garen', 'Gnar', 'Hecarim', 'Illaoi', 'Jarvan IV', 'Kled', 'K\'Sante', 'Leona', 'Malphite', 'Maokai', 'Nasus', 'Nautilus', 'Nunu & Willump', 'Olaf', 'Ornn', 'Poppy', 'Rammus', 'Rell', 'Renekton', 'Sejuani', 'Sett', 'Shen', 'Shyvana', 'Singed', 'Sion', 'Skarner', 'Tahm Kench', 'Trundle', 'Udyr', 'Urgot', 'Volibear', 'Warwick', 'Wukong', 'Yorick', 'Zac']
}


def champ_picker(build, champion):

    # Pick a Lane
    lane = input(
        'What lane do you want to play? (top, mid, bot, jungle, support) \n')
    match lane:
        case 'top':
            lane_choose = random.choices(champions['top'])
            return lane_choose
        case 'bot':
            lane_choose = random.choices(champions['bot'])
            return lane_choose
        case 'mid':
            lane_choose = random.choices(champions['mid'])
            return lane_choose
        case 'support':
            lane_choose = random.choices(champions['support'])
            return lane_choose
        case 'jungle':
            lane_choose = random.choices(champions['jungle'])
            return lane_choose

    # Pick a role to try and fine tune choice or give another option
    pick_role = input(
        f'What role do you want to play? (assassin, fighter, mage, marksman, support, tank)\n')
    n = [pick_role, lane]
    match pick_role:
        
        case 'assassin':
            role_choose = random.choices(role['assassin'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)
        case 'fighter':
            role_choose = random.choices(role['fighter'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)
        case 'mage':
            role_choose = random.choices(role['mage'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)
        case 'marksman':
            role_choose = random.choices(role['marksman'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)
        case 'support':
            role_choose = random.choices(role['support'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)
        case 'tank':
            role_choose = random.choices(role['tank'])
            if role_choose == lane:
                return role_choose
            else:
                return random.choices(n)

    build = champ.get_item_build(champion=champion)
    print(f'lane: {lane}, champion: {champion}, build: {build}')
    t.sleep(5)

champ_picker()
