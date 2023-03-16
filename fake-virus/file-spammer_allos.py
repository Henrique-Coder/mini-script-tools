# </> -- > Developed by: @Henrique-Coder (https://github.com/Henrique-Coder) </>

quantity = 3  # Quantity of files to be created
prefix = 'A'  # Prefix of the files
extension = 'txt'  # Extension of the files (without the dot)


for i in range(1, quantity+1):  # Loop to create the files
    with open(f'{prefix}{i}.{extension}', 'w') as f:  # Open the file
        f.write('')  # Write something/nothing

f.close()  # Close the file
