# 'with creates a context for the file
# When the block ends, the file will close automatically

with open ('new_file.txt')as file:
    for line in file:
        print(line.strip())