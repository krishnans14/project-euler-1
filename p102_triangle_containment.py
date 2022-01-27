"""
This script solves the Triangle Containment problem from the Project Euler:
https://projecteuler.net/problem=102
The script requires the accompanying p102_triangles.txt
"""

import numpy as np

print('starting to access the coordinates ...... \n')
# Getting the coordinates from the text file
triangle_coords = []
with open('p102_triangles.txt') as f:
    for line in f:
        data = line.split(sep=',')
        triangle_coords.append(list(map(int, data)))

"""
Solution approach 1:
My present idea is that the origin is present inside the triangle if the three
points are in either three different quadrants or in opposite quadrants.
This appears to require two steps, one is to find the quadrant where the given
points are in; second to see if they fall in one of these two categories. The
second category of opposite quadrant has in itself two cases (I-III, II-IV). Is
there any other way to do it ?
    > This approach is wrong and does not work
"""

"""
Solution Approach 2:
Find the area of triangle with origin as one of the vertices and two of the three
vertices of the given triangle. If the sum of these areas is equal to the area of
the original triangle, then we can say that the origin is inside the triangle
- Find area of triangle given three vertices
- Check whether a given point is inside a triangle

- Problems with this approach:
    - Perhaps it would have been easier not to introduce floats and screw up the comparison?
"""

def distance_between(x, y):
    return np.sqrt(np.sum(np.power(x-y,2)))

def area_of_triangle(x, y, z):
    """
    each input is a tuple/list with the x and y coordinates of the point
    Heron's formulat
    """
    a = distance_between(x,y)
    b = distance_between(x,z)
    c = distance_between(y,z)
    s = (a+b+c)/2.0
    area = np.sqrt(s*(s-a)*(s-b)*(s-c))
    return area

def check_if_inside(triangle_coord, P):
    """
    Check if P lies inside the triangle with coordinates triangle_coord
    """
    area_full = area_of_triangle(triangle_coord[0:2], triangle_coord[2:4], triangle_coord[4:6])
    area_small_1 = area_of_triangle(triangle_coord[0:2], triangle_coord[2:4], P)
    area_small_2 = area_of_triangle(triangle_coord[0:2], triangle_coord[4:6], P)
    area_small_3 = area_of_triangle(triangle_coord[2:4], triangle_coord[4:6], P)

    total_area_sub = area_small_1 + area_small_2 + area_small_3
    if(abs(area_full-total_area_sub) < 1e-4):
        return True
    else:
        return False

print('starting to count ...... \n')
count_of_tri = 0
for tr_coord in triangle_coords:
    if check_if_inside(np.array(tr_coord), np.array([0,0])):
        count_of_tri = count_of_tri+1

print(count_of_tri)
