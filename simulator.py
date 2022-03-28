import gmpy2
import numpy as np
from dataclasses import dataclass
from itertools import combinations, product

from attribute import BehavioralAttribute, Attribute
from player import Player

@dataclass
class Simulator:
  red_player_num: int
  red_group_connections: int
  blue_player_num: int
  blue_group_connections: int
  outer_group_connections: int
  players_with_behavior_num: int
  behavior: BehavioralAttribute
  q_num: int = 10
  
  def __post_init__(self):
    self._all_combination = self.generate_all_combination()
    self.counter = 0

  def __iter__(self):
    return self._all_combination

  def __next__(self):
    return next(self._all_combination)

  @staticmethod
  def create_players(number_of_players, attribute: Attribute):
    return [Player(f'{attribute.name}{index}', attribute) \
                for index in range(0, number_of_players)]
    
  @staticmethod
  def combo_to_set(combo) -> set:
    player_in_combo = set()
    for connection in combo:
      for player in connection:
        player_in_combo.add(player)
    return player_in_combo
  
  def generate_all_combination(self):

    # RED
    # (red1, red2, red3, ...redn)
    red_players = *(f'Red{number}' for number in range(self.red_player_num)),
    
    # generator((red1, red2), (red1, red3), ...(redn-1, redn))
    possible_red_connections = combinations(red_players, 2)

    # ({(red1, red2), (red1, red3)}, {(red2, red4), (red1, red3)}, ...{...})
    # This is needed for generating more outher connectios at the price of inner connections
    red_combinations = *(set(combo) for combo in combinations(possible_red_connections, self.red_group_connections)),      
    # ((red1, red2), (red1, red3), ...(redn-1, redn))
    red_players_with_behavior = tuple(combinations(red_players, self.players_with_behavior_num))

    # BLUE
    blue_players = *(f'Blue{number}' for number in range(self.blue_player_num)),
    # blue_players = self.create_players(self.blue_player_num, GroupAttribute(name='Blue', color='Blue'))
    possible_blue_connections = combinations(blue_players, 2)
    blue_combinations = *(set(combo) for combo in combinations(possible_blue_connections, self.blue_group_connections)),

    # Q
    possible_behaviors = list()
    for _q in np.linspace(0.1, 1.0, num=self.q_num):
      possible_behaviors.append(
          BehavioralAttribute(self.behavior.name, 
                              self.behavior.shape, 
                              round(_q, 2))
          )
    
    # OUTER CONNECTIONS
    outer_connection_combinations = combinations(
        product(red_players, blue_players), 
        self.outer_group_connections
        )

    for outer_combo in outer_connection_combinations:
      for red_combo in red_combinations:
        for blue_combo in blue_combinations:
          for infected_combo in red_players_with_behavior:
            for _behavior in possible_behaviors:
              self.counter += 1
              yield (red_combo, blue_combo, outer_combo, infected_combo, _behavior)
              # Variations of inner to outer connections exchange
              for modified_combo in self.generate_more_outer_connections(red_combo, blue_combo, outer_combo):
                self.counter += 1
                yield (*modified_combo, infected_combo, _behavior)

  def generate_more_outer_connections(self, red_combo, blue_combo, outer_combo):
    for red_connection in red_combo:
      new_red_combo = red_combo.difference({red_connection, })
      for blue_connection in blue_combo:
        new_combos = *product(red_connection, blue_connection),
        new_blue_combo = blue_combo.difference({blue_connection, })
        yield (new_red_combo,
               new_blue_combo,
               (*outer_combo, new_combos[0], new_combos[2]))
        yield (new_red_combo,
               new_blue_combo,
               (*outer_combo, new_combos[1], new_combos[3]))
        
  def explain_len(self, _print:bool = True, _return = False):
    red_combinations = gmpy2.comb(gmpy2.comb(self.red_player_num, 2), self.red_group_connections)
    red_players_with_behavior = gmpy2.comb(self.red_player_num, self.players_with_behavior_num)
    blue_combinations = gmpy2.comb(gmpy2.comb(self.blue_player_num, 2), self.blue_group_connections)
    networks_combinations = gmpy2.comb(self.red_player_num * self.blue_player_num, self.outer_group_connections)
    normal_connections_combinations = int(red_combinations * blue_combinations * networks_combinations * red_players_with_behavior * self.q_num)
    modified_connections_combinations = int(self.red_group_connections * self.blue_group_connections * 2)
    result = normal_connections_combinations + (normal_connections_combinations * modified_connections_combinations)

    if _print:
      print(f'''
      Q's: {self.q_num} {[round(_q, 2) for _q in np.linspace(0.1, 1.0, num=self.q_num)]}

      (Players nCr 2) = Inner Connections
      (Inner Connections nCr Group Connections) = Group Combination
      Red Players: {self.red_player_num}\tConnections: {self.red_group_connections}\tCombinations: {red_combinations}
      Blue Players: {self.blue_player_num}\tConnections: {self.blue_group_connections}\tCombinations: {blue_combinations}
      
      (Red Players nCr Players with Behavior) = Players with Behavior Combination
      Red Players with behavior: {self.players_with_behavior_num}\tCombinations: {red_players_with_behavior}
      
      (Red Players * Blue Players nCr Outer Group Connections) = Outer Group Combinations
      Total Players: {self.blue_player_num + self.red_player_num}\tConnections: {self.outer_group_connections}\tCombinations: {networks_combinations}

      Unmodified Combination = Red Group Combination * Blue Group Combination * Outer Group Combinations * Players with Behavior Combination * Qs
      {red_combinations} * {blue_combinations} * {networks_combinations} * {red_players_with_behavior} * {self.q_num}
      Unmodified Combination: {normal_connections_combinations:,}

      Red Group Connections * Blue Group Connections * 2 = Modified Combination
      Modified Combination: {modified_connections_combinations}
      Unmodified Combination + (Unmodified Combination * Modified Combination) = Total
      {normal_connections_combinations:,} + ({normal_connections_combinations:,} * {modified_connections_combinations})
      Total: {result:,}''')
    
    if _return:
      return result
    
  def __len__(self):
    return self.explain_len(_print=False, _return=True)