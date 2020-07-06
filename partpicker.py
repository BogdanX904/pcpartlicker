import requests
from bs4 import BeautifulSoup
import discord
from collections import Counter
from itertools import tee, count


def uniquify(seq, suffs = count(1)):
    """Make all the items unique by adding a suffix (1, 2, etc).

    `seq` is mutable sequence of strings.
    `suffs` is an optional alternative suffix iterable.
    """
    not_unique = [k for k,v in Counter(seq).items() if v>1] # so we have: ['name', 'zip']
    # suffix generator dict - e.g., {'name': <my_gen>, 'zip': <my_gen>}
    suff_gens = dict(zip(not_unique, tee(suffs, len(not_unique))))
    for idx,s in enumerate(seq):
        try:
            suffix = str(next(suff_gens[s]))
        except KeyError:
            # s was unique
            continue
        else:
            seq[idx] += suffix


def pick_parts(url):
    global final_message
    page = requests.get(url)
    note = "Note: The following custom part link was user-provided. PCPartPicker cannot vouch for its validity or safety. If you follow this link, you are doing so at your own risk."
    note2 = "Note: The following custom part link was user-provided. PCPartPicker cannot vouch for its validity or safety. If you follow this link, you are doing so at your own risk.\nLoading..."
    soup = BeautifulSoup(page.content, "html.parser")

    components = soup.find_all(class_="td__component")
    component_names = soup.find_all(class_="td__name")
    prices = soup.find_all(class_="td__price")
    items = []
    names= []
    custom = []
    prices = []
    for component in components:
        comp = component.text.strip("\n")
        if "custom" in comp.lower():
            custom.append(comp)
        else:
            items.append(comp)
    for name in component_names:
        comp_name = name.text.strip("\n")
        names.append(comp_name)

    uniquify(custom)
    for x in custom:
        items.append(x)

    for x in names:
        if note2 in x:
            new_set = x.replace(note2, "")
            names.pop(-1)
            names.append(new_set)

    parts = dict(zip(items, names))

    message = ""
    embed = discord.Embed(colour=discord.Colour.from_rgb(232, 169, 32), title="PCPartPicker List", url=url)
    for key, value in parts.items():
        if "custom" in key.lower():
            embed.add_field(name="Custom", value=value, inline=False)
        else:
            embed.add_field(name=key, value=value, inline=False)
            # message = message +  f"{key}: {value}\n"
    """if note in message:
        new_message = message.replace(note, "")
        if "Loading" in message:
            final_message = new_message.replace("Loading...", "")
        else:
            final_message = new_message"""
    return embed
