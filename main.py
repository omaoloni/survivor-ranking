import os

from workbook import get_player_scores
from rank import get_ranking, get_power_ranking


# TODO add README explaining the expected format of the Excel sheet
def main(episode_no: int, working_directory: str) -> None:
    """
    A script that generates an updated Survivor power ranking.
        1. Populate the current week's data into the Survivor Results Excel sheet (TBD)
        2. Read and compare the previous and current weeks' data to generate an updated power ranking

    :param episode_no: The episode for which to calculate the ranking
    :param working_directory: The directory where the Excel file is located
    """

    if episode_no is None or episode_no < 1 or episode_no > 13:
        raise TypeError(
            "'episode_no' must be a whole number between 1 and 13 (inclusive)"
        )

    curr_episode_player_scores = get_player_scores(episode_no, working_directory)
    # print("Current episode scores")
    # print(curr_episode_player_scores)

    prev_round_rankings = None
    if episode_no > 1:
        prev_episode_player_scores = get_player_scores(
            episode_no - 1, working_directory
        )
        # print("Prev episode scores")
        # print(prev_episode_player_scores)

        prev_round_rankings = get_ranking(prev_episode_player_scores)

    curr_round_power_rankings = get_power_ranking(
        prev_round_rankings, curr_episode_player_scores
    )

    print(curr_round_power_rankings)


if __name__ == "__main__":
    main(3, os.getcwd())
