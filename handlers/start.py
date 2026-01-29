from aiogram import Router, types
from aiogram.filters import CommandStart
from keyboards.main_menu import main_menu
from database.supabase_db import Database

router = Router()

# URL de uma imagem imponente (pode trocar pela sua depois)
HALL_IMAGE = "https://files.catbox.moe/oec9tv.jpg"

@router.message(CommandStart())
async def cmd_start(message: types.Message):
    # Registra o usuário no Supabase
    await Database.get_or_create_user(message.from_user.id, message.from_user.username)
    
    texto_boas_vindas = (
        f"🏙️ **DARK IRIS HALL**\n\n"
        f"Seja bem-vindo, {message.from_user.first_name}!\n\n"
        f"Você acaba de entrar no maior Shopping Center do Telegrama.\n"
        f"Navegue pelos nossos andares através do menu abaixo.\n\n"
        f"💎 **Saldo:** R$ 0,00 (Carregue no Banco)\n"
        f"🕵️‍♂️ **Status:** Ativo"
    )
    
    await message.answer_photo(
        photo=HALL_IMAGE,
        caption=texto_boas_vindas,
        reply_markup=main_menu(),
        parse_mode="Markdown"
    )