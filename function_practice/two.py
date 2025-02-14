# Basic logic
def animal_crackers(text):
    wordlist = text.lower().split()
    return wordlist[0][0] == wordlist[1][0]

print(animal_crackers('Cat acamel'))
print(animal_crackers('Cat Caamel'))
print(animal_crackers('Cat camel'))