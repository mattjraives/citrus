class Fruit:
  def __init__(self,name,parents):
    self.name = name
    self.parents = parents
    self.children = []
    self.family = []
    self.siblings = []
    self.node = None ## Link to node object in graph
  def find_children(self,basket): # basket is a list of Fruit objects
    for fruit in basket:
      if fruit.name is not self.name:
        if self.name in [parent.name for parent in fruit.parents]:
          self.children.append(fruit)
    self.family = self.parents + self.children
  def find_siblings(self,basket):
    for fruit in basket:
      if fruit.name is not self.name:
        if set(fruit.parents).is_disjoint(set(self.parents)):
          continue
        else:
          self.siblings.append(fruit)
