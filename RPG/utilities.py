def check_player_name_taken(games, name):
    name_taken = False
    for game_id in games:
        if name == games[game_id].player.name:
            name_taken = True
    return name_taken


def check_spaceship_name_taken(games, name):
    name_taken = False
    for game_id in games:
        if name == games[game_id].spaceship.name:
            name_taken = True
    return name_taken


def check_name_valid(name):
    return len(name) >= 2 and name.isalnum()
