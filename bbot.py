import discord
import asyncio
import sqlite3
import json
from discord.ext import commands

client = commands.Bot(command_prefix="/")

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)


@client.command()
async def hosgeldin_kanal_ayarla(mesaj, kanal: discord.TextChannel):
    guildid = mesaj.guild.id
    if mesaj.author.guild_permissions.administrator:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM welcome WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        d = []
        if data == d:
            con2 = sqlite3.connect("data.db")
            cursor2 = con2.cursor()
            cursor2.execute(
                f"INSERT INTO welcome VALUES ({guildid},'{mesaj.guild.name}', 1, {kanal.id})")
            con2.commit()
            con2.close()
            await mesaj.send("Hoşgeldin-gülegüle kanalı başarıyla ayarlandı.")
        else:
            await mesaj.send("Bu komut zaten ayarlanmış. Silmek için: hosgeldin_kanal_sil")
    else:
        await mesaj.send("Yetkiniz Yok")

@client.command()
async def hosgeldin_kanal_sil(mesaj):
    guildid = mesaj.guild.id
    if mesaj.author.guild_permissions.administrator:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM welcome WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        d = []
        if data == d:
            await mesaj.send("Bu komut zaten kapalı.")
        else:
            con9 = sqlite3.connect("data.db")
            cursor9 = con9.cursor()
            cursor9.execute(f"DELETE  FROM welcome WHERE sunucuid = {guildid}")
            con9.commit()
            con9.close()
            await mesaj.send("Hoşgeldin-gülegüle kanalı başarıyla kaldırıldı.")
    else:
        await mesaj.send("Yetkiniz Yok")

@client.command()
async def log_kanal_ayarla(mesaj, kanal: discord.TextChannel):
    guildid = mesaj.guild.id
    if mesaj.author.guild_permissions.administrator:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        d = []
        if data == d:
            con2 = sqlite3.connect("data.db")
            cursor2 = con2.cursor()
            cursor2.execute(
                f"INSERT INTO log VALUES ({guildid},'{mesaj.guild.name}', 1, {kanal.id})")
            con2.commit()
            con2.close()
            await mesaj.send("log kanalı başarıyla ayarlandı.")
        else:
            await mesaj.send("Bu komut zaten ayarlanmış. Silmek için: log_kanal_sil")
    else:
        await mesaj.send("Yetkiniz Yok")

@client.command()
async def log_kanal_sil(mesaj):
    guildid = mesaj.guild.id
    if mesaj.author.guild_permissions.administrator:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        d = []
        if data == d:
            await mesaj.send("Bu komut zaten kapalı.")
        else:
            con9 = sqlite3.connect("data.db")
            cursor9 = con9.cursor()
            cursor9.execute(f"DELETE  FROM log WHERE sunucuid = {guildid}")
            con9.commit()
            con9.close()
            await mesaj.send("log kanalı başarıyla kaldırıldı.")
    else:
        await mesaj.send("Yetkiniz Yok")

client.run("Instert your token")
