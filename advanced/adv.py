import shutil
import os
import re
# shutil.unpack_archive('unzip_me_for_instructions.zip')
# print(list(os.walk(os.getcwd())))

# with open('extracted_content/Instructions.txt', 'r') as file:
#     content = file.read()

# print(content)

# pattern = r'\d{3}-\d{3}-\d{4}'
# test_string = 'here is a phone 967-625-5233'
# print(re.findall(pattern,test_string))

def search(file, pattern=r'\d{3}-\d{3}-\d{4}'):
    with open(file, 'r') as f:
        text = f.read()
        
        if re.search(pattern, text):
            return re.search(pattern, text)
        else:
            pass

results = []
for folder,sub_folders, files in os.walk(os.getcwd() + '\\extracted_content'):
    for f in files:
        full_path = folder + '\\' + f
        
        results.append(search(full_path))
        

for r in results:
    if r != ' ' and r != None: 
        print(r.group())

