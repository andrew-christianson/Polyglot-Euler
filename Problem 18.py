import random

def read_tri(flike):
    tri_arr = []
    for line in flike:
        line = line.strip("\n")
        tri_arr.append([int(s) for s in line.split(" ")])
    return tri_arr

# def valid_path(path):
#     if path[0] != 0:
#         return False
#     for idx, pidx in enumerate(path[1:]):
#         if not (pidx - 1 == path[idx - 1] or pidx + 1 == path[idx - 1]):
#             return False
#     return True

def greedy_forward(tri_arr, startrow=0, startidx=0):
    path = [startidx]
    for idx, row in enumerate(tri_arr[startrow:]):
        prev_i = idx - 1
        prev_p = path[prev_i]
        if idx == 0:
            continue
        path.append(prev_p if row[prev_p] > row[prev_p + 1] else prev_p + 1)
    return path

# def argmax(list):
#     return max(zip(range(len(list)), list), key=lambda item: item[1])[0]

# def greedy_backward(tri_arr, initial_idx=2):
#     path = [initial_idx]
#     for idx, row in enumerate(reversed(tri_arr)):
#         if idx == 0:
#             continue
#         prev_i = idx - 1
#         prev_p = path[prev_i]
#         if prev_p >= len(row):
#             path.append(len(row) - 1)
#         elif prev_p == 0:
#             path.append(0)
#         else:
#             if row[prev_p] > row[prev_p - 1]:
#                 path.append(prev_p)
#             elif row[prev_p] == row[prev_p - 1]:
#                 path.append(random.choice([prev_p, prev_p-1]))
#             else:
#                 path.append(prev_p-1)
#     return reversed(path)

def look_forward_greedily(tri_arr):
    path = [0]
    for idx, row in enumerate(tri_arr):
        if idx == 0:
            continue
        prev_p = path[idx - 1]
        c_1_gpath = greedy_forward(tri_arr, startrow=idx, startidx=prev_p)
        c_1_val = path_score(c_1_gpath, tri_arr[idx:])
        c_2_gpath = greedy_forward(tri_arr, startrow=idx, startidx=prev_p + 1)
        c_2_val = path_score(c_2_gpath, tri_arr[idx:])
        if c_1_val > c_2_val:
            path.append(prev_p)
        else:
            path.append(prev_p + 1)
    return path

def path_score(path, tri_arr):
    return sum(tri_arr[idx][chc] for idx, chc in enumerate(path))

if __name__ == '__main__':
    with open("Problem 18.txt", "r") as ftri:
        tri_arr = read_tri(ftri)
    res = path_score(look_forward_greedily(tri_arr), tri_arr)
    print("The Answer to Euler Problem 18 is", res)