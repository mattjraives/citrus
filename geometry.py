import numpy as np

def orientation(p1,p2,p3):
    '''Returns the orientation of 3 points in Carresian space.
    -1: Counterclockwise
     0: Co-linear
     1: Clockwise'''
    return np.sign(np.cross((p2-p1),(p2-p3)))

def does_intersect(seg1,seg2):
    '''Checks whether the two line segments intersect'''
    tri = [seg1 + p for p in seg2] + [seg2 + p for p in seg1]
    ort = [orientation[t] for t in tri]
    if (ort[0] is not ort[1]) and (ort[2] is not ort[3]):
        return 1
    elif sum([o is 0 for o in ort]) is 4: ## the segments are co-linear
        if max(0,min(seg1[1][0],seg2[1][0]) - max(seg1[0][0],seg2[0][0]))>0 and \
           max(0,min(seg1[1][1],seg2[1][1]) - max(seg1[0][1],seg2[0][1]))>0:
            return 1
    else:
        return 0
