# Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'

list = []
for word in st.split():
    list.append(word[0])
print(list)

list_let = [i[0] for i in st.split()]
print(list_let)