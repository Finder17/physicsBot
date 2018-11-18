import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os

Client = discord.Client()

client = Bot(command_prefix='!')

@client.event
async def on_ready():
    print("Bot is now online")
    

@client.event
async def on_message(message):
    userID = message.author.id

#    if message.content.lower().startswith("!help"):
#        await client.send_message(message.channel, "Why need help, when you can fly <@{}>".format(userID))
#        await client.process_commands(message)
    
    if message.content.lower().startswith("!god"):
        if message.author.id == "272773536265928715":
            await client.delete_message(message)
            await client.send_message(message.channel, "All hail the almighty overlord <@{}>".format(userID))
            

    if message.content.lower().startswith("!say"):
        if "512763360123813908" in [role.id for role in message.author.roles]:
            args = message.content.split(" ")
            await client.delete_message(message)
            await client.send_message(message.channel, "{}".format(" ".join(args[1:])))
        else:
            await client.send_message(message.channel, "You cannot do this D:")

    #if "" in message.content
    if message.content.lower().startswith("quark") or message.content.lower().startswith("quarks") or message.content.lower().startswith("antiquark") or message.content.lower().startswith("antiquarks"):
        await client.send_file(message.channel, "quark.png")

    if message.content.lower().startswith("annihilation"):
        await client.send_file(message.channel, "ParticleAnnihilation.png")

    if message.content.lower().startswith("pair production"):
        await client.send_file(message.channel, "pairproduction.png")

    if message.content.lower().startswith("subatomic") or message.content.lower().startswith("electron") \
    or message.content.lower().startswith("mass"):
        await client.send_file(message.channel, "subatomic.png")

    if message.content.lower().startswith("neutron"):
        await client.send_file(message.channel, "subatomic.png")
        await client.send_message(message.channel, "It has a quark formation of udd")

    if message.content.lower().startswith("proton"):
        await client.send_file(message.channel, "subatomic.png")
        await client.send_message(message.channel, "<@{}> The proton is the only stable hadron! It's quarks are uud".format(userID))

    if message.content.lower().startswith("isotope") or message.content.lower().startswith("isotopes"):
        await client.send_file(message.channel, "isotope.png")

    if message.content.lower().startswith("specific charge") or message.content.lower().startswith("sc"):
        await client.send_file(message.channel, "specificcharge.png")

    if message.content.lower().startswith("alpha"):
        await client.send_file(message.channel, "alpha.png")
        await client.send_file(message.channel, "alpha2.png")

    if message.content.lower().startswith("beta"):
        await client.send_file(message.channel, "beta-.png")
        await client.send_file(message.channel, "beta2-.png")
        await client.send_message(message.channel, "<@{}> The (anti)neutrino is there in order to conserve energy".format(userID))

    if message.content.lower().startswith("gamma"):
        await client.send_file(message.channel, "gamma.png")

    if message.content.lower().startswith("snf") or message.content.lower().startswith("strong nuclear force"):
        await client.send_file(message.channel, "snf1.png")
        await client.send_message(message.channel, "<@{}> The SNF overcomes the electrostatic force between the protons in the nucleus, it has a range of 0.5fm to 3fm in which it is attractive".format(userID))

    if message.content.lower().startswith("photon") or message.content.lower().startswith("photons"):
        await client.send_file(message.channel, "photon.png")
        await client.send_file(message.channel, "photon1.png")
        await client.send_file(message.channel, "photon2.png")
        await client.send_file(message.channel, "photon3.png")

    if message.content.lower().startswith("neutrino") or message.content.lower().startswith("antineutrino") or message.content.lower().startswith("neutrinos") or message.content.lower().startswith("antineutrinos"):
        await client.send_message(message.channel, "<@{}> The (anti)neutrino is important as it allows equations to follow the conservation of energy, the rest mass of a neutrino is 0 and so is its charge (There are different types of neutrinos as well!)".format(userID))

    if message.content.lower().startswith("electron capture"):
        await client.send_file(message.channel, "eCapture.png")

    if message.content.lower().startswith("wnf") or message.content.lower().startswith("weak nuclear force"):
        await client.send_file(message.channel, "wnf.png")

    if message.content.lower().startswith("lepton") or message.content.lower().startswith("leptons"):
        await client.send_file(message.channel, "lepton1.png")
        await client.send_message(message.channel, "<@{}> Leptons are fundamental particles, all leptons have a lepton number, here are a few of them")
        await client.send_file(message.channel, "lepton2.png")

    if message.content.lower().startswith("hadron") or message.content.lower().startswith("hadrons"):
        await client.send_file(message.channel, "hadron1.png")
        await client.send_file(message.channel, "hadron2.png")
        await client.send_message(message.channel, "Hadrons can be broken up into baryons and mesons (They're made up of quarks):")
        await client.send_file(message.channel, "hadron3.png")

    await client.process_commands(message)  #important

@client.command()
async def epic():
    facts = [
        'That is EPIC',
        'ok',
        'never'
    ]
    await client.say(random.choice(facts))

@client.command(name = 'say', 
                description = 'enter anything after say for the bot to say it for you')
async def say():
    print("say")



client.run(os.getenv('TOKEN'))
