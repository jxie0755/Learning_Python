# This is from CS61a project maps
# k-means is used to calculate the centroids of a group of coordinates
# reference: http://tech.nitoyon.com/en/blog/2013/11/07/k-means/


# If given a list of coordinates, and k number of centroids, how to find out the coordinates of the centorids?
import random
from math import sqrt

def distance(coor1, coor2):
    """Returns the Euclidean distance between pos1 and pos2, which are pairs."""
    return sqrt((coor1[0] - coor2[0]) ** 2 + (coor1[1] - coor2[1]) ** 2)

def mean(s):
    """Returns the arithmetic mean of a sequence of numbers s."""
    assert len(s) > 0
    return sum(s) / len(s)

def coordinate_gen(raw_coordinates, k):
    """randomly generate k number of coordinates"""
    low_x, high_x = min(coor[0] for coor in raw_coordinates), max(coor[0] for coor in raw_coordinates)
    low_y, high_y = min(coor[1] for coor in raw_coordinates), max(coor[1] for coor in raw_coordinates)
    coors = []
    for i in range(k):
        while True:
            coor = [random.randrange(low_x, high_x), random.randrange(low_y, high_y)]
            if coor not in coors:
                break
            else:
                continue
        coors.append(coor)
    return coors

def find_closest(coordinate, centroids):
    """Return the centroid in centroids that is closest to location."""
    return min(centroids, key=lambda x: distance(coordinate, x))

def group_by_first(pairs):
    """Return a list of pairs that relates each unique key in the [key, value]
    pairs to a list of all values that appear paired with that key.

    pairs: a sequence of pairs
    """
    keys = []
    for key, _ in pairs:
        if key not in keys:
            keys.append(key)
    return [[y for x, y in pairs if x == key] for key in keys]

def group_by_centroid(raw_coordinates, centroids):
    """Return a list of clusters, where each cluster contains all coordinates nearest to a corresponding centroid in centroids.
    """
    centroid_pairs = []
    for coordinate in raw_coordinates:
        pair = [find_closest(coordinate, centroids), coordinate]
        centroid_pairs.append(pair)
    return group_by_first(centroid_pairs)

def find_centroid(cluster):
    """Return the centroid of the locations of the restaurants in cluster."""
    latitudes, longitudes = [], []
    for coordinate in cluster:
        latitudes.append(coordinate[0])
        longitudes.append(coordinate[1])
    return [mean(latitudes), mean(longitudes)]

def k_mean(raw_coordinates, k, max_learn=10):
    """return a list (K_list), to group the coordinates into k cluster,
    so that each coordinate is bond to one centroid.

    K_list: a list of pairs, first element is the centroid coordinate, second element is a list of coordinates that is grouped to this centroid.

    raw_coordinates: a list of coordinates as the raw data

    k: number of centroids

    max_learn: number of repeatingly calibration
    """
    assert len(raw_coordinates) >= k, 'Not enough coordinates to cluster'
    old_centroids, n = [], 0

    # Select initial centroids randomly by choosing k different coordinates
    centroids = coordinate_gen(raw_coordinates, k)
    # centroids = [[-5.5, 5.5], [4.5, 4.5], [-18, -20], [3, -5]]  # this will guarantee to work

    while n < max_learn:
        old_centroids = centroids
        clusters = group_by_centroid(raw_coordinates, centroids)
        centroids = [find_centroid(cluster) for cluster in clusters]
        n += 1

    return zip(centroids, clusters)


# Additional verification method
def total_distance(centroid, clusters):
    t_distance = 0
    for i in clusters:
        t_distance += distance(centroid, i)
    return t_distance


if __name__ == '__main__':
    # generate raw data from 4 areas
    area_1 = [[-6, 6], [-4, 6], [-6, 4], [-4, 4]]  # center [-5, 5]
    area_2 = [[3, 5], [5, 5], [3, 3], [5, 3]]      # center [4, 4]
    area_3 = [[-30, -10], [-10, -10], [-30, -30], [-10, -30]]
    area_4 = [[4, -4], [2, -6], [6, -6], [4, -8]]  # center [4, -6]
    raw_data = area_1 + area_2 + area_3 + area_4

    total_ddd = 0
    for i in k_mean(raw_data, 4):
        print(i)
        total_ddd += total_distance(i[0], i[1])
    print(total_ddd)
    # >>>
    # not perfect, as centroids can be lost during the re-learning, if one is not grouped to any.
    # also the calculation method is not perfect (calculating the average mean x and y for centroid), as it might miss looking for the centroids


    # True centroids
    # ([-5.0, 5.0], [[-6, 6], [-4, 6], [-6, 4], [-4, 4]])
    # ([4.0, 4.0], [[3, 5], [5, 5], [3, 3], [5, 3]])
    # ([-20.0, -20.0], [[-30, -10], [-10, -10], [-30, -30], [-10, -30]])
    # ([4.0, -6.0], [[4, -4], [2, -6], [6, -6], [4, -8]])
    # 75.88225099390857
