import os
import openpyxl
import constants


def get_player_scores(episode_no: int, working_directory: str) -> list[tuple[str, str]]:
    """
    Read episode data from the Excel sheet in `working_directory` corresponding to `episode_no` and
    return a list of tuple in the format, ('player_name', 'score').

    The expected workbook format is
        Player names are on row 1
        Final scores are on row 20 for episode 1 and row 22 for subsequent episodes.

    :param episode_no: is the episode number for which to retrieve the player names and scores
    :param working_directory: is the directory containing the Excel workbook to read

    :Example:
    >>> get_player_scores(3, "C:/path/to/directory")
    [('Olivia', 8), ('Buffy', 10), ('Hermione', '9')]
    """

    workbook = openpyxl.load_workbook(
        get_workbook_filepath(working_directory), data_only=True, read_only=True
    )
    worksheet = workbook[constants.WORKBOOK_SHEET_NAME_PREFIX + str(episode_no)]

    names = get_row_data(worksheet, 1)
    final_scores = get_row_data(worksheet, 20 if episode_no == 1 else 22)

    player_scores = list(zip(names, final_scores))

    return player_scores


def get_workbook_filepath(working_directory: str) -> str:
    """Return the full path to the Excel workbook."""
    return os.path.join(working_directory, constants.WORKBOOK_FILE_NAME)


def get_row_data(worksheet: object, row_index: int) -> list:
    """
    Return a list of non-null values from a row in the worksheet.
    The first column is omitted as it is the label for the row.

    :param worksheet: is a openpyxl Worksheet object
    :param row_index: is the row of the `worksheet` to process

    :Example:
    >>> get_row_data(worksheet_object, 1)
    ['Olivia', 'Buffy', 'Hermione']
    """
    return [cell.value for cell in worksheet[row_index][1:] if cell.value is not None]
