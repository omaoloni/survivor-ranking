class Player:
  def __init__(self, name, score, rank, power_rank):
    self.name = name
    self.score = score
    self.rank = rank
    self.power_rank = power_rank

  def __str__(self) -> str:
    return f"{self.rank}. {self.name}-{self.score} ({self.power_rank})\n"

  def __repr__(self) -> str:
    # TODO fix this overriding
    # return f'Player(\'{self.name}\', {self.score}, \'{self.rank}\', \'{self.power_rank}\')'
    return f"{self.rank}. {self.name}-{self.score} ({self.power_rank})\n"