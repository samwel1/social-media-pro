import re


#take the file name
name = input("Enter the file name:")

#open file
f = open(name)

#read file
words = f.read()

#define regex pattern
pat = r"#\w+"

#return a list of words
res = re.findall(pat, words)

#iterate through the list and print the words
for word in res:
    print(word)
