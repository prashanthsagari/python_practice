# Use for, .split(), and if to create a Statement that will print out words that start with 's':
st = 'Print only the words that Start with s in this sentence'

for word in st.split():
    if(word[0].lower() == 's'):
        print(word)


# Use range() to print all the even numbers from 0 to 10.
for i in range(10):
    if(i %2 == 0):
        print(i)
        
        # div_by_3 = [x for x in range(1, 51) if x % 3 == 0]
        # div_by_3 = list(filter(lambda x: x % 3 == 0, range(1, 51)))
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
print('***********')
for i in range(1, 50):
    if (i % 3 == 0):
        print(i)
        


# Go through the string below and if the length of a word is even print "even!"

str = 'Print every word in this sentence that has an even number of letters'
for word in str.split():
    if (len(word) % 2 == 0):
        print(word)

list = [word for word in str.split() if (len(word) % 2 == 0)]
print(list)