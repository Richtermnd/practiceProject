from aiogram import types

def _with_prefix(prefix, data):
    return f"{prefix}_{data}"


def Reply(buttons: list[list[str]]):
    kb = [[types.KeyboardButton(text=item) for item in row] for row in buttons]
    return types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)


def Inline(callback_prefix: str, buttons: list[list[tuple[str, str]]]):
    kb = [[] for _ in range(len(buttons))]
    for i, row in enumerate(buttons):
        for btn in row:
            kb[i].append(types.InlineKeyboardButton(text=btn[0], callback_data=_with_prefix(callback_prefix, btn[1])))
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def InlineRange(prefix: str, r: range, buttons_per_row=-1):
    kb = [[]]
    for i in r:
        if buttons_per_row == -1:
            kb[0].append(types.InlineKeyboardButton(text=str(i), callback_data=_with_prefix(prefix, str(i))))
        else:
            row = i // buttons_per_row
            if len(kb) < row:
                kb.append([])
            kb[row].append(types.InlineKeyboardButton(text=str(i), callback_data=_with_prefix(prefix, str(i))))
    return types.InlineKeyboardMarkup(inline_keyboard=kb)


def InlineIndexed(prefix: str, buttons: list[list[str]]):
    rows = len(buttons)
    btns = [[(text, str(j + i * rows)) for j, text in enumerate(row)] for i, row in enumerate(buttons)]
    return Inline(prefix, btns)
