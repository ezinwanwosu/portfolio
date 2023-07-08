def is_prime(n):
    not_prime = False
    lst = [2,3,5,7]
    if n in lst:
        not_prime = False
    el
    if n > 1:
        for i in lst:
            if n%i == 0:
                not_prime = True
    else:
        not_prime = True
    return not_prime
        
while True:
    try:
        n = int(input("Enter a number: "))
        break
    except:
        print("Enter a integer")
not_prime = is_prime(n)
if not_prime == True:
    print("Number isn't Prime")
else:
    print("Number is prime")

