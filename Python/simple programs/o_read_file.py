import pyttsx3

# initialisation
engine = pyttsx3.init()
  
print('This is a program that reads out your document')
def speak(doc):
    engine.say(doc)
    engine.runAndWait()
def get_file():
    f = input("Enter name of file: ")
    with open(f'f.txt','r') as file:
        doc = file.read()
    return doc

doc = get_file()
print(doc)
#speak(doc)
