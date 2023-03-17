from os import makedirs as mkdir


quantity = 3  # Quantity of folders to create
prefix = 'F'  # Prefix of folder name

for i in range(1, quantity+1):  # Loop to create folders
    mkdir(prefix + str(i))  # Create folder
