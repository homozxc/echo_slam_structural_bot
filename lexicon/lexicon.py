from config_data.config import create_kp


LEXICON_RU: dict[str, str] = {
    '/start': 'Привет!\n\nЯ эхо-бот для демонстрации работы роутеров!\n\n'
              'Если хотите - можете мне что-нибудь прислать или '
              'отправить команду /help',
    '/help': 'Я просто отправляю вам копию вашего сообщения',
    'no_echo': 'Данный тип апдейтов не поддерживается '
               'методом send_copy'
}

def random_film_description() -> list:
    kp = create_kp()
    film = kp.random()
    text = f'{film.name}\n\n' \
           f'{film.description}'
    return [film.poster.url,text]


