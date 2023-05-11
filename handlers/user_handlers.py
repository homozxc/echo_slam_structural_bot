from aiogram import Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from lexicon import lexicon
# from config_data.config import create_kp

# Инициализируем роутер уровня модуля
router: Router = Router()
# kp = create_kp()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=lexicon.LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=lexicon.LEXICON_RU['/help'])


@router.message(Command(commands='random'))
async def process_help_command(message: Message):
    answer: list = lexicon.random_film_description()
    await message.answer(text=answer[1])
    await message.answer_photo(answer[0])
