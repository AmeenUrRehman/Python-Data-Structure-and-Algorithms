# Divide big problems into small and simple problems
# Find a base condition with simple answer
# Return a roll back answer for base condition to solve all sub problems.

# Normal Iteration Loop
def find_sum(num):
    sum = 0
    for i in range(1,num+1):
        sum += i
    return sum

# Recursion
def find_sum_with_recursion(num1):
    if num1 == 1:
        return 1
    return num1 + find_sum_with_recursion(num1-1)

if __name__ == "__main__":
    print(find_sum(4))
    print(find_sum_with_recursion(4))


