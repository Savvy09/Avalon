import discord
from discord.ext import commands, tasks
from datetime import datetime
from datetime import timedelta
import os
import asyncio

intents = discord.Intents().all()
client = commands.Bot(command_prefix='a!', activity=discord.Activity(type=discord.ActivityType.listening, name="Savvy's orders"), intents=intents)
client.remove_command('help')
start_time = datetime.now()
SavvyID = 730271192778539078

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.command()
async def uptime(ctx):
    SavvyName = ctx.guild.get_member(SavvyID)
    delta_uptime = datetime.now() - start_time
    hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    embed = discord.Embed(
    title = '<a:NoTime:971005195888771092>  Bot Uptime',
    description = f"{days} days, {hours} hrs, {minutes} mins",
    color=0xFFDA00
    )

    embed.set_footer(text='Developed by Savvy#4334', icon_url=SavvyName.avatar.url)
    await ctx.send(embed=embed)

@client.command()
async def color(ctx):
  if ctx.message.author.id == SavvyID:
    embed = discord.Embed(
    title = 'Special colours for our special community!',
    description = "<:snowmanscream:964553792836231168> : <@&964556345841975416>\n<:deepocean:964553855750778950> : <@&964556464427532378>\n<:bubblegum:964553373145776189> : <@&964547418765021184>\n<:chiliflakes:964554276833734706> : <@&964556890883387432>\n<:sandstone:964554324854321212> : <@&964556956595544114>\n<:rosewood:964554221234040882> : <@&964556813292961823>\n<:lemonpie:964552127693352971> : <@&964546882548412467>\n<:nanshit:964554424552927352> : <@&964557089508827186>\n<:greentea:964553480046010369> : <@&964553015254216724>\n<:goldust:964553559179935744> : <@&964554796075986964>\n<:arcticice:964554165294628914> : <@&964556722746310706>\n<:lavender:964553419102777374> : <@&964552399240978577>\n<:midnight:964554759845593108> : <@&964557255397752923>\n<:flamingo:964554371234930708> : <@&964557029425430592>\n<:redwine:964554034214223972> : <@&964556567942946837>\n<:skyblue:964554109883654195> : <@&964556654035230781>\n<:bush:964554595772817448> : <@&964557148703064074>\n<:iris:964554655273193513> : <@&964557201224134776>",
    color=0xffffff
   )
 
    embed.set_footer(text='Avalon', icon_url='https://cdn.discordapp.com/icons/879753926981869568/a_005af94eb128aca4d5c9fb3e40f8e912.gif')
    embed.set_image(url='https://c.tenor.com/JFIE_HiM5ogAAAAC/rainbow-pride.gif')
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/840442785026146345/964583277606342676/unknown.png')
    embed.set_author(name='', icon_url='')
  
    await ctx.send(embed=embed)
  else:
    SavvyName = ctx.guild.get_member(SavvyID)
    embed2 = discord.Embed(
    title = '<a:_warn:971004404230668348>  Error!',
    description = 'This command can be used by bot developer only.',
    color=0xED4337
    )

    embed2.set_footer(text='Developed by Savvy#4334', icon_url=SavvyName.avatar.url)
    await ctx.send(embed=embed2)

@client.command()
async def say(ctx,*,args): 
    await ctx.send(args)

@client.command()
async def dump(ctx,channelid: int,*,args):
    channel = client.get_channel(channelid)
    await channel.send(args)

@client.command()
async def ping(ctx):
    await ctx.send(f"**HA! I don't say pong** :sunglasses:**. Ping is** {round(client.latency * 1000)}ms")
  
@client.command(name="getuser")  
async def getuser(ctx, userId):
  member = ctx.guild.get_member(int(userId))
  await ctx.message.reply(f"Don't test me, it's {member}")

@client.command()
@commands.has_permissions(manage_roles=True)
async def karudono(ctx, member: discord.Member):
  guild = client.get_guild(879753926981869568)
  donator_role_id = 900312241516204062
  donator_role = None
  for role in guild.roles:
    if role.id == donator_role_id:
      donator_role = role
      if donator_role in member.roles:
        await ctx.message.reply(f"Are you fucking dumb you stupid the user already has {donator_role} role. <:av_mikerr:901722957427146762>")
      else:
        channel2 = client.get_channel(965281684784291901)
        msg1 = await channel2.fetch_message(977954392022085634)
        await member.add_roles(donator_role)
        SavvyName = ctx.guild.get_member(SavvyID)
        embed2 = discord.Embed(
        title = f":white_check_mark: _**Gave {member} {donator_role} role.**_",
    color=0x62BD69
    )

        embed2.set_footer(text='Developed by Savvy#4334', icon_url=SavvyName.avatar.url)
        await ctx.send(embed=embed2)
        logmsg = msg1.content
        logmsg2 = f"\n{member.id} {datetime.now().date() + timedelta(days=30)}"
        logmsg3 = logmsg + f"\n{member.id} {datetime.now().date() + timedelta(days=30)}"
        if logmsg == "ok":
          await msg1.edit(content=logmsg2)
        else:
          await msg1.edit(content=logmsg3)

@karudono.error
async def donorole_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.message.reply('I see you naughty one, but unfortunately this command requires you to have **Manage Roles** permission')
  
@client.event
async def on_message_edit(message_before, message_after):
  author = message_before.author
  guild = message_before.guild
  channel = message_before.channel
  description = None
  if author.id == 646937666251915264:
    for embed in message_after.embeds:
                            embedInfo = (embed.to_dict())
                            if 'description' in embedInfo:
                              description = embedInfo['description']
    if description and "The contribution has been made!" in description:
       donator_role_id = 900312241516204062
       donator_role = None
       for role in guild.roles:
         if role.id == donator_role_id:
             donator_role = role
       print("Donator role is: ", donator_role)

       description = embedInfo["description"]
       first_part_description = description[ 0 : description.find("contribute") ]
       userId = ""
       for char in first_part_description:
          if char.isdigit():
            userId += char
       print("userId is: ", userId)

       description = embedInfo["description"]
       second_part_description = description[ description.find("`") : description.find("gems") ]
       amount = ""
       for char in second_part_description:
          if char.isdigit():
            amount += char
       print("amount is: ", amount)
       gemAmountInteger = int(amount)
       userIdInteger = int(userId)
       if gemAmountInteger > 0:
          member_to_add = guild.get_member(userIdInteger)
          if donator_role in member_to_add.roles:
            await channel.send(f"You already have {donator_role} role, donating gems despite having the role **won't increase your role duration.**\n_Your role will expire after 1 month of first donation_.")
          else:
            channel2 = client.get_channel(965281684784291901)
            msg1 = await channel2.fetch_message(977954392022085634)
            await member_to_add.add_roles(donator_role)
            await channel.send(f"Thank you for your friendly, dependable service through every season <@{member_to_add.id}>!! You hereby recieve the {donator_role} role.\n_It will expire on_ **{datetime.now().date() + timedelta(days=30)}**.")
            logmsg = msg1.content
            logmsg2 = f"\n{member_to_add.id} {datetime.now().date() + timedelta(days=30)}"
            logmsg3 = logmsg + f"\n{member_to_add.id} {datetime.now().date() + timedelta(days=30)}"
            if logmsg == "ok":
              await msg1.edit(content=logmsg2)
            else:
              await msg1.edit(content=logmsg3)

@tasks.loop(seconds=7200)
async def background_loop():
    await client.wait_until_ready()
    channel2 = client.get_channel(965281684784291901)
    msg1 = await channel2.fetch_message(977954392022085634)
    m1 = str(msg1.content)
    if m1 == "ok":
      print("No logs yet :(")
    else:
     division = list(x.split() for x in m1.splitlines())
     expired_lines = 0
     for pair in division:
      userId = pair[0]
      date_time_str = pair[1]
      end_date_obj = datetime.strptime(date_time_str, '%Y-%m-%d')
      if end_date_obj < datetime.now():
         guild = client.get_guild(879753926981869568)
         expired_lines += 1
         new_log = "\n".join(m1.split("\n")[expired_lines:])
         member_to_remove_id = int(userId)
         member_to_remove = guild.get_member(member_to_remove_id)
         donator_role_id = 900312241516204062
         donator_role = None
         for role in guild.roles:
           if role.id == donator_role_id:
             donator_role = role
             await member_to_remove.remove_roles(donator_role)
             print("Time's up!\nRemoved role from: ", member_to_remove)
             if len(new_log) == 0:
               await msg1.edit(content="ok")
             else:
               await msg1.edit(content=new_log)
             
async def main():
   async with client:
       background_loop.start()
       await client.start(os.getenv('token'))

asyncio.run(main())
