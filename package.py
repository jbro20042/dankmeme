@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith("%ping"):
        await client.send_message(message.channel, "Pong!")
    elif message.content.startswith("%ching"):
        await client.send_message(message.channel, "chong!")
    elif message.content.startswith("%help me"):
        await client.send_message(message.channel, "with what?")
    elif message.content.startswith("%sing me a song"):
        await client.send_message(message.channel, "ok. my poo is yum when i drink it with pee it is so tasty as wee wee wee!")
    elif message.content.startswith("%how old are you"):
        await client.send_message(message.channel, "i think about 69 billion years old or around that.")
    elif message.content.startswith("%whats your favourite food"):
        await client.send_message(message.channel, "hmmm i need to think??? maybe fried chicken from kfc thats the best")
    elif message.content.startswith("%bye"):
        await client.send_message(message.channel, "where are you going")
    elif message.content.startswith("%i need to go"):
        await client.send_message(message.channel, "nawwww ok bye bye")
    elif message.content.startswith("%is jbro sexy"):
        await client.send_message(message.channel, "God damn yes!")
client.run("NDEwNzE5MDY1MDExNzgxNjMy.DVxVVw.eP0CrD8U0CaHyjgxoWjy166n9Ws")

