import discord
import asyncio
import nest_asyncio

nest_asyncio.apply()

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)

        self.bg_task = self.loop.create_task(self.my_background_task())

    async def my_background_task(self):
       
        channel = self.get_channel(Chanel_ID) #Target Chanel ID

        while not self.is_closed():           
            await channel.send("This message is sending every 5 seconds")
            await asyncio.sleep(5) #How often message will be sent
            
client = MyClient()
client.run("", bot =False) #Your Self Token
