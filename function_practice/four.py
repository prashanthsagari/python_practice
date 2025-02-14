def master_yoda(text):
    str = ''
    for word in text.split()[::-1]:
        str += word + " "
    return str

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

def master_yoda_improved(text):
    return ' '.join(text.split()[::-1])

print(master_yoda_improved('I am home'))
print(master_yoda_improved('We are ready'))