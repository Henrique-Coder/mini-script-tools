from os import system as cmd


appdir = 'dir/to/app.extension'  # Change to the path of the app you want to open
quantity = 3  # Change to the number of times you want the app to open

# Creates a loop to open the app the number of times you choose
for i in range(quantity):
    cmd(appdir)
