from typing import List
from famous import FamousPerson
from instagram_bot import InstagramBot
import logging

logger = logging.getLogger(__name__)

class DailyFamousInstagramRemainder:

    def __init__(self, client: InstagramBot, list_of_famous: List[FamousPerson]) -> None:
        self.client = client
        self.client.login()
        self.list_of_famous = list_of_famous

    def send_remainders(self) -> None:
        for famous in self.list_of_famous:
            try:
                last_post = self.client.get_latest_post(famous.instagram_user)
                self.client.comment_on_post(last_post, famous.get_daily_text())
                famous.post_url = last_post.code
                famous.save()
            except Exception as e:
                logger.error(f"Could not send message to {famous.instagram_user}: {e}")
                raise
            else:
                logger.info(f"Message sent to {famous.instagram_user}")
