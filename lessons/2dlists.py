
# Given an array of ints, return a new array with
# the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
# reverse([1, 2, 3]) → [3, 2, 1]
# reverse([5, 11, 9]) → [9, 11, 5]
# reverse([7, 0, 0]) → [0, 0, 7]

#          0, 1, 2, 3, 4
my_list = [1, 2, 3, 4, 5]

def reverse(my_list):
    rev_list = []
    for index in range(1, len(my_list)+1):
        rev_list.append(my_list[-index])
    return rev_list

print(reverse([1,2,3,4,5])) # [5,4,3,2,1]

list_2d = [[-4, 2, 8],
            [10, 23, 0],
            [-2, 4, 8]]
print(list_2d[1][1])

print([0] * 6)

n = 3
print([[0] * n for _ in range(n)])
