# </> -- > Developed by: @Henrique-Coder (https://github.com/Henrique-Coder) </>

from os import startfile


tabs = 3  # Number of tabs to open
url = 'http://www.google.com'  # URL to open

while tabs > 0:  # Loop to open tabs
    startfile(url)  # Open tab
    tabs -= 1  # Decrease tabs counter
