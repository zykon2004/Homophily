from tqdm import tqdm
from pathlib import Path
import copy
import pandas as pd
from attribute import BehavioralAttribute

from game import Game
from simulator import Simulator


def load_simulator_to_df(
    players: int = 5,
    behavior: BehavioralAttribute = BehavioralAttribute(
        name="COVID19", shape="hexagon"
    ),
    players_with_behavior: int = 2,
    q_num: int = 100,
    pairs: bool = False,
    number_of_samples: int = 100,
    ignore_file_check: bool = False,
) -> pd.DataFrame:

    # Check if simulator was already generated
    folder_name = (
        "Homophily/generated/raw/" if Path("Homophily").exists() else "generated/raw/"
    )
    file_name = f'results_{players}_{players_with_behavior}_{q_num}{"_pairs" if pairs else ""}_{number_of_samples}.xlsx'
    full_file_path = Path(folder_name).joinpath(file_name)

    if full_file_path.exists() and not ignore_file_check:
        df = pd.read_excel(full_file_path)
        print(f"Loaded {str(full_file_path)}")

    else:
        simulators = Simulator.generate_simulators(
            players=players,
            players_with_behavior=players_with_behavior,
            q_num=q_num,
            behavior=behavior,
        )

        df = play_simulator(
            simulators, pairs=pairs, number_of_samples=number_of_samples
        )
        df.to_excel(full_file_path)
        print(f"\nGenerated {str(full_file_path)}")

    return df


def play_simulator(simulators, pairs=False, number_of_samples=100) -> pd.DataFrame:
    """Create samples of games based on simulators.
    Play the games and return the results as a dataframe.

    pairs: if True will generate a pair of combinations:
    normal and less homophily"""

    results = []
    header = copy.copy(Game.columns)
    if pairs:
        if "propegration_difference" not in header:
            header.insert(-1, "propegration_difference")
            header.append("pair_args")

    for simulator in tqdm(tuple(simulators)):
        simulator_generator = simulator.random_combination_generator(pairs=pairs)
        for _ in range(number_of_samples):
            if pairs:

                game, less_homophily_game = next(simulator_generator)

                game = Game(*game)
                game.play()

                less_homophily_game = Game(*less_homophily_game)
                less_homophily_game.play()

                propegration_difference = (
                    less_homophily_game.behavior_propagation - game.behavior_propagation
                )
                game_result = game.to_list()
                game_result.insert(-1, propegration_difference)
                game_result.append(str(less_homophily_game))
                results.append(game_result)

            else:
                game = Game(*next(simulator_generator))
                game.play()
                results.append(game.to_list())

    return pd.DataFrame(results, columns=header)
