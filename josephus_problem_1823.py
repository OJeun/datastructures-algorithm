# Time complexity: O(n^2), space complexity: O(n)
def find_the_winner(n, k):

    # create a circle of n elements using for loop
    # circle = []
    # for element in range(n):
    #     circle.append(element + 1)

    # create a circle array of n elements using list comprehension
    circle = [element + 1 for element in range(n)]

    return find_the_winner_helper(circle, k, 0)

def find_the_winner_helper(arr, k, start_index):
    if len(arr) == 1:
        return arr[0]
    array_length = len(arr)
    remove_index = (start_index + k - 1) % array_length
    arr.pop(remove_index)
    return find_the_winner_helper(arr, k, remove_index)

# Time complexity: O(n), space complexity: O(n)
def find_the_winner_with_big_o_n_time_complexity(n, k):
    def josephus(n):
        if n == 1:
            return 0
        return (josephus(n - 1) + k) % n
    return josephus(n) + 1

# Time complexity: O(n), space complexity: O(1)
def find_the_winner_using_array(n, k):
    winner = 0
    for i in range(2, n + 1):
        winner = (winner + k) % i
    return winner + 1