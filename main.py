import pandas as pd

from attribute import BehavioralAttribute
from game import Game
from simulator import Simulator


def main():

  simulator = Simulator(
    red_player_num = 5,
    red_group_connections = 9,
    blue_player_num = 5,
    blue_group_connections = 9,
    outer_group_connections = 3,
    players_with_behavior_num = 2,
    behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
    q_num = 10
  )
  results = []

  for _ in range(30):
    game = Game(*next(simulator))
    game()
    results.append(game.to_list())

  df = pd.DataFrame(results, columns=Game.columns)
  print(df)

if __name__ == '__main__':
    main()