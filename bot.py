import discord
import json
import configparser

print('imports complete')

#read and import the config file
config = configparser.ConfigParser()
config.read('config.ini')
TOKEN = config['bot']['discordbottoken']

#configure the bot
intents = discord.Intents.default()
intents.messages = True


#print(TOKEN)

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('                     .:-===+++++++==-:.                     ')
    print('                .-=++++++++++++++++++++++=-:                ')
    print('             :=++++++++++++++++++++++++++++++=-.            ')   
    print('          .=++++++++++++++++++++++++++++++++++++=:          ')
    print('        .=+++++++++++++++++++::=++++++++++++++++++=:        ')
    print('      .=++++++++++++++++++=:    .=+++++++++++++++++++:      ')
    print('     -+++++++++++++++++++:        .=++++++++++++++++++-     ')
    print('    -++++++++++++++++++:            -++++++++++++++++++=    ')
    print('   =++++++++++++++++=:              :=+++++++++++++++++++   ')
    print('  =+++++++++++++++++:                 :++++++++++++++++++=  ')
    print(' :+++++++++++++++: :==:                 :+++++++++++++++++= ')
    print(' +++++++++++++=:     :=+:   ..            :===+++++++++++++.')
    print('-++++++++++++:         :++:=+-                .=+++++++++++-')
    print('=++++++++++:            .++-.                   :=+++++++++=')
    print('++++++++=:             :+-                        .=++++++++')
    print('++++++++=.                         -:             .=++++++++')
    print('=+++++++++=.                    .-+:            .-++++++++++')
    print('-+++++++++++=:                .-=:=+:         .=+++++++++++-')   
    print(' +++++++++++++==+:             :   :++:     .=+++++++++++++.')
    print(' :++++++++++++++++=:                 :==: .-++++++++++++++= ')
    print('  =++++++++++++++++++:                 :++++++++++++++++++  ')
    print('   ++++++++++++++++++++:              .=+++++++++++++++++.  ')
    print('    =++++++++++++++++++=            .-++++++++++++++++++.   ')
    print('     -++++++++++++++++++=:        .=++++++++++++++++++-     ')
    print('      .=++++++++++++++++++=.    .=+++++++++++++++++++:      ')
    print('        :+++++++++++++++++++=..-+++++++++++++++++++-        ')
    print('          :=++++++++++++++++++++++++++++++++++++=:          ')
    print('            .-=+++++++++++++++++++++++++++++++-.            ')
    print('               .:-++++++++++++++++++++++++-:.               ')
    print('                    .::-==++++++++==--:.                    ')
    print(f'logged in as {client.user}')
    print('MHISdisbot is online')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    #if message.content.startswith('$hello'):
     #   embed=discord.Embed(title="Hello World!", description=" MHIS is a bot that (for now) acts as the interface between Discord ,meshtastic (and hopefully soon the physical maidstone hackspace)", color=0x00ff00)
      #  embed.set_author(name="Maidstone Hackspace Info System", icon_url="https://maidstone-hackspace.org.uk/wp-content/uploads/2022/09/cropped-hackspace_960x540.png")
       # await message.channel.send(embed=embed)
        #print('hello world')
        
        
    if message.content.startswith('!ping'):
        await message.channel.send('Pong')
        print('pong')
        
    if message.content.startswith('!disrepo'):
        await message.channel.send('https://github.com/maidstone-hackspace/MHISdisbot')
        print('disrepo')

    if message.content.startswith('!meshrepo'):
        await message.channel.send('https://github.com/maidstone-hackspace/MHISmeshbot')
        print('meshrepo')

    if message.content.startswith('!help'):
        await message.channel.send('command list')
        await message.channel.send('test if the bot is active = !ping')
        await message.channel.send('link to the discord bot github repo = !disrepo')
        await message.channel.send('link to the Meshtastic bot github repo = !meshrepo')
        print('command list')

client.run(TOKEN)
