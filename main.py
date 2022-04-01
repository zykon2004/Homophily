import pandas as pd

from attribute import BehavioralAttribute
from game import Game
from simulator import Simulator


def main():
  
  PLAYERS_WITH_BEHAVIOR_NUM = 2
  PLAYERS_ON_EACH_GROUP = 5
  Q_NUM = 100
  simulators = (
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 10,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 10,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 10,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 10,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 10,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 10,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 9,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 9,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 9,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 9,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 8,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 8,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 8,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 8,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 7,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 7,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 7,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 7,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 6,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 6,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 6,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 6,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 5,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 5,
      outer_group_connections = 5,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 10,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 10,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 9,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 9,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 9,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 9,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 8,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 8,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 8,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 8,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 7,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 7,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 7,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 7,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 6,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 6,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 6,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 6,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 5,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 5,
      outer_group_connections = 4,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 5,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 5,
      outer_group_connections = 3,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
    ),
    Simulator(
      red_player_num = PLAYERS_ON_EACH_GROUP,
      red_group_connections = 5,
      blue_player_num = PLAYERS_ON_EACH_GROUP,
      blue_group_connections = 5,
      outer_group_connections = 2,
      players_with_behavior_num = PLAYERS_WITH_BEHAVIOR_NUM,
      behavior = BehavioralAttribute(name='COVID19', shape='hexagon'),
      q_num = Q_NUM
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

    
  df = pd.DataFrame(results, columns=Game.columns)
  df.to_excel('results_5_2_100.xlsx')


if __name__ == '__main__':
    main()