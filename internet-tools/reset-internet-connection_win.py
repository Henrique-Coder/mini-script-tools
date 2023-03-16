# </> -- > Developed by: @Henrique-Coder (https://github.com/Henrique-Coder) </>

from os import system as cmd


# Reset internet connection
cmd('ipconfig /release')
cmd('ipconfig /renew')
cmd('ipconfig /flushdns')
