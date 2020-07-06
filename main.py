import discord
from discord.ext import commands
import asyncio
import requests
from bs4 import BeautifulSoup
from partpicker import pick_parts
import re
import json


bot = commands.Bot(command_prefix=">", help_command=None)
bot.owner_ids = [287256464047865857, 405798011172814868]
links = ["https://pcpartpicker.com/list/", "https://uk.pcpartpicker.com/list/", "https://de.pcpartpicker.com/list/"]
url = ""


@bot.event
async def on_ready():
    print("Bot is online.")


@bot.event
async def on_message(message: discord.Message):
    if ">" in message.content:
        pass
    else:
        if not message.author.id == 729059784179056721:
            try:
                match = re.findall("[pcpartpicker]", message.content)
                if match and "list" in message.content:
                    link = message.content
                    msg = pick_parts(link)
                    await message.channel.send(embed=msg)
            except requests.exceptions.MissingSchema:
                pass
    await bot.process_commands(message)

supers = ["super", "s"]


@bot.command(aliases = ["h"])
async def help(ctx):
    help_message = discord.Embed(title="Commands", description="Bot prefix is `>`.", colour=discord.Colour.from_rgb(232, 169, 32))
    help_message.add_field(name="**recommend**", value="Aliases: r, recommended, recommendations.\nUsage: >r `[GPU Model]`", inline=False)
    help_message.add_field(name="**append**", value="Alias: a.\nUsage: >a `[GPU Model]` `[Name]` `[URL]`.\n*Bot owners only.*", inline=False)
    help_message.add_field(name="**delete**", value="Aliases: del, remove.\nUsage: >del `[GPU Model]` `[Name]`.\n*Bot owners only.*", inline=False)
    #help_message.add_field(name="", value="", inline=False)
    await ctx.send(embed=help_message)


@bot.command(aliases=["r", "recommended", "recommendations"])
async def recommend(ctx, *, message:str):
    if "5600" in message.lower():
        with open("rx5600xt.json", "r") as f:
            gpu = json.load(f)
        gpu_embed = discord.Embed(title="RX 5600 XT", description="If any of these items are out of stock, choose the next item in the list.")
        for k,v in gpu.items():
            gpu_embed.add_field(name=k, value=f"[Buy]({v})", inline=False)
        await ctx.send(embed=gpu_embed)
    elif "5700" and "xt" in message.lower():
        with open("rx5700xt.json", "r") as f:
            gpu = json.load(f)
        gpu_embed = discord.Embed(title="RX 5700 XT",
                                       description="If any of these items are out of stock, choose the next item in the list.")
        for k, v in gpu.items():
            gpu_embed.add_field(name=k, value=f"[Buy]({v})", inline=False)
        await ctx.send(embed=gpu_embed)
    elif "1600" and any(super in message.lower() for super in supers):
        with open("gtx1660s.json", "r") as f:
           gpu = json.load(f)
        gpu_embed = discord.Embed(title="GTX 1660 Super",
                                       description="If any of these items are out of stock, choose the next item in the list.")
        for k, v in gpu.items():
            gpu_embed.add_field(name=k, value=f"[Buy]({v})", inline=False)
        await ctx.send(embed=gpu_embed)
    elif "5700" in message.lower():
        with open("rx5700.json", "r") as f:
           gpu = json.load(f)
        gpu_embed = discord.Embed(title="RX 5700",
                                       description="If any of these items are out of stock, choose the next item in the list.")
        for k, v in gpu.items():
            gpu_embed.add_field(name=k, value=f"[Buy]({v})", inline=False)
        await ctx.send(embed=gpu_embed)
    elif "580" in message.lower():
        with open("rx580.json", "r") as f:
           gpu = json.load(f)
        gpu_embed = discord.Embed(title="RX 580",
                                       description="If any of these items are out of stock, choose the next item in the list.")
        gpu_embed.set_footer(text="Any XFX RX 580 variant is good, with the 8GB models being the best.")
        for k, v in gpu.items():
            gpu_embed.add_field(name=k, value=f"[Buy]({v})", inline=False)
        await ctx.send(embed=gpu_embed)
    else:
        await ctx.send("You need to specify a GPU model!")


@bot.command(aliases = ["a"])
async def append(ctx, message:str, name:str, link:str):
    if ctx.message.author.id in bot.owner_ids:
        if "5600" in message.lower():
            with open("rx5600xt.json", "r") as f:
                gpu = json.load(f)
            gpu.update({name: link})
            with open("rx5600xt.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done.")
        elif "5700" and "xt" in message.lower():
            with open("rx5700xt.json", "r") as f:
                gpu = json.load(f)
            gpu.update({name: link})
            with open("rx5700xt.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done.")
        elif "1660" and any(super in message.lower() for super in supers):
            with open("gtx1660s.json", "r") as f:
                gpu = json.load(f)
            gpu.update({name: link})
            with open("gtx1660s.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done.")
        elif "5700" in message.lower():
            with open("rx5700.json", "r") as f:
                gpu = json.load(f)
            gpu.update({name: link})
            with open("rx5700.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done.")
        elif "580" in message.lower():
            with open("rx580.json", "r") as f:
                gpu = json.load(f)
            gpu.update({name: link})
            with open("rx580.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done.")
        else:
            await ctx.send("You need to specify a GPU model!")
    else:
        await ctx.send("You don't have permission to use that command!")


@bot.command(aliases = ["del", "remove"])
async def delete(ctx,message:str, name:str):
    if ctx.message.author.id in bot.owner_ids:
        if "5600" in message.lower():
            with open("rx5600xt.json", "r") as f:
                gpu = json.load(f)
            gpu.pop(name)
            with open("rx5600xt.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done")
        elif "5700" and "xt" in message.lower():
            with open("rx5700xt.json", "r") as f:
                gpu = json.load(f)
            gpu.pop(name)
            with open("rx5700xt.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done")
        elif "5700" in message.lower():
            with open("rx5700.json", "r") as f:
                gpu = json.load(f)
            gpu.pop(name)
            with open("rx5700.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done")
        elif "580" in message.lower():
            with open("rx580.json", "r") as f:
                gpu = json.load(f)
            gpu.pop(name)
            with open("rx580.json", "w") as f:
                json.dump(gpu, f)
            await ctx.send("Done")
        else:
            await ctx.send("You need to specify a GPU model!")
    else:
        await ctx.send("You don't have permission to use that command!")

bot.run("TOKEN")
