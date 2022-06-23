from attribute import BehavioralAttribute
import simulator
from tools import load_simulator_to_df, play_simulator
from simulator import Simulator


def main():
    # Define the simulators
    players = 5
    behavior = BehavioralAttribute(name="COVID19", shape="hexagon")
    players_with_behavior = 2
    q_num = 1000
    pairs = True
    number_of_samples = 500
    ignore_file_check = True
    # simulators = (
    #   Simulator(red_player=players,
    #             blue_player=players,
    #             players_with_behavior=players_with_behavior,
    #             red_group_connections = 12,
    #             blue_group_connections = 12,
    #             outer_group_connections = 3,
    #             q_num=q_num,
    #             behavior=behavior),
    #   Simulator(red_player=players,
    #             blue_player=players,
    #             players_with_behavior=players_with_behavior,
    #             red_group_connections = 12,
    #             blue_group_connections = 12,
    #             outer_group_connections = 4,
    #             q_num=q_num,
    #             behavior=behavior),

    #   )

    # print(play_simulator(simulators, pairs=pairs, number_of_samples=number_of_samples))
    df = load_simulator_to_df(
        players=players,
        behavior=behavior,
        players_with_behavior=players_with_behavior,
        q_num=q_num,
        pairs=pairs,
        number_of_samples=number_of_samples,
        ignore_file_check=ignore_file_check,
    )


if __name__ == "__main__":
    main()
