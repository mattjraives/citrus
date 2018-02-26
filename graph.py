import numpy as np
from matplotlib import pyplot as plt

class Node:
  '''Node in a graph'''
  def __init__(self,x,y,label=None):
    self.x = x
    self.y = y
    self.xy = np.array([x,y])
    self.label=label
  def plot(self,ax,marker="H",color="red",ms="8",**kwargs):
    ax.plot(self.x,self.y,marker=marker,color=color,ms=ms,ls="",**kwargs)

class Edge:
  '''Edge in a graph'''
  def __init__(self,p,q,label=None):
    self.o = p
    self.d = q
    self.xy = p.xy - q.xy
    self.len = np.linalg.norm(self.xy)
    self.uv = self.xy/self.len
    self.label=label
  def plot(self,ax,color="red",ls=":",**kwargs):
    ax.plot([self.o.x,self.d.x],[self.o.y,self.d.y],color=color,ls=ls,**kwargs)
  def meets(self,v):
    if (v.o is self.o) or (v.d is self.d):
      d = 1
    elif (v.o is self.d) or (v.d is self.o):
      d = -1
    else:
      d = 0
    return d
  def angle(self,v):
    d = self.meets(v)
    return np.arccos(np.clip(d*np.tensordot(self.uv,v.uv,axes=(0,0)), -1.0, 1.0))
  def crosses(self,v,verbose=0):
    orientation = lambda p1,p2,p3: int(np.sign(np.cross((p2-p1),(p2-p3))))
    triangles = [(self.o,self.d,v.o),
                 (self.o,self.d,v.d),
                 (v.o,v.d,self.o),
                 (v.o,v.d,self.d)]
    ort = [orientation(*[t.xy for t in tri]) for tri in triangles]
    if (ort[0] != ort[1]) and (ort[2] != ort[3]):
      return 1
    elif not sum([abs(o) for o in ort]):
      if sorted([self.o.x,self.d.x])+sorted([v.o.x,v.d.x]) is not\
         sorted([self.o.x,self.d.x,v.o.x,v.d.x]) and \
         sorted([self.o.y,self.d.y])+sorted([v.o.y,v.d.y]) is not\
         sorted([self.o.y,self.d.y,v.o.y,v.d.y]):
        return 1
      else:
        return 0
    else:
      return 0

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
    for p in self.points:
      p.plot(**kwargs)
  def draw_edges(self,**kwargs):
    for e in self.edges:
      e.plot(**kwargs)
