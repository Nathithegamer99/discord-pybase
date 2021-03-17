import discord
from discord.ext import commands
import random
from discord import Color as c

teal = c.teal()
magenta = c.magenta() #choose any colour, but be mindful of the discord.Color colours, they are wierd, unless you go with a custom RGB "system"

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(color = magenta)
        em.add_field(name='info', value='for information about the server, head over to #・info !', inline=False)
        em.add_field(name='Socials', value='Socials Medias For, lycolt.' , inline=False)
        em.add_field(name='Commands', value='Run l.commands for a list of categories.', inline=False)
        em.set_footer(text='Man, embeds are so cool.')
        await ctx.send(embed=em)

print('LOADED')



def setup(client):
    client.add_cog(Help(client))
