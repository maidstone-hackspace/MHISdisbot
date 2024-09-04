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

    if message.content.startswith('$hello'):
        embed=discord.Embed(title="Hello World!", description=" MHIS is a bot that (for now) acts as the interface between Discord ,meshtastic (and hopefully soon the physical maidstone hackspace)", color=0x00ff00)
        embed.set_author(name="Maidstone Hackspace Info System", icon_url="https://maidstone-hackspace.org.uk/wp-content/uploads/2022/09/cropped-hackspace_960x540.png")
        await message.channel.send(embed=embed)
        print('hello world')
        
        
    #if message.content.startswith('$ping'):
      #  await message.channel.send('Pong')
      #  await edit(nick='Macaroni Dispenser')
      #  print('pong')


client.run(TOKEN)
