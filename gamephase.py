from copy import deepcopy

from player import Player


class GamePhase:
  def __init__(self, players):
    self.players = players

  @property
  def edges(self):
    def generate_id(*args):
      return f'{max(*args)} -- {min(*args)}'
    
    connections = {}
    for player in self.players:
      for connection in player.connections:
        names = (player.name, connection.name)
        id = generate_id(names)
        connections[id] = {
          'id': id,
          'from': max(names),
          'to': min(names),
        }
    return list(connections.values())

  @property
  def nodes(self):
    return [player.to_dict() for player in self.players]

  def propergate_behavior(self):
    """Allow player's behavior to propergate to other players.

    Returns True if the behavior of any player changed, False otherwise.
    """
    is_modified = False
    # deepcopy is needed because otherwise the behavior 
    # would propergate to the whole group in 1 iteration
    modified_players = deepcopy(self.players)
    for original, _copy in zip(self.players, modified_players):
      result =  original.check_connections_behavior()
      if (result):
        _copy.behavior = result
        _copy.size = Player.default_size + 5
        is_modified = True
      else:
        _copy.size = _copy.default_size
    
    if is_modified:
      return modified_players
    return False