import pandas as pd

from attribute import BehavioralAttribute
from game import Game
from simulator import Simulator


def main():

  simulators = (
    Simulator(
      red_player_num = 5,
      red_group_connections = 10,
      blue_player_num = 5,
      blue_group_connections = 10,
      outer_group_connections = 3,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 9,
      blue_player_num = 5,
      blue_group_connections = 9,
      outer_group_connections = 5,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 9,
      blue_player_num = 5,
      blue_group_connections = 9,
      outer_group_connections = 3,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 8,
      blue_player_num = 5,
      blue_group_connections = 8,
      outer_group_connections = 5,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 8,
      blue_player_num = 5,
      blue_group_connections = 8,
      outer_group_connections = 3,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 7,
      blue_player_num = 5,
      blue_group_connections = 7,
      outer_group_connections = 5,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 7,
      blue_player_num = 5,
      blue_group_connections = 7,
      outer_group_connections = 3,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 6,
      blue_player_num = 5,
      blue_group_connections = 6,
      outer_group_connections = 5,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 6,
      blue_player_num = 5,
      blue_group_connections = 6,
      outer_group_connections = 3,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 5,
      blue_player_num = 5,
      blue_group_connections = 5,
      outer_group_connections = 5,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 10,
      blue_player_num = 5,
      blue_group_connections = 10,
      outer_group_connections = 2,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 9,
      blue_player_num = 5,
      blue_group_connections = 9,
      outer_group_connections = 4,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 9,
      blue_player_num = 5,
      blue_group_connections = 9,
      outer_group_connections = 2,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 8,
      blue_player_num = 5,
      blue_group_connections = 8,
      outer_group_connections = 4,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 8,
      blue_player_num = 5,
      blue_group_connections = 8,
      outer_group_connections = 2,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 7,
      blue_player_num = 5,
      blue_group_connections = 7,
      outer_group_connections = 4,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 7,
      blue_player_num = 5,
      blue_group_connections = 7,
      outer_group_connections = 2,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 6,
      blue_player_num = 5,
      blue_group_connections = 6,
      outer_group_connections = 4,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 6,
      blue_player_num = 5,
      blue_group_connections = 6,
      outer_group_connections = 2,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
    Simulator(
      red_player_num = 5,
      red_group_connections = 5,
      blue_player_num = 5,
      blue_group_connections = 5,
      outer_group_connections = 4,
      players_with_behavior_num = 2,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = 10
    ),
  )

  results = []
  for index, simulator in enumerate(simulators):
    simulator_generator = simulator.random_combination_generator()
    for _ in range(500):
      game = Game(*next(simulator_generator))
      game()
      results.append(game.to_list())
    print(f'{1 + index}/{len(simulators)}')
  # for s in simulator.random_samples_generator(number_of_samples=10):
  #   game = Game(*s)
  #   game()
  #   results.append(game.to_list())
    
  df = pd.DataFrame(results, columns=Game.columns)
  df.to_excel('results.xlsx')
  # simulator.explain_len()
  # for _ in range(30):
  #   game = Game(*next(simulator))
  #   game()
  #   results.append(game.to_list())

  # df = pd.DataFrame(results, columns=Game.columns)
  # simulator.explain_len()

if __name__ == '__main__':
    main()