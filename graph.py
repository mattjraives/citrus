import numpy as np
from matplotlib import pyplot as plt

class Node:
  '''Node in a graph'''
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.edges = []
  def connect(self,p2):
    self.edges.append(Edge(self,p2))

class Edge:
  '''Edge in a graph'''
  def __init__(self,p1,p2):
    self.p1 = p1
    self.p2 = p2
    self.len = np.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

class Graph:
  '''Graph'''
  def __init__(self,ax):
    self.ax = ax
    self.points = []
    self.edges = []
  def add_point(self,p):
    self.points.append(p)
  def add_edge(self,e):
    self.edges.append(e)
  def draw_points(self,**kwargs):
    for p in points:
      ax.plot(p.x,p.y,ls="-",`**kwargs)
