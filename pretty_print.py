from player import Player


def print_power_ranking(power_ranked_players: list[Player]) -> str:
    """
    Pretty print the list of Players.

    :param power_ranked_players: is a sorted list (desc) of Players based on their rank

    >>> pretty_print_power_ranking([1. Buffy-28 (+0), 2. Olivia-25 (+1), 3. Hermione-22 (-1)]))
    1. Buffy-28 (+0)
    2. Olivia-25 (+1)
    3. Hermione-22 (-1)
    """
    if power_ranked_players is None or len(power_ranked_players) == 0:
        print("No players to print.")

    for player in power_ranked_players:
        print(player)
