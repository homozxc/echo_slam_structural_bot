from config_data.config import create_kp
from kinopoisk_dev import MovieParams, MovieField, PossValField

kp = create_kp()

LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ бот, который поможет тебе найти подходящий фильм на вечер\n\n'
              'Чтобы узнать мои возможности '
              'отправьте команду /help',
    '/help': '/random - случайный фильм с его описанием\n'
             '/genres - список фильмов по выбранному жанру',
    '/genres': 'Нажми на кнопку и получи список фильмов по этим жанрам!',
    'random_button': 'Фильм',
    'genres_button': 'Фильмы по жанрам'
}

BUTTONS: dict[str,str] = {
    'genr1': 'Фильм',
    'genr2': 'Тв-сериал',
    'genr3': 'Мультфильм',
    'genr4': 'Аниме',
    'genr5': 'Анимированный сериал'
}

LEXICON_COMMANDS_RU: dict[str, str] = {
                '/start': 'Начать общение с ботом',
                '/random': 'Случайный фильм с описанием и постером',
                '/genres': 'Топ 5 произведений по жанрам'}

GENRES = [kp.possible_values_by_field(params=PossValField.GENRES)[i].slug for i in range(10)]


def film_description(index: int = 0) -> list:
    if index != 0:
        film = kp.find_one_movie(index)
    else:
        film = kp.random()
    text = f'{film.name}\n\n' \
           f'{film.description}\n\n'
    return [film.poster.url, text]


def genres(limit: int = 5, ind_genre: int = 1) -> dict:
    item = kp.find_many_movie(params=[MovieParams(keys=MovieField.TYPE_NUMBER, value=ind_genre)])
    d = {str(item.docs[i].id): item.docs[i].name for i in range(limit)}
    return d

