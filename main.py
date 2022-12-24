#!/usr/bin/env python
# pylint: disable=unused-argument, wrong-import-position
# This program is dedicated to the public domain under the CC0 license.


import logging

from telegram import __version__ as TG_VER

try:
    from telegram import __version_info__
except ImportError:
    __version_info__ = (0, 0, 0, 0, 0)  # type: ignore[assignment]

if __version_info__ < (20, 0, 0, "alpha", 1):
    raise RuntimeError(
        f"This example is not compatible with your current PTB version {TG_VER}. To view the "
        f"{TG_VER} version of this example, "
        f"visit https://docs.python-telegram-bot.org/en/v{TG_VER}/examples.html"
    )
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Привет, {user.mention_html()}! Напиши /help, чтобы увидеть доступные команды."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_html(
        "<b>Список доступных команд</b>\n"
        "/floppa -- Прислать ASCII рисунок Шлёпы\n"
        "/imposter -- Прислать ASCII рисунок Импостера\n"
        "/amogus_sus -- Прислать ASCII рисунок Амогуса\n"
        "/gigachad -- Прислать ASCII рисунок Гигачада\n"
        "/problem -- Что-то не так?"
    )

# Data strings
floppa_str = "BRUH"
imposter_str = ""
amogus_str = ""
gigachad_str = ""
trollface_str = ""

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    print(update.message.text)
    await update.message.reply_text(update.message.text + '?')
    
async def send_string(str, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_markdown_v2("```" + str + "```")


async def floppa_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_string(floppa_str, update, context)

    
async def imposter_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_string(imposter_str, update, context)

    
async def amogus_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_string(amogus_str, update, context)

    
async def gigachad_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await send_string(gigachad_str, update, context)

    
async def trollface_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    for i in range(20):
        await send_string(trollface_str, update, context)


def main() -> None:
    # Create the Application and pass the token to it
    application = Application.builder().token("5868502448:AAFdwqJKKuxlaiAyVDd-akz3JT3WegrmVlc").build()
    
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("floppa", floppa_command))
    application.add_handler(CommandHandler("imposter", imposter_command))
    application.add_handler(CommandHandler("amogus_sus", amogus_command))
    application.add_handler(CommandHandler("gigachad", gigachad_command))
    application.add_handler(CommandHandler("problem", trollface_command))
    
    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling()


if __name__ == "__main__":
    with open("/data/floppa.txt", "r") as file:
        floppa_str = file.read()
        
    with open("/data/imposter.txt", "r") as file:
        imposter_str = file.read()
        
    with open("/data/amogus.txt", "r") as file:
        amogus_str = file.read()
        
    with open("/data/gigachad.txt", "r") as file:
        gigachad_str = file.read()
        
    with open("/data/trollface.txt", "r") as file:
        trollface_str = file.read()
    main()
