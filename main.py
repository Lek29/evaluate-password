import urwid


def has_digit(password):
    return any([sign.isdigit() for sign in password])


def has_letters(password):
    return any([sign.isalpha() for sign in password])


def is_very_long(password):
    return len(password) > 12


def has_upper_letters(password):
    return any([sign.isupper() for sign in password])


def has_lower_letters(password):
    return any([sign.islower() for sign in password])


def has_symbols(password):
    return any([sign in '%#' for sign in password])


check_function = [
    has_digit,
    has_letters,
    has_upper_letters,
    has_lower_letters,
    is_very_long,
    has_symbols,
]


def calculate_rating(password):
    score = 0
    for func in check_function:
        if func(password):
            score += 2
    return f'Рейтинг пароля: {score}'


def on_password_change(edit, new_edit_text):
    rating = calculate_rating(new_edit_text)
    reply.set_text(f'{rating}')


def main():
    global reply
    input_password = urwid.Edit('Введите пароль:', mask='*')
    reply = urwid.Text('Рейтинг пароля: 0')
    menu = urwid.Pile([input_password, reply])
    menu = urwid.Filler(menu, valign='middle')

    urwid.connect_signal(input_password, 'change', on_password_change)
    urwid.MainLoop(menu).run()


if __name__ == '__main__':
    main()