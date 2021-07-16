import subprocess
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import Updater
from telegram.ext import Filters
from telegram.ext import MessageHandler
from post_processing import post_processing
from pathlib import Path

model = Path('model_from_web/lines_1024_batches').absolute()
launch_file = Path('generate_transformers.py').absolute()


def message_handler(update: Update, context: CallbackContext):
    my_text = update.message.text
    generated_text = subprocess.run(f"python3 {launch_file} "
                                    f"--model_type=gpt2 "
                                    f"--model_name_or_path={model} "
                                    f"--k=20 --p=0.9 --prompt='{my_text}' --length=150",
                                    shell=True, capture_output=True
                                    )
    decoded_generated_text = generated_text.stdout.decode()
    response = post_processing(str(decoded_generated_text))
    update.message.reply_text(text=str(response))
    print(my_text)


def main():
    print("Start")
    updater = Updater(
        token="1487513251:AAGuqREy6i6xqATYxrwN9DvlWAJS2ioBk3M",
        use_context=True,
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=message_handler))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()