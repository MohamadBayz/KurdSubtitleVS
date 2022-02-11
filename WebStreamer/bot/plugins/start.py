from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot


@StreamBot.on_message(filters.command(["start", "help"]))
async def start(_, m: Message):
    await m.reply(
        f'سڵاوت لێبێت {m.from_user.mention(style="md")} 📢!, دەتوانیت هەر جۆرە فایلێک بتەوێت بۆم بنێریت و منیش بەستەری سەیرکردن و دابەزاندنیت پێبدەم. 🔻
تێبینی ئەم بۆتە بەتایبەتی بۆ بەگەڕخستنی ڤیدیۆ دروست کراوە، بۆیە هەوڵبدە ڤیدیۆکە بەپێی تایبەتمەندییە خوازراوەکان بێت تاکو بەبێ کێشە بتوانرێت بەگەڕبخرێت. ▶️'
    )
