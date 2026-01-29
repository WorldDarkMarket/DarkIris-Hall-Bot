def dark_market_menu():
    buttons = [
        [
            InlineKeyboardButton(text="💳 Dark GG", callback_data="buy_dark_gg"),
            InlineKeyboardButton(text="💎 Dark AMEX", callback_data="buy_dark_amex")
        ],
        [InlineKeyboardButton(text="🚀 Dark CC (Bot Externo)", callback_data="open_dark_cc")],
        [InlineKeyboardButton(text="🔑 Dark Logins", callback_data="cat_logins")],
        [InlineKeyboardButton(text="📄 Dark Docs", callback_data="cat_docs")],
        [InlineKeyboardButton(text="⬅️ Voltar ao Hall", callback_data="back_to_main")]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)