def fib(num, memo=None):
    if memo is None:
        memo = {}
    if num <= 2:
        return 1
    if num in memo:
        return memo[num]

    memo[num] = fib(num - 1, memo) + fib(num - 2, memo)

    return memo[num]


def grid_traveler(row, col, memo={}):
    key = f"{row},{col}"
    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0
    if key in memo:
        return memo[key]

    memo[key] = grid_traveler(row - 1, col, memo) + grid_traveler(row, col - 1, memo)

    return memo[key]


def can_sum(target, nums, memo={}):
    if target == 0:
        return True
    if target < 0:
        return False
    if target in memo:
        return memo[target]

    for num in nums:
        new_target = target - num

        if can_sum(new_target, nums, memo):
            memo[target] = True
            return True

    memo[target] = False
    return False


def sum_path(target, nums, result=[]):
    if target == 0:
        return result
    if target < 0:
        return None

    for num in nums:
        new_target = target - num
        if sum_path(new_target, nums, result) is not None:
            print(num)
            result.append(num)
            return result

    return None


def shortest_sum(target, nums):
    r = None
    if target == 0:
        return []
    if target < 0:
        return None

    for num in nums:
        new = target - num
        result = shortest_sum(new, nums)
        if result is not None:
            result.append(num)
            if r is None:
                r = result.copy()
            else:
                if len(r) > len(result):
                    r = result.copy()

    return r


def can_construct(target, wordbank):
    if target == "":
        return True

    for word in wordbank:
        if word in target:

            if (target.index(word)) == 0:
                if can_construct(target[len(word):], wordbank):
                    return True

    return False


print(can_construct("abcdef", ["ab", "abc", "cd", "a", "f", "a"]))
