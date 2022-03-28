from dataclasses import dataclass

@dataclass(frozen=True)
class Attribute():
  name: str = 'Neutral'
  shape: str = 'dot'

@dataclass(frozen=True)
class BehavioralAttribute(Attribute):
  # Lower is stronger, default is higher than 1 so it won't propergate
  q: float = 1.1  

@dataclass(frozen=True)
class GroupAttribute(Attribute):
  color: str = 'Red'