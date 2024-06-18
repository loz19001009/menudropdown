import discord
from discord.ext import commands
import os

class DropdownMenu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label='Annie Hub V2', value='1'),
            discord.SelectOption(label='Aim For Solara', value='2'),
            discord.SelectOption(label='W-azure V2', value='3'),
            discord.SelectOption(label='Fries Hub', value='4'),
            discord.SelectOption(label='Xero Hub', value='5'),
            discord.SelectOption(label='Redz Hub', value='6'),
            discord.SelectOption(label='PowerBlack Hub', value='7'),
            discord.SelectOption(label='Zen Hub', value='8'),
            discord.SelectOption(label='Crazzy Hub', value='9'),
            discord.SelectOption(label='HoHo Hub', value='10'),
            discord.SelectOption(label='Neon Hub', value='11'),
            discord.SelectOption(label='Vector Hub', value='12'),
            discord.SelectOption(label='Faifao Hub New', value='13'),
            discord.SelectOption(label='OMG Hub', value='14'),
            discord.SelectOption(label='Min Gaming Hub', value='15'),
            discord.SelectOption(label='Doraemon Hub', value='16'),
            discord.SelectOption(label='MTrietHub Version 2', value='17'),
            discord.SelectOption(label='Maris Hub Main', value='18'),
            discord.SelectOption(label='Rinx Hub', value='19'),
            discord.SelectOption(label='Best Hub', value='20'),
            discord.SelectOption(label='Banana Hub Fake', value='21'),
            discord.SelectOption(label='Maris Auto Fruit (Blox Fruit)', value='22'),
            discord.SelectOption(label='Winter Hub V2', value='23'),
            discord.SelectOption(label='PerdLoader hub ( key )', value='24')
        ]
        super().__init__(placeholder='Chọn 1 script 🐔 !', options=options)

    async def callback(self, interaction: discord.Interaction):
        responses = {
            '1': '**Annie Hub V2 :**```loadstring(game:HttpGet(\'https://raw.githubusercontent.com/1st-Mars/Annie/main/1st.lua\'))()```',
            '2': '**Aim For Solara :**```loadstring(game:HttpGet(("https://raw.githubusercontent.com/Ownqa/Fixed/main/Solarus.lua"),true))()```',
            '3': '**W-azure V2 :**```getgenv().Team = "Pirates"\ngetgenv().AutoLoad = false --Will Load Script On Server Hop\ngetgenv().SlowLoadUi  = false\ngetgenv().ForceUseSilentAimDashModifier = false --Force turn on silent aim , if error then executor problem\ngetgenv().ForceUseWalkSpeedModifier = false --Force turn on Walk Speed Modifier , if error then executor problem\nloadstring(game:HttpGet("https://api.luarmor.net/files/v3/loaders/3b2169cf53bc6104dabe8e19562e5cc2.lua"))()```',
            '4': '**Fries Hub :**```loadstring(game:HttpGet(\'https://raw.githubusercontent.com/Frieshup/FriesHup/main/Update1\'))()```',
            '5': '**Xero Hub :**```getgenv().Team = "Marines" -- Pirates/Marines\n\ngetgenv().Fix_Lag = true -- true/false\n\nloadstring(game:HttpGet("https://xerohub.click/script/main.lua"))()```',
            '6': '**Redz Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/REDzHUB/BloxFruits/main/redz9999"))()```',
            '7': '**PowerBlack Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Powerblack09yt/Scripts/main/loader.lua"))()```',
            '8': '**Zen Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Zenhubtop/zen_hub_pr/main/zennewwwwui.lua", true))()```',
            '9': '**Crazzy Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/xSync-gg/Crazzy-Hub/main/V3"))()```',
            '10': '**HoHo Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/acsu123/HOHO_H/main/Loading_UI"))()```',
            '11': '**Neon Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/NIGHTHUBONTOP/Main/main/LoaderScript.lua"))()```',
            '12': '**Vector Hub :**```_G.Mode = "Eng" -- ไทย | Vn\nloadstring(game:HttpGet("https://raw.githubusercontent.com/AAwful/VectorHub/main/Loader.lua"))()```',
            '13': '**Faifao Hub New :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/KhanhTranVan/Guest/main/thankforbuying"))()```',
            '14': '**OMG Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Omgshit/Scripts/main/MainLoader.lua"))()```',
            '15': '**Min Gaming Hub :**```loadstring(game:HttpGet"https://github.com/Basicallyy/Basicallyy/raw/main/MinNew.lua")()```',
            '16': '**Doraemon Hub :**```loadstring(game:HttpGet(\'https://raw.githubusercontent.com/onepicesenpai/onepicesenpai/main/onichanokaka\'))()```',
            '17': '**MTrietHub Version 2 :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Minhtriettt/Free-Script/main/Main-V2.lua"))()```',
            '18': '**Maris Hub Main :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/marisdeptrai/Script-Free/main/Maris-Hub.lua"))()```',
            '19': '**Rinx Hub :**```_G.Language = "English"loadstring(game:HttpGetAsync\'https://shz.al/~RinXScript\')()```',
            '20': '**Best Hub :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/BestScriptEverr/Main-/main/Trezzyisbest", true))()```',
            '21': '**Banana Hub Fake :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Nghia11n/Banana-Hub/main/bananahub.lua"))()```',
            '22': '**Maris Auto Fruit (Blox Fruit) :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/marisdeptrai/Script-Free/main/FruitFinder.lua"))()```',
            '23': '**Winter Hub V2 :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/Yatsuraa/Yuri/main/Winterhub_V2.lua"))()```',
            '24': '**PerdLoader hub ( key ) :**```loadstring(game:HttpGet("https://raw.githubusercontent.com/PerdHub/Blosfruitscript/main/PerdLoader"))()```**Key Script :**```PERD-YOUD```',
        }
        response = responses.get(self.values[0], 'No response found for this option.')
        await interaction.response.send_message(response, ephemeral=True)

class MyBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')

bot = MyBot()

@bot.command()
async def script(ctx):
    view = discord.ui.View()
    view.add_item(DropdownMenu())

    embed = discord.Embed(
        title="Chọn 1 script !",
        description="Bot được tạo bởi Legend_august 🦅",
        color=discord.Color.green()
    )
    embed.set_image(url="https://www.icegif.com/wp-content/uploads/2023/06/icegif-776.gif")
    await ctx.send(embed=embed, view=view)

# Ensure to keep your bot token safe and not hardcode it in the script
TOKEN = os.getenv('TOKEN')
bot.run(TOKEN)
