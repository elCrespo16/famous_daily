from instagram_bot import InstagramBot
from telegram import TelegramNotifier
from pathlib import Path
from famous import FamousLoader
from daily_remainder_bot import DailyFamousInstagramRemainder
import logging

logger = logging.getLogger(__name__)
ConsoleOutputHandler = logging.StreamHandler()
logging.basicConfig(filename='summary.log', encoding='utf-8', level=logging.INFO)
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.INFO)
session_path = Path("session.json")


def main():
    notifier = TelegramNotifier()
    notifier.notify("Starting upload")
    try:
        bot = InstagramBot()
        famous_loader = FamousLoader()
        list_of_famous = famous_loader.load()
        logger.info(f"Loaded {len(list_of_famous)} famous people")
        list_of_famous_to_notify = ", ".join([f"Loaded famous person: {famous.name}, Instagram: {famous.instagram_user}"
                                    for famous in list_of_famous if famous.instagram_user])
        notifier.notify(list_of_famous_to_notify)
        daily_remainder = DailyFamousInstagramRemainder(bot, list_of_famous)
        daily_remainder.send_remainders()
    except Exception as e:
        notifier.notify(f"Error: {e}")
    else:
        notifier.notify("Upload finished")



if __name__ == "__main__":
    main()