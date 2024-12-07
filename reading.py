file = open('new_file.txt')

content = file.read(10) # integer value will only read specific number of characters
print(content)

content = file.read(10) # file remembers where it was from last read and starts from last point
print(content)
file.seek(0) # changes position of the next operation
file.tell() # returns current position

# content = file.readline().strip() # strip removes any whitespace (including new lines) from both the beginning and end of string
# # print(repr(content))
# print(content)

# content = file.readline().strip()
# print(content)

# content = file.readlines()
# print(content)

file.close