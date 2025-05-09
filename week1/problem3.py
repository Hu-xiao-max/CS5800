def count_critical_events(A, t):
    count = 0
    n = len(A)
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] > t * A[j]:
                count += 1
    return count

# 示例测试
if __name__ == "__main__":
    # A = [12, 3, 6, 1, 9, 17, 19]
    A = [1, 2, 3, 16, 12, 19, 17, 19, 18, 9, 10]
    t1 = 2
    t2 = 3
    result1 = count_critical_events(A, t1)
    result2 = count_critical_events(A, t2)
    print('Array A', A)
    print("Number of critical events 1 :", result1)
    print("Number of critical events 2 :", result2)
