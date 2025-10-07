from datetime import datetime
from typing import List
import yaml
import os
from pydantic import BaseModel

class FamousPerson(BaseModel):
    name: str
    instagram_user: str
    default_text: str = "Día {day}: esperando con ilusión que {name} pueda enviar un 'feliz cumpleaños' a mi futura esposa Adriana. Sería el regalo de su vida. 💕"
    start_day: datetime = datetime.now()
    post_url: str = ""

    @classmethod
    def load(cls, config_file) -> 'BaseModel':
        """
        Load config from file
        """
        with open(config_file) as f:
            config = yaml.load(f.read(), Loader=yaml.FullLoader)
        new_config =  cls.parse_obj(config)
        return new_config

    def save(self, config_file):
        """
        Save config to file
        """
        with open(config_file, "w") as f:
            yaml.dump(self.dict(), f, default_flow_style=False)

    def get_daily_text(self) -> str:
        """
        Set the publication day in the text
        """
        day = (datetime.now() - self.start_day).days
        return self.default_text.replace("{day}", str(day)).replace("{name}", self.name)

class FamousLoader:

    FAMOUS_FOLDER = "data"

    def load(self) -> List[FamousPerson]:
        list_of_famous = []
        for file in os.listdir(self.FAMOUS_FOLDER):
            if file.endswith(".yaml") or file.endswith(".yml"):
                config_file = os.path.join(self.FAMOUS_FOLDER, file)
                list_of_famous.append(FamousPerson.load(config_file))
        return list_of_famous
