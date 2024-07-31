"""
8
10
2 3 2 4 1 10 3 0

3
0 3 3 4
1 2 3 4
2 2 3 3

"""
# def get_sum_fours(line, m):
#     result = []
#     temp_result = []
#     remainder = 0
#     n = len(line)-1
#     counter = 4
#     index = 0
#     i = 0
#     while n > 0:
#         for i in range(len(line) - 1):
#             if i >= m or i > reminder:
#                 pass
#             remainder = m - i
#             i += 1
#             n -= 1



def read_input():
    n = int(input().strip())
    m = int(input().strip())
    line = [map(int, input().strip())]
    return line, m


line, m = read_input()
# get_sum_fours(line, m)
