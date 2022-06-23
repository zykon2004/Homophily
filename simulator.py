import gmpy2
import numpy as np
from dataclasses import dataclass
from itertools import combinations, product
import random
import math

from attribute import BehavioralAttribute, Attribute
from player import Player
from game import Game


@dataclass
class Simulator:
    red_player: int
    red_group_connections: int
    blue_player: int
    blue_group_connections: int
    outer_group_connections: int
    players_with_behavior: int
    behavior: BehavioralAttribute
    q_num: int = 10

    # def __post_init__(self):
    #   self._all_combination = self.generate_all_combination()
    #   self.counter = 0

    # def __iter__(self):
    #   return self._all_combination

    # def __next__(self):
    #   return next(self._all_combination)

    # @staticmethod
    # def create_players(number_of_players, attribute: Attribute):
    #   return [Player(f'{attribute.name}{index}', attribute) \
    #               for index in range(0, number_of_players)]

    # @staticmethod
    # def combo_to_set(combo) -> set:
    #   player_in_combo = set()
    #   for connection in combo:
    #     for player in connection:
    #       player_in_combo.add(player)
    #   return player_in_combo

    # def random_samples_generator(self, number_of_samples):
    #   random_indexes = random.sample(range(0, len(self)), number_of_samples)
    #   random_indexes.sort()
    #   previous_index = 0
    #   for index in random_indexes:
    #     for _ in range(index - previous_index - 1):
    #       next(self)
    #     yield next(self)
    #     previous_index = index

    def random_combination_generator(self, pairs=False):
        """Generate random combintaion of inner group connections,
        outer group connections, q, and players with behevior based on initial values.

        If pairs is True will generate a pair of combinations:
        (combination based on initial values,
        combination based on modified initial values to have less homophily)"""
        # RED
        red_players = (*(f"Red{number}" for number in range(self.red_player)),)
        # possible_red_connections = combinations(red_players, 2)
        # red_combinations = *(combinations(possible_red_connections, self.red_group_connections)),
        red_players_with_behavior = (
            *(combinations(red_players, self.players_with_behavior)),
        )

        # BLUE
        blue_players = (*(f"Blue{number}" for number in range(self.blue_player)),)
        # possible_blue_connections = combinations(blue_players, 2)
        # blue_combinations = *(combinations(possible_blue_connections, self.blue_group_connections)),

        # Q
        possible_behaviors = []
        digits = int(math.log10(self.q_num))
        for _q in np.linspace(0, 1.0, num=self.q_num):
            possible_behaviors.append(
                BehavioralAttribute(
                    self.behavior.name, self.behavior.shape, round(_q, digits)
                )
            )
        # # OUTER CONNECTIONS
        # outer_connection_combinations = *(combinations(
        #     product(red_players, blue_players),
        #     self.outer_group_connections
        #     )),

        while True:
            random_red_combinations = self.generate_random_product(
                red_players, red_players, k=self.red_group_connections
            )
            random_blue_combinations = self.generate_random_product(
                blue_players, blue_players, k=self.blue_group_connections
            )
            random_outer_connections = self.generate_random_product(
                red_players, blue_players, k=self.outer_group_connections
            )
            random_red_players_with_behavior = random.choice(red_players_with_behavior)
            random_possible_behaviors = random.choice(possible_behaviors)

            normal_combination = (
                random_red_combinations,
                random_blue_combinations,
                random_outer_connections,
                random_red_players_with_behavior,
                random_possible_behaviors,
            )
            if pairs:
                less_homophily_combination = (
                    self.remove_random_items(random_red_combinations, k=1),
                    self.remove_random_items(random_blue_combinations, k=1),
                    self.generate_random_product(
                        red_players,
                        blue_players,
                        k=self.outer_group_connections + 2,
                        initial_result=random_outer_connections,
                    ),
                    random_red_players_with_behavior,
                    random_possible_behaviors,
                )
                yield (normal_combination, less_homophily_combination)
            else:
                yield normal_combination

    # def generate_all_combination(self):

    #   # RED
    #   red_players = *(f'Red{number}' for number in range(self.red_player)),
    #   possible_red_connections = combinations(red_players, 2)
    #   red_combinations = combinations(possible_red_connections, self.red_group_connections)
    #   red_players_with_behavior = combinations(red_players, self.players_with_behavior)

    #   # BLUE
    #   blue_players = *(f'Blue{number}' for number in range(self.blue_player)),
    #   possible_blue_connections = combinations(blue_players, 2)
    #   blue_combinations = combinations(possible_blue_connections, self.blue_group_connections)

    # # Q
    # possible_behaviors = []
    # digits = int(math.log10(self.q_num))
    # for _q in np.linspace(0, 1.0, num=self.q_num):
    #   possible_behaviors.append(
    #       BehavioralAttribute(self.behavior.name,
    #                           self.behavior.shape,
    #                           round(_q, digits))
    #       )

    # # OUTER CONNECTIONS
    # outer_connection_combinations = combinations(
    #     product(red_players, blue_players),
    #     self.outer_group_connections
    #     )

    #   for _aggregated_product in product(
    #     red_combinations,
    #     blue_combinations,
    #     outer_connection_combinations,
    #     red_players_with_behavior,
    #     possible_behaviors
    #     ):
    #     yield _aggregated_product
    #     self.counter += 1

    def explain_len(self, _print: bool = True, _return=False):
        red_combinations = gmpy2.comb(
            gmpy2.comb(self.red_player, 2), self.red_group_connections
        )
        red_players_with_behavior = gmpy2.comb(
            self.red_player, self.players_with_behavior
        )
        blue_combinations = gmpy2.comb(
            gmpy2.comb(self.blue_player, 2), self.blue_group_connections
        )
        networks_combinations = gmpy2.comb(
            self.red_player * self.blue_player, self.outer_group_connections
        )
        normal_connections_combinations = int(
            red_combinations
            * blue_combinations
            * networks_combinations
            * red_players_with_behavior
            * self.q_num
        )
        # modified_connections_combinations = int(self.red_group_connections * self.blue_group_connections * 2)
        result = normal_connections_combinations

        if _print:
            print(
                f"""
      Q's: {self.q_num}

      (Players nCr 2) = Inner Connections
      (Inner Connections nCr Group Connections) = Group Combination
      Red Players: {self.red_player}\tConnections: {self.red_group_connections}\tCombinations: {red_combinations}
      Blue Players: {self.blue_player}\tConnections: {self.blue_group_connections}\tCombinations: {blue_combinations}
      
      (Red Players nCr Players with Behavior) = Players with Behavior Combination
      Red Players with behavior: {self.players_with_behavior}\tCombinations: {red_players_with_behavior}
      
      (Red Players * Blue Players nCr Outer Group Connections) = Outer Group Combinations
      Total Players: {self.blue_player * self.red_player}\tConnections: {self.outer_group_connections}\tCombinations: {networks_combinations}

      Total Combination = Red Group Combination * Blue Group Combination * Outer Group Combinations * Players with Behavior Combination * Qs
      {red_combinations} * {blue_combinations} * {networks_combinations} * {red_players_with_behavior} * {self.q_num}
      Total Combination: {result:,}"""
            )

        if _return:
            return result

    def __len__(self):
        return self.explain_len(_print=False, _return=True)

    @staticmethod
    def generate_random_product(*iterables, initial_result: tuple = None, k: int = 1):
        """Return k-sized tuple of random elements from the given iterables."""
        if initial_result:
            result = set(initial_result)
        else:
            result = set()

        while len(result) < k:
            _result = {random.choice(elements) for elements in iterables}
            if len(_result) == len(iterables):
                result.add(tuple(_result))
        return tuple(result)

    @staticmethod
    def remove_random_items(items: tuple, k: int = 0) -> tuple:
        """Remove random k number of items from items"""
        items_to_remove = set()
        while len(items_to_remove) < k:
            items_to_remove.add(random.choice(items))
        return tuple(set(items).difference(items_to_remove))

    @staticmethod
    def generate_simulators(
        players: int,
        players_with_behavior: int,
        q_num: int,
        behavior: BehavioralAttribute,
    ):
        """Generate all possible simulators with different edges configurations
        Max inner edges: (players * (players - 1)) / 2
        Max outer edges: inner edges"""

        for inner_edges in range(players - 1, int((players * (players - 1)) / 2) + 1):
            for outer_edges in range(1, inner_edges):
                yield (
                    Simulator(
                        red_player=players,
                        red_group_connections=inner_edges,
                        blue_player=players,
                        blue_group_connections=inner_edges,
                        outer_group_connections=outer_edges,
                        players_with_behavior=players_with_behavior,
                        q_num=q_num,
                        behavior=behavior,
                    )
                )
