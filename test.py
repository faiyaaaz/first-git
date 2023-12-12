def facto(a):
    factorial = 1

    if a == 0:
        factorial = 1
        return factorial
    for i in range(1,a+1):
        factorial = factorial * i

    return factorial

print(facto(int(input("Enter: "))))