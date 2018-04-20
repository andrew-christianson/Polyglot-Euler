import random


def read_tri(flike):
    tri_arr = []
    for line in flike:
        line = line.strip("\n")
        tri_arr.append([int(s) for s in line.split(" ")])
    return tri_arr


def path_score(path, tri_arr):
    return sum([tri_arr[idx][chc] for idx, chc in enumerate(path)])


def greedy_forward(tri_arr, initial_row=0, initial_idx=0):
    path = [initial_idx]
    for idx, row in enumerate(tri_arr[initial_row:]):
        prev_i = idx - 1
        prev_p = path[prev_i]
        if idx == 0:
            continue
        if prev_p >= len(row):
            path.append(len(row) - 1)
        else:
            path.append(prev_p if row[prev_p] > row[prev_p + 1] else prev_p + 1)
    return path


def greedy_backward(tri_arr, initial_idx=2, initial_row=0):
    path = [initial_idx]
    for idx, row in enumerate(reversed(tri_arr[:initial_row])):
        if idx == 0:
            continue
        prev_i = idx - 1
        prev_p = path[prev_i]
        if prev_p >= len(row):
            path.append(len(row) - 1)
        elif prev_p <= 0:
            path.append(0)
        else:
            if row[prev_p] > row[prev_p - 1]:
                path.append(prev_p)
            elif row[prev_p] == row[prev_p - 1]:
                path.append(random.choice([prev_p, prev_p-1]))
            else:
                path.append(prev_p-1)
    return list(reversed(path))


def look_forward_greedily(tri_arr):
    path = [0]
    for idx, row in enumerate(tri_arr):
        if idx == 0:
            continue
        prev_p = path[idx - 1]
        c_1_gpath = greedy_forward(tri_arr, initial_row=idx, initial_idx=prev_p)
        c_1_val = path_score(c_1_gpath, tri_arr[idx:])
        c_2_gpath = greedy_forward(tri_arr, initial_row=idx, initial_idx=prev_p + 1)
        c_2_val = path_score(c_2_gpath, tri_arr[idx:])
        if c_1_val > c_2_val:
            path.append(prev_p)
        else:
            path.append(prev_p + 1)
    return path


def look_backward_greedily(tri_arr, initial_idx):
    path = [initial_idx]
    for idx, row in enumerate(reversed(tri_arr)):
        if idx == 0:
            continue
        prev_p = path[idx - 1]
        if prev_p == 0:
            path.append(0)
        elif prev_p >= len(row):
            path.append(len(row) - 1)
        else:
            c_1_gpath = greedy_backward(tri_arr, initial_row=len(tri_arr) - idx, initial_idx=prev_p)
            c_1_val = path_score(c_1_gpath, tri_arr[:len(tri_arr) - idx])
            c_2_gpath = greedy_backward(tri_arr, initial_row=len(tri_arr) - idx, initial_idx=prev_p - 1)
            c_2_val = path_score(c_2_gpath, tri_arr[:len(tri_arr) - idx])
            if c_1_val > c_2_val:
                path.append(prev_p)
            else:
                path.append(prev_p - 1)
    return list(reversed(path))

if __name__ == '__main__':
    with open("Problem 67.txt", "r") as tfile:
        tri_arr = read_tri(tfile)
    res = look_forward_greedily(tri_arr)
    print("The (wrong) answer to Euler Problem 67 is", path_score(res,tri_arr))

    