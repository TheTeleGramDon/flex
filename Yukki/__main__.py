import asyncio
import importlib
import os
import re
import random

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytgcalls import idle
from rich.console import Console
from rich.table import Table
from youtubesearchpython import VideosSearch

from config import (LOG_GROUP_ID, LOG_SESSION, STRING1, STRING2, STRING3,
                    STRING4, STRING5)
from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, BOT_ID, BOT_NAME, LOG_CLIENT,
                   OWNER_ID, app)
from Yukki.Core.Clients.cli import LOG_CLIENT
from Yukki.Core.PyTgCalls.Yukki import (pytgcalls1, pytgcalls2, pytgcalls3,
                                        pytgcalls4, pytgcalls5)
from Yukki.Database import (get_active_chats, get_active_video_chats,
                            get_sudoers, is_on_off, remove_active_chat,
                            remove_active_video_chat)
from Yukki.Inline import private_panel
from Yukki.Plugins import ALL_MODULES
from Yukki.Utilities.inline import paginate_modules

loop = asyncio.get_event_loop()
console = Console()
HELPABLE = {}
HOTTIE_IMG = random.choice(HOTTIE)
HOTTIE = (
      "https://telegra.ph/file/dfb3f645a161318015b31.jpg",
      "https://telegra.ph/file/0233572f88b43c172be6b.jpg",
      "https://telegra.ph/file/4718ea5902ed433f9cf38.jpg",
      "https://telegra.ph/file/4d1ddeb0d63f54a8dce29.jpg",
      "https://telegra.ph/file/97300050457226a824628.jpg",
      "https://telegra.ph/file/90f945c6e3c4a5e2cb863.jpg",
      "https://telegra.ph/file/c19d18bea30a222a4ceac.jpg",
      "https://telegra.ph/file/1f8f6bd142fd4b104dc95.jpg",
      "https://telegra.ph/file/4fc91fd4a1ac4d25a2a1b.jpg",
      "https://telegra.ph/file/9332b113ddb8555bf6ffe.jpg",
      "https://telegra.ph/file/fbc20e462231564a7407f.jpg",
      "https://telegra.ph/file/45df1a2dcf2e385d5cb7b.jpg",
      "https://telegra.ph/file/89e069ddc5c581a3501ef.jpg",
      "https://telegra.ph/file/2d75f08b6da4ac453a500.jpg",
      "https://telegra.ph/file/4b8a6352daa4597e5b507.jpg",
      "https://telegra.ph/file/4ffaff9bb7f3d7818ef21.jpg",
      "https://telegra.ph/file/a62f6de763dbb2b32dace.jpg",
      "https://telegra.ph/file/7c5715131dd0f188e1582.jpg",
      "https://telegra.ph/file/5f8e2c2e0147d8ec4fa86.jpg",
      "https://telegra.ph/file/30dd0b041aaff87826264.jpg",
      "https://telegra.ph/file/9b9de1bd73e482e45d47e.jpg",
      "https://telegra.ph/file/6a1a542b0846bae071a15.jpg",
      "https://telegra.ph/file/6fa7b00d49c8db42f2bb1.jpg",
      "https://telegra.ph/file/f3e0cedf92b3f234cd84f.jpg",
      "https://telegra.ph/file/60998d8f5520b95aec7f9.jpg",
      "https://telegra.ph/file/2d9f1eb3c8ae1980bf9f6.jpg",
      "https://telegra.ph/file/f830ea186d932a076719a.jpg",
      "https://telegra.ph/file/0cde16e55a50dd22715cd.jpg",
      "https://telegra.ph/file/74fc9c85fd341157fee1c.jpg",
      "https://telegra.ph/file/dd8b72e3976d1fd35615a.jpg",
      "https://telegra.ph/file/1b81b3ff11c45e4e31358.jpg",
      "https://telegra.ph/file/be4e82ab2b9de9cb97fb0.jpg",
      "https://telegra.ph/file/58b3cdf9203431ecfce2a.jpg",
      "https://telegra.ph/file/2fb2fefda863a096b0e42.jpg"
)
async def initiate_bot():
    with console.status(
        "[magenta] Finalizing Booting...",
    ) as status:
        try:
            chats = await get_active_video_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_video_chat(chat_id)
        except Exception as e:
            pass
        try:
            chats = await get_active_chats()
            for chat in chats:
                chat_id = int(chat["chat_id"])
                await remove_active_chat(chat_id)
        except Exception as e:
            pass
        status.update(
            status="[bold blue]Scanning for Plugins", spinner="earth"
        )
        console.print("Found {} Plugins".format(len(ALL_MODULES)) + "\n")
        status.update(
            status="[bold red]Importing Plugins...",
            spinner="bouncingBall",
            spinner_style="yellow",
        )
        for all_module in ALL_MODULES:
            imported_module = importlib.import_module(
                "Yukki.Plugins." + all_module
            )
            if (
                hasattr(imported_module, "__MODULE__")
                and imported_module.__MODULE__
            ):
                imported_module.__MODULE__ = imported_module.__MODULE__
                if (
                    hasattr(imported_module, "__HELP__")
                    and imported_module.__HELP__
                ):
                    HELPABLE[
                        imported_module.__MODULE__.lower()
                    ] = imported_module
            console.print(
                f">> [bold cyan]Successfully imported: [green]{all_module}.py"
            )
        console.print("")
        status.update(
            status="[bold blue]Importation Completed!",
        )
    console.print(
        "[bold green]Congrats!! Yukki Music Bot has started successfully!\n"
    )
    try:
        await app.send_message(
            LOG_GROUP_ID,
            random.choice(HOTTIE), caption="<b>Hottie Has been Started! Working Fine For Status, Click /start And /help For More Info.</b>",
            reply_markup=InlineKeyboardMarkup(
                [
                  [                  
                       InlineKeyboardButton(
                             text="[► Summon Me ◄]",
                             url=f"https://t.me/Hottie_Robot?startgroup=true")
                     ] 
                ]
            ),
        ) 
    except Exception as e:
        print(
            "\nBot has failed to access the log Channel. Make sure that you have added your bot to your log channel and promoted as admin!"
        )
        console.print(f"\n[red]Stopping Bot")
        return
    a = await app.get_chat_member(LOG_GROUP_ID, BOT_ID)
    if a.status != "administrator":
        print("Promote Bot as Admin in Logger Channel")
        console.print(f"\n[red]Stopping Bot")
        return
    console.print(f"\n┌[red] Bot Started as {BOT_NAME}!")
    console.print(f"├[green] ID :- {BOT_ID}!")
    if STRING1 != "None":
        try:
            await ASS_CLI_1.join_chat("OfficialYukki")
            await ASS_CLI_1.join_chat("YukkiSupport")
        except:
            pass
        console.print(f"├[red] Assistant 1 Started as {ASSNAME1}!")
        console.print(f"├[green] ID :- {ASSID1}!")
    if STRING2 != "None":
        try:
            await ASS_CLI_2.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 2 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 2 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_2.join_chat("OfficialYukki")
            await ASS_CLI_2.join_chat("YukkiSupport")
        except:
            pass
        console.print(f"├[red] Assistant 2 Started as {ASSNAME2}!")
        console.print(f"├[green] ID :- {ASSID2}!")
    if STRING3 != "None":
        try:
            await ASS_CLI_3.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 3 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 3 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_3.join_chat("OfficialYukki")
            await ASS_CLI_3.join_chat("YukkiSupport")
        except:
            pass
        console.print(f"├[red] Assistant 3 Started as {ASSNAME3}!")
        console.print(f"├[green] ID :- {ASSID3}!")
    if STRING4 != "None":
        try:
            await ASS_CLI_4.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 4 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 4 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_4.join_chat("OfficialYukki")
            await ASS_CLI_4.join_chat("YukkiSupport")
        except:
            pass
        console.print(f"├[red] Assistant 4 Started as {ASSNAME4}!")
        console.print(f"├[green] ID :- {ASSID4}!")
    if STRING5 != "None":
        try:
            await ASS_CLI_5.send_message(
                LOG_GROUP_ID,
                "<b>Congrats!! Assistant Client 5 has started successfully!</b>",
            )
        except Exception as e:
            print(
                "\nAssistant Account 5 has failed to access the log Channel. Make sure that you have added your Assistant to your log channel and promoted as admin!"
            )
            console.print(f"\n[red]Stopping Bot")
            return
        try:
            await ASS_CLI_5.join_chat("OfficialYukki")
            await ASS_CLI_5.join_chat("YukkiSupport")
        except:
            pass
        console.print(f"├[red] Assistant 5 Started as {ASSNAME5}!")
        console.print(f"├[green] ID :- {ASSID5}!")
    if LOG_SESSION != "None":
        try:
            await LOG_CLIENT.join_chat("OfficialYukki")
            await LOG_CLIENT.join_chat("YukkiSupport")
        except:
            pass
    console.print(f"└[red] Yukki Music Bot Boot Completed.")
    if STRING1 != "None":
        await pytgcalls1.start()
    if STRING2 != "None":
        await pytgcalls2.start()
    if STRING3 != "None":
        await pytgcalls3.start()
    if STRING4 != "None":
        await pytgcalls4.start()
    if STRING5 != "None":
        await pytgcalls5.start()
    await idle()
    console.print(f"\n[red]Stopping Bot")


@app.on_callback_query(filters.regex("shikhar"))
async def shikhar(_, CallbackQuery):
    text, keyboard = await help_parser(CallbackQuery.from_user.mention)
    await CallbackQuery.message.edit(text, reply_markup=keyboard)


if __name__ == "__main__":
    loop.run_until_complete(initiate_bot())
