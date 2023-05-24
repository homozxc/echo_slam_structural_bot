from aiogram import Router
from aiogram.filters import Command, CommandStart, Text, or_f
from aiogram.types import Message, CallbackQuery
from lexicon.lexicon import *
from keyboards.keyboards import start_kb, create_inline_kb
from filters.filters import IsDigitCallbackData

# Инициализируем роутер уровня модуля
router: Router = Router()


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'], reply_markup=start_kb)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(or_f(Command(commands='random'), Text(text=LEXICON_RU['random_button'])))
async def process_random_command(message: Message):
    answer: list = film_description()
    await message.answer(text=answer[1])
    await message.answer_photo(answer[0])


@router.message(or_f(Command(commands='genres'), Text(text=LEXICON_RU['genres_button'])))
async def process_genres_command(message: Message):
    await message.answer(text=LEXICON_RU['/genres'], reply_markup=create_inline_kb(1, **BUTTONS))


@router.callback_query(Text(startswith='genr'))
async def process_genre_press(callback: CallbackQuery):
    await callback.message.edit_text(text='Выберите интересующий фильм, для подробного описания',
                                     reply_markup=create_inline_kb(1, **genres(5, int(callback.data[-1:]))))


@router.callback_query(IsDigitCallbackData())
async def process_film_press(callback: CallbackQuery):
    answer: list = film_description(int(callback.data))
    await callback.message.edit_text(text=answer[1])
    await callback.message.reply_photo(photo=answer[0])
