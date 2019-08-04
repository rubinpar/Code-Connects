for i in range(10):
    print(i)

arr = [i for i in range(10)]
print(arr) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr[4] = 100
arr[8] = 800
print(arr) # [0, 1, 2, 3, 100, 6, 7, 800, 9]


arr = [2*i + 1 for i in range(5)]
# [0, 1, 2, 3, 4]
# [1, 3, 5, 7, 9]
print(arr)
# [1, 3, 5, 7, 9]

arr = [i**2 for i in range(7)]
print(arr)
# [0, 1, 2, 3, 4, 5, 6]
# [1, 2, 4, 8, 16, 32, 64]
