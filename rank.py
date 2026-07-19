from player import Player


def get_sorted_player_list(
    players: list[tuple[str, str]], sort_descending: bool
) -> list[tuple[str, str]]:
    """
    Return a list of players sorted by score with flexibility on asc or desc order.

    :param players: is a list of tuple in the format, ('player_name', 'score')

    :Example:
    >>> get_sorted_player_list([('Olivia', 8), ('Buffy', 10), ('Hermione', '9')], True)
    [('Buffy', 10), ('Hermione', '9'), ('Olivia', 8)]
    """
    return sorted(players, key=lambda x: x[1], reverse=sort_descending)


def get_ranking(players: list[tuple[str, str]]) -> dict[str, str]:
    """
    Return a dict of {'player_name' : 'ranking'}

    :param players: is a list of tuple in the format, ('player_name', 'score')

    :Example:
    >>> get_ranking([('Olivia', 8), ('Buffy', 10), ('Hermione', '9')])
    {'Buffy': '1', 'Hermione': '2', 'Olivia': '3'}
    """
    sorted_players = get_sorted_player_list(players, True)

    player_rankings = {
        player[0]: rank for rank, player in enumerate(sorted_players, start=1)
    }

    return player_rankings


def get_power_ranking(
    existing_player_standings: dict[str, str],
    current_player_scores: list[tuple[str, str]],
) -> list[Player]:
    """
    Return a sorted list (desc) of `Players` based on their current score.
    Calculate their `power_ranking` as the difference between their standing in the previous episode and current episode.
    If `existing_player_standing` is None (i.e. current episode is 1) then power ranking value for all Players is 0.

    :param existing_player_standings: is a representation of the standings as of the previous episode
    :param current_player_scores: contains the updated scores for each player as of the current episode

    :Example:
    >>> get_power_ranking({'Buffy': '1', 'Hermione': '2', 'Olivia': '3'}, [('Olivia', 25), ('Buffy', 28), ('Hermione', '22')])
    [1. Buffy-28 (+0), 2. Olivia-25 (+1), 3. Hermione-22 (-1)]
    """
    current_player_scores_sorted = get_sorted_player_list(current_player_scores, True)

    players = []

    for rank, current_player in enumerate(current_player_scores_sorted, start=1):
        player_name = current_player[0]
        power_ranking = (
            0
            if existing_player_standings is None
            else existing_player_standings[player_name] - rank
        )

        power_ranking_str = (
            "+" + str(power_ranking) if power_ranking >= 0 else str(power_ranking)
        )

        player = Player(player_name, current_player[1], rank, power_ranking_str)
        players.append(player)

    return players
