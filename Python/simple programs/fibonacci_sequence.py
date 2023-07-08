def fibonacci(r):
    if r in {0,1}:
        return r
    return fibonacci(r-1)+fibonacci(r-2)

valid = False
while not valid:
    try:
        length = int(input("Enter length of fibonacci sequence: "))
        valid = True
    except:
        print('Type an integer')
print([fibonacci(n) for n in range(length)])
