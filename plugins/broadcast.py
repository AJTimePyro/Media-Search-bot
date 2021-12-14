from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import UserIsBlocked
from utils import collection_user
from info import ADMINS


@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcastHandler(bot, message):
    if message.reply_to_message:
        MSG = message.reply_to_message
    else:
        return await message.reply_text("First send me the message that you want to send to the other users of this bot! <b>Then as a reply to it send <code>/broadcast</code></b>")
    m = await message.reply_text("`Broadcasting..`")
    ALLCHATS = [document['userid'] for document in collection_user.find()]
    SUCE = 0
    FAIL = 0
    BlOCK = 0
    for chat in ALLCHATS:
        try:
            await MSG.copy(chat)
            SUCE += 1
        except UserIsBlocked:
            BlOCK += 1
        except Exception as e:
            FAIL += 1
    await message.reply_text(
        f"Successfully Broadcasted to {SUCE} Chats\nFailed - {FAIL} Chats\nBlocked - {BLOCK} !"
    )
    await m.delete()

@Client.on_message(filters.command("stats") & filters.user(ADMINS))
async def gistat(_, message):
    count = 0
    for document in collection_user.find():
        count += 1
    await message.reply_text(f"Total Chats in Database - {count}", quote=True)

