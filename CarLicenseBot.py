import logging, sys, os
import requests
from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application, CallbackContext, JobQueue
from urllib.request import urlopen
#import requests
from bs4 import BeautifulSoup
from seleniumbase import Driver
import time

import WebInteraction
import Enums, ProductObjects

TOKEN: Final = os.environ.get('TOKEN')
BOT_USERNAME: Final = "@CarLicenseBot"
DEBUG: Final = True
logger = logging.getLogger('CarLicenseLogger')

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.debug(f'In start_command!')
    await update.message.reply_text('Hello! Thanks for chatting with me. I am CarLicenseBot!')

async def help_command(update: Update, context:CallbackContext):
    logger.debug(f'In help_command!')
    await update.message.reply_text('This is the help command!')


def handle_text_response(text: str) -> str:
    text = text.lower()
    #if "yad2" in text:
    #    fetch_Yad2()

def send_message_to_group(chat_id, thread_id, message_text: str):
    # formatting options in here: https://core.telegram.org/bots/api#formatting-options

    url_post = (f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=" + str(chat_id) +
                "&message_thread_id=" + str(thread_id) + "&parse_mode=HTML" + "&text=" + "<b>" + str(message_text) + "</b>")
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = requests.post(url_post, headers=headers)
    #print(r)
    #print(requests.get(url).json())  # this sends the message



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text = str = update.message.text.lower()

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    if "do" in text:
        wi = WebInteraction.WebInteraction(logger)
        result = wi.interact_with_website('7524613')
        await update.message.reply_text(result)
        # if reply:
        #     #await update.message.reply_text(reply)
        #     send_message_to_group(Enums.ChatsIds.LemesiraTempGroup, reply)
        # else:
        #     logger.warning("Fetched yad2 data is empty.")
        #     await update.message.reply_text("Fetched yad2 data is empty.")

    # if message_type == 'group':
    #     if BOT_USERNAME in text:
    #         new_text: str = text.replace(BOT_USERNAME, '').strip()
    #         response: str = handle_text_response(new_text)
    #     else:
    #         return
    # else:
    #     response: str = handle_text_response(text)

    # print('Bot:', response)
    # await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.error(f'Update {update} caused error {context.error}')


def init_logger():
    logger.debug('initializing logger')
    # Set the threshold logging level of the logger to INFO
    if DEBUG:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)
    # Create a stream-based handler that writes the log entries    #into the standard output stream
    handler = logging.StreamHandler(sys.stdout)
    # Create a formatter for the logs
    logger.addHandler(handler)


def init_seleniumbase_driver():
    logger.debug('initializing seleniumbase_driver')
    os.environ["PATH"] = "/opt/render/project/.render/chrome/opt/google/chrome:" + os.environ.get("PATH", "")
    try:
        driver = Driver(uc=True, headless=True)
        driver.get(Enums.LemesiraURLs.example)
        time.sleep(1)
    except NameError:
        logger.error(f'Error fetching url in init_seleniumbase_driver try')
    except Exception as e:
        logger.error(f'Something else went wrong in init_seleniumbase_driver try, the error is: {e}')
    finally:
        logger.debug(f'init_seleniumbase_driver.quit()')
        driver.quit()


def check_function():

    pass


if __name__ == '__main__':
    init_logger()
    logger.info('Starting CarLicense bot...')

    init_seleniumbase_driver()
    #check_function()
    app = Application.builder().token(TOKEN).build()

    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # Message handler for all text messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls
    logger.info('Polling...')
    app.run_polling(poll_interval=2)
