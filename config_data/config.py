from dataclasses import dataclass
from environs import Env
from kinopoisk_dev import KinopoiskDev



@dataclass
class TgBot:
    token: str            # Токен для доступа к телеграм-боту


@dataclass
class Config:
    tg_bot: TgBot
    kp_token: str


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')),kp_token='KP_TOKEN')


def create_kp(path: str | None = None) -> KinopoiskDev:
    env = Env()
    env.read_env(path)
    return KinopoiskDev(env('KP_TOKEN'))
