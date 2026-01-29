from aiogram import types
from database.supabase_db import Database

async def process_ticket_request(callback: types.CallbackQuery, category: str, subject: str):
    user_id = callback.from_user.id
    ticket = await Database.create_ticket(user_id, category, subject)
    
    text = (
        f"🎫 **Ticket Criado com Sucesso!**\n\n"
        f"🆔 **ID:** #{ticket['id']}\n"
        f"📁 **Setor:** {category}\n"
        f"📝 **Assunto:** {subject}\n\n"
        f"Aguarde. Um consultor Lara V3 entrará em contato ou seu produto será processado."
    )
    
    await callback.message.answer(text, parse_mode="Markdown")
    # Aqui você enviaria uma notificação para o seu ADMIN_ID