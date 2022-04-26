from attribute import BehavioralAttribute
from simulator import Simulator
from tools import play_simulator


def main():
  # Define the simulators
  players = 6
  players_with_behavior = 3
  q_num = 100
  behavior = BehavioralAttribute(name='COVID19', shape='hexagon')
  pairs=True
  number_of_samples=100
  simulators = Simulator.generate_simulators(
    players=players, 
    players_with_behavior=players_with_behavior,
    q_num=q_num, 
    behavior=behavior, 
    )
  
  df = play_simulator(tuple(simulators), pairs=pairs, number_of_samples=number_of_samples)
  df.to_excel(f'generated/raw/results_{players}_{players_with_behavior}_{q_num}{"_pairs" if pairs else ""}_{number_of_samples}.xlsx')


if __name__ == '__main__':
    main()