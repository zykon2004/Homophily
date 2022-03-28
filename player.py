from typing import ClassVar
from collections import Counter
from dataclasses import dataclass, field
from copy import deepcopy

from attribute import GroupAttribute, BehavioralAttribute


@dataclass
class Player:
  name: str
  group: GroupAttribute
  behavior: BehavioralAttribute = field(init=False)
  connections: set = field(default_factory=set)
  default_size: int = field(default=8, repr=False)
  RED_BEHAVIOR: ClassVar[GroupAttribute] = GroupAttribute(name='Red', color='Red')
  BLUE_BEHAVIOR: ClassVar[GroupAttribute] = GroupAttribute(name='Blue', color='Blue')

  def __post_init__(self):
    self.behavior = BehavioralAttribute(
        name=self.group.name, shape=self.group.shape
        )  # Just for initiation, will be changed later
    self.size = self.default_size

  
  def __hash__(self):
    return hash(self.name)

  def check_connections_behavior(self):
    """This is where the infection happens.

    Return: True if behavior changed.
    """
    behaviors = Counter()
    for connection in self.connections:
      behaviors[connection.behavior] += 1

    for behavior, count in behaviors.items():
      if behavior.q <= float(count / len(self.connections)) and self.behavior != behavior:
        return behavior
    
    return False

  def to_dict(self) -> dict:
    return {
        'id': self.name, 
        'label': self.name, 
        'color': self.group.color,
        'shape': self.behavior.shape,
        'size': self.size
    }

  def connect(self, other) -> bool:
    """Connect the players. This mutates both objects.
    Return True if succesful.
    """
    if self is other or other in self.connections:
      return False

    self.connections.add(other)
    other.connections.add(self)
    return True
  
  def disconnect(self, other) -> bool:
    """Disconnect the players. This mutates both objects.
    Return True if succesful.
    """
    if other not in self.connections:
      return False

    self.connections.remove(other)
    other.connections.remove(self)
    return True

  def __deepcopy__(self, memo):
    cls = self.__class__
    result = cls.__new__(cls)
    memo[id(self)] = result
    for k, v in self.__dict__.items():
        setattr(result, k, deepcopy(v, memo))
    return result
  
  def __repr__(self) -> str:
      return self.name
  
  @classmethod
  def create(cls, name:str):
    if 'red' in name.lower():
      return cls(name, cls.RED_BEHAVIOR)
    if 'blue' in name.lower():
      return cls(name, cls.BLUE_BEHAVIOR)