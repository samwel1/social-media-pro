import re

#take the input
text = input()

#define regex sequence
pattern = r'#\w+'

#serch throuh the input and return a list of words
search = re.findall(pattern,text)

#join the list with a new line. Can also be achieved using for loop
result = "\n".join(search)

#Print result
print(result)
