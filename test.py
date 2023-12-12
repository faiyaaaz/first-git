def facto(a):
    factorial = 1

    if a == 0:
        factorial = 1
        return factorial
    for i in range(1,a+1):
        factorial = factorial * i

    return factorial

print(facto(int(input("Enter: "))))

def is_prime(a):
    flag = True
    if a == 1 :
        flag = False
        return flag
    for i in range(2,a):
        if a % i == 0:
            flag = False
    return flag

print(is_prime(int(input("Enter a: "))))
    