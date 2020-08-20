#!/usr/bin/env python3

import discord
import board
import neopixel
import asyncio
import logging
import time
from discord.ext import commands
from discord import User
from discord import Member
from discord import VoiceState
from math import *
from time import sleep


pixels = neopixel.NeoPixel(board.D18, num_of_leds, brightness =0.8)

client = discord.Client()

@client.event
async def on_ready():
    countAndShowLeds()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_voice_state_update(member,before,after):
#Name of User
    if member.id == UserID:  #Copy and paste Users ID
        if before.channel is None and after.channel is not None:
            if after.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} joined {}.".format(member.display_name, after.channel))
                pixels[SetPixelNumberHere] = (x, x , x)  #Enter PixelNumber and Set RGB Color Code
        if before.channel is not None and after.channel is None:
            if before.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} has left {}.".format(member.display_name, before.channel))
                pixels[SetPixelNumberHere] = (0, 0, 0)  #Enter Same PixelNumber


#Name of User2
    if member.id == UserID:  #Copy and paste Users ID
        if before.channel is None and after.channel is not None:
            if after.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} joined {}.".format(member.display_name, after.channel))
                pixels[SetPixelNumberHere] = (x, x , x)  #Enter PixelNumber and Set RGB Color Code
        if before.channel is not None and after.channel is None:
            if before.channel.id == VoiceChannelID:  #Copy and paste VoiceChannelID
                print("{} has left {}.".format(member.display_name, before.channel))
                pixels[SetPixelNumberHere] = (0, 0, 0)  #Enter Same PixelNumber

client.run("BOT TOKEN HERE")  #Enter BOT TOKEN                
