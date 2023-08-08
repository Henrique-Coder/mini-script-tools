from os import system as cmd


quantity = 3  # Number of notifications to send
prefix = 'N'  # Prefix of the notification title

for i in range(1, quantity + 1):  # Loop to send notifications
    cmd('msg * /time:0 /v ' + prefix + str(i))  # Send notification
