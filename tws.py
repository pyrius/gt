def twoSum(nums, target):
    seen = {}
    for i, v in enumerate(nums):
        remaining = target - v
        if remaining in seen:
            print(f"i = {i}, v = {v}")
            print(f"remaining = {remaining}")
            return (seen[remaining], i)
        seen[v] = i
        print(f"seen = {seen}")
    return ()


nums = [1, 2, 5, 7, 3, 4, 7, 8, 4, 2, 9]
target = 17
print(twoSum(nums, target))
