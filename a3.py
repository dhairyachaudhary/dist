"""
CSE101: Introduction to Programming
Assignment 3

Name        : Dhairya
Roll-no     : 2019035
"""



import math
import random
import sys



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)

    Returns:
        Euclidean distance between p1 and p2
    """
    return (math.sqrt(((p2[1]-p1[1])**2)+((p2[0]-p1[0])**2)))

def swap(i1,i2,lst):
    """Helper function for sorting an array"""
    temp=lst[i1]
    lst[i1]=lst[i2]
    lst[i2]=temp


def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        List of points sorted by X coordinate
    """
    pointer1=0
    while pointer1<len(points)-1:
        pointer2=pointer1+1
        a=pointer1
        while pointer2<len(points):
            if points[pointer1][0]>points[pointer2][0]:
                swap(pointer1,pointer2,points)
            a=a+1
            pointer2=pointer2+1
        pointer1=pointer1+1
    return points


def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        List of points sorted by Y coordinate
    """
    pointer1=0
    while pointer1<len(points)-1:
        pointer2=pointer1+1
        a=pointer1
        while pointer2<len(points):
            if points[pointer1][1]>points[pointer2][1]:
                swap(pointer1,pointer2,points)
            a=a+1
            pointer2=pointer2+1
        pointer1=pointer1+1
    return points



def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    distmin=sys.maxsize
    pointer1=0
    while pointer1<len(plane)-1:
        pointer2=pointer1+1
        while pointer2<len(plane):
            d=dist(plane[pointer1],plane[pointer2])
            if d<distmin:
                distmin=d
                x1=plane[pointer1]
                x2=plane[pointer2]
            pointer2=pointer2+1
        pointer1=pointer1+1
    return (distmin,x1,x2)


def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a
    given upper bound. This function is called by
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    sort_points_by_Y(points)
    pointer1=0
    while pointer1<len(points)-1:
        pointer2=pointer1+1
        while pointer2<len(points) and points[pointer2][1]-points[pointer1][1]<d:
            if dist(points[pointer1],points[pointer2])<d:
                d=dist(points[pointer1],points[pointer2])
                x1=pointer1
                x2=pointer2
            pointer2=pointer2+1
        pointer1=pointer1+1
    try:
        return (d,points[x1],points[x2])
    except:
        return -1


def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane.

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    if (len(points)==2):
        return (dist(points[0],points[1]),points[0],points[1]);

    mid=int((len(points)+1)/2)

    p1=points[:mid]
    p2=points[mid-1:]

    d1 = efficient_closest_pair_routine(p1)
    d2 = efficient_closest_pair_routine(p2)

    if (d1[0]<d2[0]):
        d=d1
    else:
        d=d2

    strip=[]
    a=0
    while a<len(points):
        if abs(points[mid][0]-points[a][0])<=d[0]:
            strip.append(points[a])
        a=a+1
    dstrip=(closest_pair_in_strip(strip,d[0]))
    if dstrip==-1:
        return d
    else:
        return dstrip

def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
        """
    sort_points_by_X(points)
    return efficient_closest_pair_routine(points)

def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """

    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10, 10)
    plane = generate_plane(plane_size, num_pts)
    print("Points:", plane)
    #For computing using Naive approach
    naive=(naive_closest_pair(plane))
    print("Closest Pair:",naive[1:])
    print("Distance:",naive[0])
    #For computing using efficient approach
    efficient=(efficient_closest_pair(plane))
    print("Closest Pair:",efficient[1:])
    print("Distance:",efficient[0])
