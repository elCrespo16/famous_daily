from typing import Any
from instagrapi import Client
from instagrapi.exceptions import LoginRequired
from pathlib import Path
import os
import logging

logger = logging.getLogger(__name__)
ConsoleOutputHandler = logging.StreamHandler()
logging.basicConfig(filename='summary.log', encoding='utf-8', level=logging.INFO)
logger.addHandler(ConsoleOutputHandler)
logger.setLevel(logging.INFO)
session_path = Path("session.json")

class InstagramBot:
    def __init__(self):
        self.username =  os.environ.get("USERNAME", "")
        self.password = os.environ.get("PASSWORD", "")
        self.client = Client()
        self.client.delay_range = [1, 3]

    def login(self):
        login_via_session = False
        login_via_pw = False

        session = self.client.load_settings(session_path) if session_path.exists() else None

        if session:
            try:
                self.client.set_settings(session)
                self.client.login(self.username, self.password)

                # check if session is valid
                try:
                    self.client.get_timeline_feed()
                except LoginRequired:
                    logger.info("Session is invalid, need to login via username and password")

                    old_session = self.client.get_settings()

                    # use the same device uuids across logins
                    self.client.set_settings({})
                    self.client.set_uuids(old_session["uuids"])

                    self.client.login(self.username, self.password)
                login_via_session = True
            except Exception as e:
                logger.info("Couldn't login user using session information: %s" % e)

        if not login_via_session:
            try:
                logger.info("Attempting to login via username and password. username: %s" % self.username)
                if self.client.login(self.username, self.password):
                    login_via_pw = True
            except Exception as e:
                logger.info("Couldn't login user using username and password: %s" % e)

        if not login_via_pw and not login_via_session:
            raise Exception("Couldn't login user with either password or session")

    def get_latest_post(self, username: str):
        user_id = self.client.user_id_from_username(username)
        medias = self.client.user_medias(user_id, 1)
        if not medias:
            raise Exception(f"No media found for user {user_id}")
        return medias[0]

    def comment_on_post(self, comment: Any, text: str) -> None:
        self.client.media_comment(comment.id, text)
        logger.info(f"Commented on post {comment.code} {text}")