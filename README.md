# Survivor Ranking

A Python tool that generates weekly Survivor fantasy pool rankings based on player scores stored in an Excel workbook.

The program calculates each player's current ranking and tracks movement compared to the previous episode, making it easy to see who is rising or falling in the fantasy standings.

## Features

- Reads Survivor fantasy pool results from an Excel workbook
- Calculates episode-by-episode player standings
- Calculates power rankings based on rank movement:
  - `+N` = moved up N positions
  - `-N` = moved down N positions
  - `+0` = unchanged
- Supports weekly episode updates
- Produces formatted console output

Example output:

```text
1. Buffy-28 (+0)
2. Olivia-25 (+1)
3. Hermione-22 (-1)
```

## Requirements

- Python 3.10+
- `openpyxl`

Install dependencies:

```bash
pip install openpyxl
```

## Project Structure

```text
survivor-ranking/
│
├── main.py              # Application entry point
├── rank.py              # Ranking and power ranking calculations
├── player.py            # Player data model
├── workbook.py          # Excel workbook parsing
├── pretty_print.py      # Ranking output formatting
├── constants.py         # Workbook configuration
├── .gitignore
└── README.md
```

## Setup

Clone the repository:

```bash
git clone https://github.com/omaoloni/survivor-ranking.git
cd survivor-ranking
```

Install dependencies:

```bash
pip install openpyxl
```

Place the Survivor fantasy results workbook in the project directory.

The expected workbook filename is:

```text
Fantasy-Tribe-Season-50-Copy.xlsx
```

## Excel Workbook Format

The workbook should contain one sheet per episode using the naming convention:

```text
Ep #1
Ep #2
Ep #3
...
```

Each episode sheet should contain player names and scores in the expected locations.

Example:

| Player | Score |
|---|---:|
| Buffy | 28 |
| Olivia | 25 |
| Hermione | 22 |

## Usage

Run the program:

```bash
python main.py
```

The application will generate the current power ranking using the configured episode and workbook.

To generate a ranking for a specific episode:

```python
main(episode_no, working_directory)
```

Example:

```python
main(3, "/path/to/workbook")
```

## How Power Rankings Are Calculated

The power ranking compares each player's current position against their previous episode position.

Formula:

```text
Power Ranking = Previous Rank - Current Rank
```

Examples:

| Previous Rank | Current Rank | Movement |
|---|---|---|
| 5 | 2 | +3 |
| 1 | 4 | -3 |
| 2 | 2 | +0 |

A positive value indicates improvement, while a negative value indicates a decline.

## Future Improvements

Potential enhancements:

- Add command-line arguments for episode selection
- Support configurable workbook formats, contestant count, etc.
- Improve handling of tied scores
- Export rankings to CSV or Excel
- Add automated tests for ranking calculations
