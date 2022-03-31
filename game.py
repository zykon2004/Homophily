from collections import deque
from dataclasses import dataclass
from typing import ClassVar

from attribute import BehavioralAttribute
from gamephase import GamePhase
from player import Player
    
@dataclass
class Game:
  red_players_connections: int
  blue_players_connections: int
  outer_group_connections: int
  players_with_behavior: int
  behavior: BehavioralAttribute
  columns: ClassVar[list] = [
    'q', 
    'propagation', 
    'depth', 
    'is_blue_behavior_changed',
    'players_with_behavior', 
    'edge_degree', 
    'outer_edges', 
    'inner_edges', 
    'red_players',
    'blue_players',
    'args'
  ]

  def __post_init__(self):
    self.players = {}
    self.create_connections(self.red_players_connections)
    self.create_connections(self.blue_players_connections)
    self.create_connections(self.outer_group_connections)
    self.introduce_behavior(self.players_with_behavior, self.behavior)
    self.phases = deque()
    self.phases.append(GamePhase(list(self.players.values())))
    pass
  
  def create_connections(self, player_connections):
    for players in player_connections:
      for player in players:
        if player not in self.players:
          self.players[player] = Player.create(player)
      
      p1, p2 = players
      self.players[p1].connect(self.players[p2])

  def introduce_behavior(self, 
                         players_with_behavior, 
                         behavior:BehavioralAttribute) -> None:
    
    for player in players_with_behavior:
      self.players[player].behavior = behavior
      self.players[player].size = Player.default_size + 5

  @property
  def depth(self):
    return len(self.phases)

  def __getitem__(self, index):
    return self.phases[index]
  
  @property
  def behavior_propagation(self):
    players_with_behavior = sum((1 for player in self.phases[-1].players if player.behavior == self.behavior))
    return round(float(players_with_behavior) * 100 / len(self.phases[-1].players), 3)

  @property
  def is_blue_behavior_changed(self):
    for player in self.phases[-1].players.values():
      if all((player.group == Player.BLUE_BEHAVIOR ,
             player.behavior == self.behavior)):
        return True
    return False
  
  @property
  def connections_mean(self):
    return float(sum(len(player.connections) for player in self.players.values()))/len(self.players)

  def __call__(self):
    modified_players = self.phases[-1].propergate_behavior()
    while(modified_players):
        self.phases.append(GamePhase(modified_players))
        modified_players = self.phases[-1].propergate_behavior()
  
  def to_list(self):
      return [
        self.behavior.q,
        self.behavior_propagation,
        self.depth,
        self.is_blue_behavior_changed,  
        len(self.players_with_behavior),
        self.connections_mean,
        len(self.outer_group_connections),
        (len(self.red_players_connections) + len(self.blue_players_connections)) / 2,
        len([player for player in self.players.values() if player.group.name == 'Red']),
        len([player for player in self.players.values() if player.group.name == 'Blue']),
        repr(self)
      ]