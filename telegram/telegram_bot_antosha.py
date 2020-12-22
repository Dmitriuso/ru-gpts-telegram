import subprocess
import telegram
from telegram import Update
from telegram import Bot
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.utils.request import Request
from post_processing import post_processing


def log_error(f):
    def inner(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(f'Ошибка: {e}')
            raise e
    return inner


@log_error
def message_handler(update: Update, context: CallbackContext):
    my_text = update.message.text
    generated_text = subprocess.run("python3 "
                                    "/home/dmitri/Forschung/text_generation/ru-gpts-for-telegram/generate_transformers.py "
                                    "--model_type=gpt2 "
                                    "--model_name_or_path=/home/dmitri/Forschung/text_generation/ru-gpts-for-telegram/model_from_web/ckpt_60000/ "
                                    "--k=20 --p=0.9 --prompt='{}' --length=100".format(my_text), shell=True, capture_output=True)
    decoded_generated_text = generated_text.stdout.decode()
    response = post_processing(str(decoded_generated_text))
    update.message.reply_text(text=str(response))
    print(my_text)


def main():
    # print("Start")

    req = Request(
        connect_timeout=0.7,
    )

    bot = Bot(
        request=req,
        token='1487513251:AAGuqREy6i6xqATYxrwN9DvlWAJS2ioBk3M',
        base_url="https://telegg.ru/orig/bot",
    )
    updater = Updater(
        bot=bot,
        use_context=True,
    )

    #print(updater.bot.get_me())

    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
