import discord
import pymysql.cursors
import datetime

connection = pymysql.connect(
    host='db',
    user='debuger',
    password='password',
    database='servercoins',
    cursorclass=pymysql.cursors.DictCursor
)

intents = discord.Intents.all()
client = discord.Client(intents=intents)

chList = {
    'welcome': 918485500766068769
}

def search(userid):
    try:
        with connection.cursor() as cursor:
            sql = "select * from `User` where `user_id` = %s"
            cursor.execute(sql, userid)
            connection.commit()

    finally:
        cursor.close()

    return cursor.fetchall()


def InsertUser(username, userid, role):
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `User` (`user_name`, `user_id`, `role`) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, userid, role))
            connection.commit()
    except pymysql.err.IntegrityError:
        pass
    finally:
        cursor.close()


def proposal_point(userid):
    user = search(userid)

    try:
        with connection.cursor() as cursor:
            sql = "UPDATE `User` SET `coin`=`coin`-10 where user_id = %s"
            cursor.execute(sql, int(user[0]['user_id']))
            connection.commit()

    finally:
        cursor.close()


def proposal(userid, event):
    user = search(userid)

    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `Proposal` (`time`, `user_name`, `user_id`, `event`) VALUES ({}, `{}`, {}, `{}`)".format(datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'), user[0]['user_name'], int(user[0]['user_id']), event)
            cursor.execute(sql)
    finally:
        cursor.close()


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')


@client.event
async def on_member_join(member):
    channel = client.get_channel(chList['welcome'])
    InsertUser(member.name, member.id, member.roles)
    await channel.send(f'Hi!{member.mention}. Thank you come here!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    member = message.author
    messagelist = message.content.split()

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if len(messagelist) > 1:
        if message.content.startswith('$proposal'):
            proposal_point(member.id)
            proposal(member.id, messagelist[1])



@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message



client.run('')
