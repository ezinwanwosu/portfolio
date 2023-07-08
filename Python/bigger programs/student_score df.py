import pandas as pd
#names = ['A','B','C','D','E','F','G','H','I','J']
#scores = [50,36,80,46,36,97,36,86,14,100]
#student_dict = {'Name':names, 'Score':scores}
#df = pd.DataFrame(student_dict)
#print(df)
#df.to_csv(r'C:\Users\bianc\OneDrive\Portfolio\Python\bigger programs\student_score.txt',index = None,header = None)

def menu():
    valid = False
    print('''
1.Input student name and score
2.Output students name and score that passed
3.Quit ''')
    while not valid:
        try:
            choice = int(input("Enter your choice: "))
            if choice >0 and choice <4:
                valid = True
        
        except:
            print('Enter an integer')
            valid = False
    if choice == 1:
        name = ''
        names = []
        scores = []
        while name != 'xxx':
            name = input("Enter students name:  (xxx to end)")
            if name == 'xxx':
                break
            names.append(name)
            try:
                score = int(input("Enter students score"))
                scores.append(score)
            except:
                print("Error - Invalid Input - Try again")
                names.pop()
                scores.pop()
            
                
        with open('student_score.txt','a') as f:
            for i in range(len(names)):
                f.write(f'{names[i]},{scores[i]}\n')
        
menu()
                
            
            
            
