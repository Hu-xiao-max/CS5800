def search_insert(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # If not found, left is the correct insert position
    return left

# 示例测试
print(search_insert([1, 3, 5, 6], 5))  # 输出 2
print(search_insert([1, 3, 5, 6], 2))  # 输出 1
print(search_insert([1, 3, 5, 6], 7))  # 输出 4
