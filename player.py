class Player:
    """
    A participant in the fantasy pool.

    :param name: The name of the player
    :param score: The player's score
    :param rank: The player's overall rank in the pool
    :param power_rank: The player's power ranking (i.e. how many places they've shifted up
      or down in the overall ranking since last episode)
    """

    def __init__(self, name: str, score: str, rank: str, power_rank: str):
        self.name = name
        self.score = score
        self.rank = rank
        self.power_rank = power_rank

    def __str__(self) -> str:
        """
        Returns a "pretty" string representation of the Player
        """
        return f"{self.rank}. {self.name}-{self.score} ({self.power_rank})\n"

    def __repr__(self) -> str:
        """
        Returns a "pretty" string representation of the Player
        """
        # TODO fix this overriding
        # return f'Player(\'{self.name}\', {self.score}, \'{self.rank}\', \'{self.power_rank}\')'
        return f"{self.rank}. {self.name}-{self.score} ({self.power_rank})\n"
