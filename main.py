import pandas as pd

from attribute import BehavioralAttribute
from game import Game
from simulator import Simulator


def main():
  
  q_num = 100
  simulators = []
  behavior = BehavioralAttribute(name='COVID19', shape='hexagon')
  player_num = 6
  players_with_behavior_num = 2
  # for player_num in range(3, 10):
  for inner_edges in range(player_num - 1, int((player_num * (player_num - 1)) / 2) + 1):
    for outer_edges in range(1, inner_edges):
      # for players_with_behavior_num in range(1, player_num):
      simulators.append(Simulator(
        red_player_num=player_num,
        red_group_connections=inner_edges,
        blue_player_num=player_num,
        blue_group_connections=inner_edges,
        outer_group_connections=outer_edges,
        players_with_behavior_num=players_with_behavior_num,
        q_num=q_num,
        behavior=behavior,
      ))
  
  results = []
  for index, simulator in enumerate(simulators):
    simulator_generator = simulator.random_combination_generator()
    for _ in range(100):
      game = Game(*next(simulator_generator))
      game()
      results.append(game.to_list())
    print(f'{1 + index}/{len(simulators)}')

    
  df = pd.DataFrame(results, columns=Game.columns)
  df.to_excel(f'results_{player_num}_{players_with_behavior_num}_{q_num}.xlsx')


if __name__ == '__main__':
    main()