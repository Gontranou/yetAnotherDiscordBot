
import discord #pour utiliser discord
import numpy as np
import random
from dotenv import load_dotenv #en test pour une "environment variable"
import os


client = discord.Client()

tanks = []                                        #all the basic bs
healers = []
dps = []
emojiTank = '<:sadcat2:643173970400772126>'
emojiHeal = '<:jesus:642763325343662155>'
emojiDps = '<:gungeon:642779751202684968>'
premierGroupe = []
deuxiemeGroupe = []
troisiemeGroupe = []
quatriemeGroupe = []

@client.event
async def on_ready():
	print('I have logged in') #se connecte et dit qu'il se connecte, c'est fou quand même la technologie
	# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="toujours..."))
	# await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="par la fenêtre..."))
	await client.change_presence(activity=discord.Streaming(name="rien", url="https://www.youtube.com/watch?v=fC7oUOUEEi4"))
	await client.user.edit(username="New Horizons rands")

@client.event 
async def on_reaction_add(reaction, user): #quand une réaction arrive
	if user.name == 'FAIT DES RANDS TOUT SEUL !!': #ne prend pas en compte ses propres réacitons
		return

	channel = reaction.message.channel #prend le channel dans lequel la réaction à lieu
	print( '{} a réagi avec {}'.format(user.name, reaction.emoji)) #send a la console qui a réagi et avec quoi, par soucis de debug

	if str(reaction.emoji) == '<:sadcat2:643173970400772126>': #check si l'emoji de la réaction est bien celui voulu
		tanks.append(user.name) #ajoute le pseudo de la personne qui a réagi à la liste
		print('les tanks : {}'.format(tanks))
	elif str(reaction.emoji) == '<:jesus:642763325343662155>':
		healers.append(user.name)
		print('les heals : {}'.format(healers))
	elif str(reaction.emoji) == '<:gungeon:642779751202684968>':
		dps.append(user.name)
		print('les dps : {}'.format(dps))
	else:
		return

	print(reaction.emoji)

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('.start'): #envoie le message pour initaliser la récupération de réactions
		msg = await message.channel.send('__***↘ Veuillez réagir avec ↙***__\n<:sadcat2:643173970400772126> *si vous êtes tank*\n<:jesus:642763325343662155> *si vous êtes heal*\n<:gungeon:642779751202684968> *si vous êtes dps*')
		await msg.add_reaction(emojiTank)
		await msg.add_reaction(emojiHeal)
		await msg.add_reaction(emojiDps)

	if message.content.startswith('.rand'): #commence le rand
		random.shuffle(tanks) #shuffle toutes les listes, toute la randomizer part est ici
		random.shuffle(healers)
		random.shuffle(dps)

		print(dps) #présent par pur soucis de debug
		print(healers)
		print(tanks)

		if len(tanks) == 1: #ajoute aux différents groupes dans un certain ordres les personnes qui ont réagis à leurs rôles avec : Tank > Heal > Dps
			premierGroupe.append(tanks[0])
		else:
			premierGroupe.insert(0, "Un tank PU")

		if len(healers) == 1:
			premierGroupe.append(healers[0])
		else: 
			premierGroupe.insert(1, "Un heal PU")

		if len(dps) == 1:
			premierGroupe.append(dps[0])
		else:
			premierGroupe.insert(2, 'Un dps PU')

		if len(dps) == 2:
			premierGroupe.remove('Un dps PU') #à partir d'ici le bullshit commence....
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
		else:
			premierGroupe.insert(3, 'Un dps PU')

		if len(dps) == 3:
			premierGroupe.remove('Un dps PU') #enlève chaque 'Un ... PU' à chaque fois et le remplace par celui convenue. Et ça pour tous les rôles et tout le temps
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
		else:
			premierGroupe.insert(4, 'Un dps PU')



		if len(tanks) == 2:
			premierGroupe.remove('Un tank PU')
			premierGroupe.insert(0, tanks[0])
			deuxiemeGroupe.append(tanks[1])
		else:
			deuxiemeGroupe.insert(0, 'Un tank PU')

		if len(healers) == 2:
			premierGroupe.remove('Un heal PU')
			premierGroupe.insert(1, healers[0])
			deuxiemeGroupe.append(healers[1])
		else:
			deuxiemeGroupe.insert(1, "Un heal PU")

		if len(dps) == 4:
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.append(dps[3])
		else:
			deuxiemeGroupe.insert(2, "Un dps PU")

		if len(dps) == 5:
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.append(dps[3])
			deuxiemeGroupe.append(dps[4])
		else:
			deuxiemeGroupe.insert(3, "Un dps PU")

		if len(dps) == 6:
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.append(dps[3])
			deuxiemeGroupe.append(dps[4])
			deuxiemeGroupe.append(dps[5])
		else:
			deuxiemeGroupe.insert(4, "Un dps PU")


		if len(tanks) == 3:
			premierGroupe.remove('Un tank PU')
			deuxiemeGroupe.remove('Un tank PU')
			premierGroupe.insert(0, tanks[0])
			deuxiemeGroupe.insert(0, tanks[1])
			troisiemeGroupe.append(tanks[2])
		else:
			troisiemeGroupe.insert(0, "Un tank PU")

		if len(healers) == 3:
			premierGroupe.remove('Un heal PU')
			deuxiemeGroupe.remove('Un heal PU')
			premierGroupe.insert(1, healers[0])
			deuxiemeGroupe.insert(1, healers[1])
			troisiemeGroupe.append(healers[2])
		else:
			troisiemeGroupe.insert(1, "Un heal PU")
		
		if len(dps) == 7:
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.append(dps[3])
			deuxiemeGroupe.append(dps[4])
			deuxiemeGroupe.append(dps[5])
			troisiemeGroupe.append(dps[6])
		else:
			troisiemeGroupe.insert(2, "Un dps PU")

		if len(dps) == 8:
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.append(dps[3])
			deuxiemeGroupe.append(dps[4])
			deuxiemeGroupe.append(dps[5])
			troisiemeGroupe.remove('Un dps PU')
			troisiemeGroupe.append(dps[6])
			troisiemeGroupe.append(dps[7])
		else: 
			troisiemeGroupe.insert(3, "Un dps PU")

		if len(dps) == 9:
			premierGroupe.remove('Un dps PU') #pas encore trouvé d'alternative à cette horreur visuelle.
			premierGroupe.remove('Un dps PU')
			premierGroupe.remove('Un dps PU')
			premierGroupe.append(dps[0])
			premierGroupe.append(dps[1])
			premierGroupe.append(dps[2])
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.remove('Un dps PU')
			deuxiemeGroupe.append(dps[3])
			deuxiemeGroupe.append(dps[4])
			deuxiemeGroupe.append(dps[5])
			troisiemeGroupe.remove('Un dps PU')
			troisiemeGroupe.remove('Un dps PU')
			troisiemeGroupe.append(dps[6])
			troisiemeGroupe.append(dps[7])
			troisiemeGroupe.append(dps[8]) #c'est genre vraiment moche, beurk
		else:
			troisiemeGroupe.insert(4, "Un dps PU")

			#créations des 'embed' qui seront envoyés dans le chat

		embed1 = discord.Embed(title='Groupe Numéro 1', url="https://www.youtube.com/watch?v=dQw4w9WgXcQ", color=0x366bb8)
		embed1.set_author(name="Si vous n'êtes pas avec les personnes que vous voulez, plaignez-vous au Dieu de la RNG", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819238578269323314/arrow.png")
		embed1.add_field(name="Dans votre groupe vous avez :", value=" \u200b", inline=False)
		embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/399167973774065666/819208315422638131/M.png")
		embed1.add_field(name="Tank : ", value=premierGroupe[0], inline=True)
		embed1.add_field(name="Healer : ", value=premierGroupe[1], inline=True)
		embed1.add_field(name="Dps : ", value=premierGroupe[2], inline=False)
		embed1.add_field(name="Dps : ", value=premierGroupe[3], inline=False)
		embed1.add_field(name="Dps : ", value=premierGroupe[4], inline=False)
		embed1.set_footer(text="De la part de Gontranou, Bonne chance pour votre clé :D", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819187730453495808/NHimg.png")

		embed2 = discord.Embed(title='Groupe Numéro 2', url="https://youtu.be/_S7WEVLbQ-Y?t=313", color=0x003481)
		embed2.set_author(name="Si vous n'êtes pas avec les personnes que vous voulez, plaignez-vous au Dieu de la RNG", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819238578269323314/arrow.png")
		embed2.add_field(name="Dans votre groupe vous avez :", value=" \u200b", inline=False)
		embed2.set_thumbnail(url="https://cdn.discordapp.com/attachments/399167973774065666/819208315422638131/M.png")
		embed2.add_field(name="Tank : ", value=deuxiemeGroupe[0], inline=True)
		embed2.add_field(name="Healer : ", value=deuxiemeGroupe[1], inline=True)
		embed2.add_field(name="Dps : ", value=deuxiemeGroupe[2], inline=False)
		embed2.add_field(name="Dps : ", value=deuxiemeGroupe[3], inline=False)
		embed2.add_field(name="Dps : ", value=deuxiemeGroupe[4], inline=False)
		embed2.set_footer(text="De la part de Gontranou, Bonne chance pour votre clé :D", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819187730453495808/NHimg.png")

		embed3 = discord.Embed(title='Groupe Numéro 3', url="https://www.youtube.com/watch?v=YUZsHDB8o2Q", color=0x000038)
		embed3.set_author(name="Si vous n'êtes pas avec les personnes que vous voulez, plaignez-vous au Dieu de la RNG", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819238578269323314/arrow.png")
		embed3.add_field(name="Dans votre groupe vous avez :", value=" \u200b", inline=False)
		embed3.set_thumbnail(url="https://cdn.discordapp.com/attachments/399167973774065666/819208315422638131/M.png")
		embed3.add_field(name="Tank : ", value=troisiemeGroupe[0], inline=True)
		embed3.add_field(name="Healer : ", value=troisiemeGroupe[1], inline=True)
		embed3.add_field(name="Dps : ", value=troisiemeGroupe[2], inline=False)
		embed3.add_field(name="Dps : ", value=troisiemeGroupe[3], inline=False)
		embed3.add_field(name="Dps : ", value=troisiemeGroupe[4], inline=False)
		embed3.set_footer(text="De la part de Gontranou, Bonne chance pour votre clé :D", icon_url="https://cdn.discordapp.com/attachments/399167973774065666/819187730453495808/NHimg.png")


		await message.channel.send(embed=embed1) #envoye enfin les 'embed' dans le chat avec les groupes prêt à partir au combat !
		await message.channel.send('\u200b')
		await message.channel.send(embed=embed2)
		# await message.channel.send('\u200b') #j'utilise des commentaires pour garder la commande mais ne pas l'utiliser
		# await message.channel.send(embed=embed3)
		print(premierGroupe)
		print(deuxiemeGroupe)
		print(troisiemeGroupe)
		


		# await message.channel.send('les tanks : {}\nles heals : {}\nles dps : {}'.format(tanks, healers, dps))





load_dotenv('.env') #load l'environment variable dans '.env'
# client.run(os.getenv('TOKEN'))
client.run('') #insert token here

#merci d'avoir lu tous ces commentaires inutiles, j'écrirai peut-être un livre un jour avec tous ces commentaires...