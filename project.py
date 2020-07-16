import sys
import os
print('Argument List:', str(sys.argv[1]))
#what folder is in the current directory?


gather_array = []
#empty array to gather individual elements within each file


for filename in os.listdir(os.path.join(os.getcwd(), 'input')):
    with open('input/' + filename, 'r') as f:
        text = f.read()
        text_array = text.splitlines()
        for i in text_array:
            gather_array.append(i)
            gather_array.sort()
#loop through each text file within the folder to read the text
#turn the text into an array of an array
#loop through each array and add into gather_array
#sort the accumulated array in alphabetical order


final_array = []
#empty array to gather unique values


for i in gather_array:
    if i not in final_array:
        final_array.append(i)
#ensure uniqueness of individual sentences


final_file = open("final_text.txt", "w+")
for i in final_array:
    final_file.write(str(i) + '\n')
    print(i)
final_file.close()
#create and write to text file from final_array
