import subprocess
import discord
from discord.ext import commands
import time

# By DeadEagle

# Install Discord py / subprocess (if needed)


# Enter your token to connect your code to your bot.
TOKEN = 'Your-Discord-Bot-Token'

# Define the client
client = discord.Client()

# Define bot & prefix [Prefix not really used in this bot]
bot = commands.Bot(command_prefix='!')

# On Ready (This event will be called when the bot starts & is Ready [It will launch SearchForProcess(): & Start looking for your process]
@client.event
async  def on_ready():
    print('Logged in as {0.user}'.format(client))
    await SearchForProcess()

# LoopProcess, this is called AFTER SearchForProcess(): [Wait 3600 Seconds (1Hour) and continue Searching]
async def LoopProcess():
    time.sleep(3600)
    await SearchForProcess()

# SearchForProccess,
async def SearchForProcess():
    # Channel = Copy Discord Channel ID
    Channel = client.get_channel(912355235433967669)
    # processName = The Process you want to search.
    processName = 'PhoenixMiner.exe'

    # Finding all running processes.
    AllTasks = subprocess.check_output('tasklist', shell=True)
    # Converting it from Bytes to String so we can use it.
    AllTasksString = str(AllTasks)
    # If Processname (Your processName Variable) is found in the AllRunningTasks list, this the loop will reset, and wait 3600 seconds again to restart.
    if processName in AllTasksString:
        print('Online & Running.')
        await LoopProcess()
    # Else: If your processName Variable is NOT found in the TaskList, this Else: will run. it will send a message to your Channel Variable telling you
    # Your software is Offline, afterwards the bot will start looping again (wait 3600 seconds)
    else:
        print('Software NOT FOUND!')
        await Channel.send(processName +' IS NOT RUNNING AT THE MOMENT [Error]')
        await LoopProcess()


#Start your bot, include the token.
client.run(TOKEN)
