from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def main_menu():
    buttons = [
        [InlineKeyboardButton(text="🛍️ Lojas (XDeals)", callback_data="open_shopping")],
        [InlineKeyboardButton(text="🌑 DarkMarket", callback_data="open_darkmarket")],
        [InlineKeyboardButton(text="🏛️ Banco Iris (Saldo/Perfil)", callback_data="open_bank")],
        [InlineKeyboardButton(text="🧪 DarkLabs", callback_data="open_darklabs")],
        [InlineKeyboardButton(text="🍻 IrisBar (Grupo)", url="https://t.me/seu_link")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)