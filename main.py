from attribute import BehavioralAttribute
from tools import load_simulator_to_df


def main():
  # Define the simulators
  players = 6
  behavior = BehavioralAttribute(name='COVID19', shape='hexagon')
  players_with_behavior = 3
  q_num = 100
  pairs = True
  number_of_samples = 100
  ignore_file_check = True
  
  df = load_simulator_to_df(
    players = players, 
    behavior = behavior,
    players_with_behavior = players_with_behavior, 
    q_num = q_num, 
    pairs = pairs, 
    number_of_samples = number_of_samples, 
    ignore_file_check = ignore_file_check
    )


if __name__ == '__main__':
    main()