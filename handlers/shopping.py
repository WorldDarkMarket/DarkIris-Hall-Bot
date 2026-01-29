from aiogram import Router, F, types
from keyboards.shop_menus import shopping_categories_menu, streaming_menu # Criaremos abaixo
from utils.ticket_system import process_ticket_request

router = Router()

@router.callback_query(F.data == "open_shopping")
async def open_shopping(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "🛍️ **DARK IRIS SHOPPING**\n\nBem-vindo à galeria! Escolha um setor:",
        reply_markup=shopping_categories_menu(),
        parse_mode="Markdown"
    )

# Sub-menu de Streamings
@router.callback_query(F.data == "cat_streaming")
async def show_streaming(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "📺 **ASSINATURAS & STREAMING**\n\nSelecione o serviço desejado:",
        reply_markup=streaming_menu(),
        parse_mode="Markdown"
    )

# Lógica de compra (Exemplo: Netflix)
@router.callback_query(F.data == "buy_netflix")
async def buy_netflix(callback: types.CallbackQuery):
    # Aqui usamos a lógica de ticket que criamos antes
    await process_ticket_request(callback, "STREAMING", "Assinatura Netflix (R$ 30,00)")
    
    # Notificação Extra para o Admin
    from main import bot
    import os
    await bot.send_message(
        os.getenv("ADMIN_ID"), 
        f"🚨 **NOVA ORDEM:** {callback.from_user.full_name} solicitou Netflix!"
    )