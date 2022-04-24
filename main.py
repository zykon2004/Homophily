from typing import Generator
from tqdm import tqdm
import pandas as pd

from attribute import BehavioralAttribute
from game import Game
from simulator import Simulator


def main():
  # Define the simulators
  players = 6
  players_with_behavior = 3
  q_num = 100
  behavior = BehavioralAttribute(name='COVID19', shape='hexagon')
  pairs=False
  number_of_samples=100
  
  simulators = Simulator.generate_simulators(
    players=players, 
    players_with_behavior=players_with_behavior,
    q_num=q_num, 
    behavior=behavior,
    )
  
  df = play_simulator(tuple(simulators), pairs=pairs, number_of_samples=number_of_samples)
  df.to_excel(f'generated/raw/results_{players}_{players_with_behavior}_{q_num}{"_pairs" if pairs else ""}.xlsx')


def play_simulator(simulators, 
                   pairs=False, 
                   number_of_samples=100) -> pd.DataFrame:
  '''Create samples of games based on simulators. 
  Play the games and return the results as a dataframe.
  
  pairs: if True will generate a pair of combinations:
  normal and less homophily'''
  
  results = []
  header = Game.columns
  if pairs:
    if 'propegration_difference' not in header:
      header.insert(-1, 'propegration_difference')

  for simulator in tqdm(simulators):
    simulator_generator = simulator.random_combination_generator(pairs=pairs)
    for _ in range(number_of_samples):
      if pairs:
        
        game, less_homophily_game = next(simulator_generator)
        
        game = Game(*game)
        game.play()
        
        less_homophily_game = Game(*less_homophily_game)
        less_homophily_game.play()
        
        propegration_difference = less_homophily_game.behavior_propagation - game.behavior_propagation
        game_result = game.to_list()
        game_result.insert(-1, propegration_difference)
        results.append(game_result)
      
      else:
        game = Game(*next(simulator_generator))
        game.play()
        results.append(game.to_list())
        
  return pd.DataFrame(results, columns=header)


if __name__ == '__main__':
    main()