from aiogram import Router, F, types
from database.supabase_db import Database
from keyboards.bank_menus import bank_main_menu # Vamos criar abaixo

router = Router()

@router.callback_query(F.data == "open_bank")
async def open_bank(callback: types.CallbackQuery):
    user = await Database.get_or_create_user(callback.from_user.id, callback.from_user.username)
    
    texto_perfil = (
        f"🏛️ **BANCO IRIS - PAINEL DO CLIENTE**\n\n"
        f"👤 **Usuário:** {callback.from_user.full_name}\n"
        f"🆔 **ID:** `{callback.from_user.id}`\n"
        f"💰 **Saldo Disponível:** R$ {user['balance']:.2f}\n\n"
        f"Escolha uma operação abaixo:"
    )
    
    await callback.message.edit_text(texto_perfil, reply_markup=bank_main_menu(), parse_mode="Markdown")

@router.callback_query(F.data == "deposit_money")
async def start_deposit(callback: types.CallbackQuery):
    # Aqui futuramente integraremos a API do Mercado Pago ou Gateway Crypto
    await callback.message.answer(
        "💎 **CARREGAR SALDO**\n\n"
        "1️⃣ Envie o valor que deseja depositar.\n"
        "2️⃣ Escolha o método (PIX ou Crypto).\n\n"
        "*(Simulação: Por enquanto, crie um ticket de depósito para falar com a Lara V3)*"
    )
    # Chama o sistema de ticket para o admin validar o depósito manual por enquanto
    from utils.ticket_system import process_ticket_request
    await process_ticket_request(callback, "FINANCEIRO", "Depósito de Saldo")

    from os import getenv

@router.message(F.text.startswith("/setbalance"))
async def set_user_balance(message: types.Message):
    # Apenas você (ADMIN) pode usar
    if str(message.from_user.id) != getenv("ADMIN_ID"):
        return

    try:
        # Exemplo de uso: /setbalance 12345678 100
        parts = message.text.split()
        target_id = int(parts[1])
        new_amount = float(parts[2])
        
        from database.supabase_db import supabase
        supabase.table("users").update({"balance": new_amount}).eq("id_tg", target_id).execute()
        
        await message.answer(f"✅ Saldo de `{target_id}` atualizado para R$ {new_amount}", parse_mode="Markdown")
    except Exception as e:
        await message.answer("❌ Erro. Use: `/setbalance ID VALOR`")

@router.callback_query(F.data == "view_history")
async def view_history(callback: types.CallbackQuery):
    from database.supabase_db import supabase
    
    # Busca as últimas 10 transações
    res = supabase.table("transactions").select("*").eq("user_id", callback.from_user.id).order("created_at", desc=True).limit(10).execute()
    
    if not res.data:
        return await callback.answer("📜 Você ainda não possui movimentações.", show_alert=True)
    
    msg = "📜 **HISTÓRICO DE CONTA**\n\n"
    for t in res.data:
        icon = "➕" if t['amount'] > 0 else "➖"
        msg += f"{icon} R$ {abs(t['amount']):.2f} - {t['type']} ({t['created_at'][:10]})\n"
        
    await callback.message.answer(msg, parse_mode="Markdown")        