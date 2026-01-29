from aiogram import Router, F, types
from database.supabase_db import Database
from keyboards.shop_menus import dark_market_menu

router = Router()

@router.callback_query(F.data == "buy_dark_gg")
async def buy_gg(callback: types.CallbackQuery):
    user = await Database.get_or_create_user(callback.from_user.id, callback.from_user.username)
    preco_gg = 50.0 # Exemplo
    
    if float(user['balance']) < preco_gg:
        return await callback.answer("❌ Saldo insuficiente no Banco Iris!", show_alert=True)
    
    # Tenta pegar do estoque
    item = await Database.get_stock_item("GG")
    if not item:
        return await callback.answer("⚠️ Estoque esgotado! Tente mais tarde.", show_alert=True)
    
    # Deduz saldo e entrega
    await Database.update_balance(callback.from_user.id, -preco_gg)
    
    await callback.message.answer(
        f"✅ **Compra Realizada!**\n\n"
        f"📦 **Produto:** Dark GG\n"
        f"💳 **Dados:**\n`{item['content']}`\n\n"
        f"Obrigado por comprar no DarkIrisHall!",
        parse_mode="Markdown"
    )