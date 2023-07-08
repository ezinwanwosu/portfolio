#Nth term [Arithmetic sequence]
#nth term function and length
def nthTerm(nth_term,length):
    index = nth_term.find('n')
    num = nth_term[0:index]
    n = nth_term[index]
    sign = nth_term[index+1]
    end = nth_term[index+2:]
    for i in range(1,length+1):
        if sign == '+':
            print(num)
            print(i)
            print(end)
            print(f'{(float(num)*i)+float(end)}')
        else:
            print(f'{(float(num)*i)-float(end)}')

valid = False
                
#ask for nth term
nth_term = input("Enter nth term: ")
#ask for length
while not valid:
    try:
        length = int(input("Enter length of sequence: "))
        valid = True
    except:
        print("Enter integer")
        valid = False
nthTerm(nth_term,length)

#by bianca
