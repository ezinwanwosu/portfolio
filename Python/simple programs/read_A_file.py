print('This program allows you to read a select amount of lines from a file or how many words')
def read_file(file,length,ask):
    try:
        with open(f'{file}.txt','r') as f:
            if ask == 'l':
                doc = f.readlines()
                for i in range(length):
                    print(doc[i])
            else:
                full = ''
                data = f.read()
                words = data.split()
                for i in range(length):
                    full += f'{words[i]} '
                print(full)
    except:
        print("File doesn't exist")

file = input("Enter the file name: ")
ask = input('Lines (l) or word count (w) ')
if ask == 'l':
    length = int(input("Enter how many lines you want to read: "))
else:
    length = int(input("Enter word count: "))

    
read_file(file,length,ask)
