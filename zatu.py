import discord
import ast
import datetime
import re
import time
import asyncio
import random
import json
import os
from discord.ext import commands,tasks

client = commands.Bot(command_prefix="ge!")

token = "NzA3MTI0OTU4NDUwNjc5OTQw.XrZOzw.UToflt_eDGt0cXq0BXrbNinD7Xw"

admin = [684010765979877376,642294528916586507,386369883190984706,381354474457006091]

@client.command()
async def say(ctx, *, text):
  if ctx.author.id in admin:
      await ctx.send(text)

client.run(token, bot=False)
