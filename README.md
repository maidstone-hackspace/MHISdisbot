# (MHISdisbot) Maidstone Hackspace Infomation System DIScord BOT module
[![Bandit](https://github.com/maidstone-hackspace/MHISdisbot/actions/workflows/bandit.yml/badge.svg)](https://github.com/maidstone-hackspace/MHISdisbot/actions/workflows/bandit.yml)
![image](https://github.com/user-attachments/assets/ddddfc99-50ec-4f26-9985-b95485383bda)

This is the Bot module of the Maidstone hackspace infomation system , it will combine regular discord bot features with an mqtt client to allow for simple comumnication with the other modules 
 

**Dependancies:**

[Python 3.12.5](https://www.python.org/downloads/release/python-3125/) (Latest)

[Discord.py](https://pypi.org/project/discord.py/) (Latest)


**Todo:**

mqtt 

write some pytest scripts

fancy embeds

make it run as a container (also so the container code can be used to make templates for other modules)

change the discord token to a secret/enviromental variable imported to the container instead of a local file that is just gitignore'ed
