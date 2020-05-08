def check_name_taken(game, games, name):
    name_taken = False
    for game_id in games:
        if name == games[game_id].player.name:
            name_taken = True
    return name_taken


def check_name_valid(name):
    return len(name) >= 2 and name.isalnum()
