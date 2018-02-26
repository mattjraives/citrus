import numpy as np

def geom(points):
  if points:
    o = point(np.mean([p.x for p in points]),np.mean([p.y for p in points]))
    r = np.max([1,2*np.max([vector(p,o).len for p in points])])
  else:
    r = 1
    o = point(0,0)
  return o,r

def d_score(x,y,points,dnorm=1,**kwargs):
  xy = point(x,y)
  distances = [vector(xy,p).len for p in points]
  o,r = geom(points)
  distances.append(0.75*(r - vector(xy,o).len))
  if dnorm:
    return np.min(distances)/dnorm
  else:
    return 0

def a_score(x,y,new_edges,edges,anorm=np.pi,**kwargs):
  if not edges:
    anorm = 0
  if anorm:
    xy = point(x,y)
    new_edges = [vector(xy,e) for e in new_edges]
    angles = [ne.angle(e) for ne in new_edges for e in edges if ne.meets(e)]
    return np.min(angles)/anorm
  else:
    return 0

def i_score(x,y,new_edges,edges,inorm=-0.1,**kwargs):
  if not edges:
    inorm = 0
  if inorm:
    xy = point(x,y)
    new_edges = [vector(xy,e) for e in new_edges]
    crosses = [ne.crosses(e) for ne in new_edges for e in edges \
               if not ne.meets(e)]
    return np.sum(crosses)/inorm
  else:
    return 0

def total_score(x,y,new_edges,points,edges,**kwargs):
  d = d_score(x,y,points,**kwargs)
  a = a_score(x,y,new_edges,edges,**kwargs)
  i = i_score(x,y,new_edges,edges,**kwargs)
  return d+a+i

v_total_score = np.vectorize(total_score,excluded=[2,3,4])
