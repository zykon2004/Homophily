from copy import deepcopy

from player import Player


class GamePhase:
  def __init__(self, players, deepcopy_players=False):
    if deepcopy_players:
      self.players = deepcopy(players)
    else:
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
    players_to_modify = set()
    
    for index, player in enumerate(self.players):
      behavior =  player.check_connections_behavior()
      if behavior:
        players_to_modify.add((index, behavior))
        is_modified = True
      else:
        player.size = player.default_size
        
    for index, behavior in players_to_modify:
      self.players[index].behavior = behavior
      self.players[index].size = Player.default_size + 5
      self.players[index].update_neigbours_about_behavior_change(behavior)
      
    if is_modified:
      return self.players
    return False