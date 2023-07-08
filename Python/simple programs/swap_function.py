def swap(a,b):
    c = a
    a = b
    b = c
    return a,b
if __name__ == '__main__':
    print('hi')
    swap()

def echo(word):
    echoed = word[-1]
    return f'{word}{echoed*5}'
