file = open('new_file.txt')

for line in file:
    print(line.strip())

file.close()