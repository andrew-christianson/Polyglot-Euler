from __future__ import print_function
import copy

def read_tri(flike):
    tri_arr = []
    for line in flike:
        line = line.strip("\n")
        tri_arr.append([int(s) for s in line.split(" ")])
    return tri_arr


def efficient(tri_arr):
    tri_arr = list(reversed(copy.deepcopy(tri_arr)))
    for idx, row in enumerate(tri_arr):
        if idx == 0:
            continue
        for ridx, _ in enumerate(row):
            tri_arr[idx][ridx] += max(tri_arr[idx-1][ridx], tri_arr[idx-1][ridx + 1])
    return tri_arr[-1][0]

if __name__ == '__main__':
    with open("Problem 67.txt", "r") as ftri:
        tri_arr = read_tri(ftri)
    res = efficient(tri_arr)
    print("The answer to Euler Problem 67 is", res)
