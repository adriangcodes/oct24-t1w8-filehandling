# Open a file for writing - destructive operation - if the file already exists, it will empty it first
file = open('new_file.txt', 'w') # creates the file for writing
# w for overwrite, a for append existing file

file.write('This is a new file!\n') # \n adds a new line
file.write('See ya!\n')

file.close