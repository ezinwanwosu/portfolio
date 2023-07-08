#This program allows you to input towns and there population and gives you the option to output the town with the largest population
def menu():
    print("""
1. Input town and their populations
2. Display town with largest population
3. Edit town and/or population
4. Quit program """)
    choice = int(input())
    return choice

def option1():
    town = ''
    towns = []
    population = []
    while town != 'xxx':
        town = input("Enter town name:  (xxx to end)")
        if town == 'xxx':
            break
        towns.append(town)
        try:
            population = int(input("Enter population: "))
            towns.append(town)
        except:
            print("Error - Invalid Input - Try again")
            towns.pop()
            population.pop()
        
            
    with open('towns.txt','a') as f:
        for i in range(len(names)):
            f.write(f'{towns[i]},{population[i]}\n')
    


def option2():
    with open('towns.txt','r') as f:
        lines = f.readlines()
        for i in lines:
            
    







choice = menu()
while choice != 4:
    if choice == 1:
        option1()
        
