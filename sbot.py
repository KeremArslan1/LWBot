# By KB (A.RP Kerem#7777)
import discord
import asyncio
import sqlite3

intents = discord.Intents(members=True, messages=True, emojis=True, guilds=True, bans=True)
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)


@client.event
async def on_message_edit(before, after):
    kanall = await client.fetch_channel(before.channel.id)
    guildid = kanall.guild.id
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Mesaj Editlendi", color=0x00c6e0)
            embed.add_field(name="Düzenleyen: ", value=before.author.name, inline=False)
            embed.add_field(name="Önceki mesaj: ", value=before.content, inline=False)
            embed.add_field(name="Sonraki mesaj: ", value=after.content, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_message_delete(message):
    kanall = await client.fetch_channel(message.channel.id)
    guildid = kanall.guild.id
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Mesaj Silindi", color=0x00c6e0)
            embed.add_field(name="Mesaj Sahibi: ", value=message.author.name, inline=False)
            embed.add_field(name="Kanal: ", value=kanall.name, inline=False)
            embed.add_field(name="Mesaj İçeriği: ", value=message.content, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_emojis_update(guild, before, after):
    print("dadasdasdas")
    print(after)
    print(guild.id)
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        sayi = 0
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Sunucu emojileri güncellendi.", color=0x00c6e0)
            for i in after:
                sayi += 1
                embed.add_field(name=f"{sayi}.Emoji: ", value=client.get_emoji(id=i.id), inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_role_create(role):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(role.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            if role.hoist:
                ayrimi = "Evet"
            else:
                ayrimi = "Hayır"
            if role.mentionable:
                bahs = "Evet"
            else:
                bahs = "Hayır"
            embed = discord.Embed(title="Yeni Rol Oluşturuldu", color=0x00c6e0)
            embed.add_field(name=f"Rol adı: ", value=role.name, inline=False)
            embed.add_field(name=f"Rol id: ", value=role.id, inline=False)
            embed.add_field(name=f"Rol diğer kişilerden ayrı gösteriliyor mu: ", value=ayrimi, inline=False)
            embed.add_field(name=f"Hekes bu rolden bahsedebilir mi: ", value=bahs, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_role_delete(role):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(role.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            if role.hoist:
                ayrimi = "Evet"
            else:
                ayrimi = "Hayır"
            if role.mentionable:
                bahs = "Evet"
            else:
                bahs = "Hayır"
            embed = discord.Embed(title="Rol Silindi", color=0x00c6e0)
            embed.add_field(name=f"Rol adı: ", value=role.name, inline=False)
            embed.add_field(name=f"Rol id: ", value=role.id, inline=False)
            embed.add_field(name=f"Rol diğer kişilerden ayrı gösteriliyor muydu: ", value=ayrimi, inline=False)
            embed.add_field(name=f"Hekes bu rolden bahsedebilir miydi: ", value=bahs, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_role_update(before, after):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(before.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            if before.hoist:
                ayrimib = "Evet"
            else:
                ayrimib = "Hayır"
            if after.hoist:
                ayrimia = "Evet"
            else:
                ayrimia = "Hayır"
            if after.mentionable:
                bahsa = "Evet"
            else:
                bahsa = "Hayır"
            if before.mentionable:
                bahsb = "Evet"
            else:
                bahsb = "Hayır"
            embed = discord.Embed(title="Rol Güncellendi", color=0x00c6e0)
            embed.add_field(name=f"Rol id: ", value=before.id, inline=False)
            embed.add_field(name=f"Eski rol adı: ", value=before.name, inline=False)
            embed.add_field(name=f"Yeni rol adı: ", value=before.name, inline=False)
            embed.add_field(name=f"Eskiden rol diğer kişilerden ayrı gösteriliyor muydu: ", value=ayrimib, inline=False)
            embed.add_field(name=f"Şuan rol diğer kişilerden ayrı gösteriliyor mu: ", value=ayrimia, inline=False)
            embed.add_field(name=f"Eskiden hekes bu rolden bahsedebilir miydi: ", value=bahsb, inline=False)
            embed.add_field(name=f"Şimdi hekes bu rolden bahsedebilir mi: ", value=bahsa, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_channel_create(channel):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(channel.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Yeni Kanal Oluşturuldu", color=0x00c6e0)
            embed.add_field(name=f"Kanal id: ", value=channel.id, inline=False)
            embed.add_field(name=f"Kanal adı: ", value=channel.name, inline=False)
            embed.add_field(name=f"Kanal kategorisi: ", value=channel.category, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_channel_delete(channel):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(channel.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Kanal Silindi", color=0x00c6e0)
            embed.add_field(name=f"Kanal id: ", value=channel.id, inline=False)
            embed.add_field(name=f"Kanal adı: ", value=channel.name, inline=False)
            embed.add_field(name=f"Kanal kategorisi(silinmeden): ", value=channel.category, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_guild_channel_update(before, after):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(before.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Kanal Güncellendi", color=0x00c6e0)
            embed.add_field(name=f"Kanal id: ", value=before.id, inline=False)
            embed.add_field(name=f"Eski kanal adı: ", value=before.name, inline=False)
            embed.add_field(name=f"Eski kanal kategorisi: ", value=before.category, inline=False)
            embed.add_field(name=f"Yeni kanal adı: ", value=after.name, inline=False)
            embed.add_field(name=f"Yeni kanal kategorisi: ", value=after.category, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_member_ban(guild, user):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Kullanıcı Banlandı", color=0x00c6e0)
            embed.add_field(name=f"Kullanıcı adı: ", value=user.name, inline=False)
            embed.add_field(name=f"Kullanıcı id: ", value=user.id, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass


@client.event
async def on_member_unban(guild, user):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Kullanıcının banı kaldırıldı", color=0x00c6e0)
            embed.add_field(name=f"Kullanıcı adı: ", value=user.name, inline=False)
            embed.add_field(name=f"Kullanıcı id: ", value=user.id, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass

@client.event
async def on_member_update(before, after):
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM log WHERE sunucuid = {int(before.guild.id)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            embed = discord.Embed(title="Kullanıcı Güncellendi", color=0x00c6e0)
            embed.add_field(name=f"Kullanıcı id: ", value=before.id, inline=False)
            embed.add_field(name=f"Eski kullanıcı adı: ", value=before.name, inline=False)
            embed.add_field(name=f"Yeni kullanıcı adı: ", value=after.name, inline=False)
            embed.add_field(name=f"Eski kullanıcı nicki: ", value=before.nick, inline=False)
            embed.add_field(name=f"Yeni kullanıcı nicki: ", value=after.nick, inline=False)
            embed.add_field(name=f"Eski kullanıcı avatarı: ", value=before.avatar_url, inline=False)
            embed.add_field(name=f"Yeni kullanıcı avatarı: ", value=after.avatar_url, inline=False)
            await kanal.send(embed=embed)
        else:
            pass
    except:
        pass

@client.event
async def on_member_join(member):
    guildid = member.guild.id
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM welcome WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            await kanal.send(f"Aramıza hoşgeldin dostum <@{member.id}>")
        else:
            pass
    except:
        pass


@client.event
async def on_member_remove(member):
    guildid = member.guild.id
    try:
        con = sqlite3.connect("data.db")
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM welcome WHERE sunucuid = {int(guildid)}")
        data = cursor.fetchall()
        con.close()
        data = data[0]
        sunucuiddb = int(data[0])
        durumdb = int(data[2])
        kanaliddb = int(data[3])
        if durumdb == 1:
            kanal = await client.fetch_channel(kanaliddb)
            await kanal.send(f"Gitmene üzüldük dostum {member.name}")
        else:
            pass
    except:
        pass

client.run("Instert your token")
