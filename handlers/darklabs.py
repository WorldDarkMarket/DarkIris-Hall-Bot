from aiogram import Router, F, types
from keyboards.main_menu import main_menu # Para o botão de voltar

router = Router()

@router.callback_query(F.data == "open_darklabs")
async def open_darklabs(callback: types.CallbackQuery):
    texto = (
        "🧪 **DARK LABS - ÁREA DE PESQUISA**\n\n"
        "Bem-vindo ao laboratório DarkLabs. Aqui o conhecimento é a maior moeda.\n\n"
        "🔹 **DarkToolsLabs:** Ferramentas privadas e scripts exclusivos.\n"
        "🔹 **AcademiaGhost:** Formações, consultorias e canais VIP."
    )
    
    buttons = [
        [types.InlineKeyboardButton(text="💀 DarkToolsLabs (Área Restrita)", callback_data="tools_labs")],
        [types.InlineKeyboardButton(text="👻 AcademiaGhost (Cursos)", callback_data="academia_ghost")],
        [types.InlineKeyboardButton(text="⬅️ Voltar ao Hall", callback_data="back_to_main")]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    
    await callback.message.edit_text(texto, reply_markup=keyboard, parse_mode="Markdown")

@router.callback_query(F.data == "academia_ghost")
async def academia_ghost(callback: types.CallbackQuery):
    texto = (
        "🎓 **ACADEMIA GHOST**\n\n"
        "Escolha sua especialização:\n"
        "• Cursos de Carding & Eng. Social\n"
        "• Mentorias Individuais\n"
        "• Acesso a Canais de Conteúdo"
    )
    # Aqui você usaria a mesma lógica de Ticket do Shopping
    buttons = [[types.InlineKeyboardButton(text="🎫 Abrir Ticket de Matrícula", callback_data="buy_course")],
               [types.InlineKeyboardButton(text="⬅️ Voltar", callback_data="open_darklabs")]]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    
    await callback.message.edit_text(texto, reply_markup=keyboard, parse_mode="Markdown")