import os
from supabase import create_client, Client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

class Database:
    @staticmethod
    async def get_or_create_user(id_tg, username):
        user = supabase.table("users").select("*").eq("id_tg", id_tg).execute()
        if not user.data:
            user = supabase.table("users").insert({"id_tg": id_tg, "username": username, "balance": 0}).execute()
        return user.data[0]

    @staticmethod
    async def update_balance(id_tg, amount):
        # amount pode ser negativo para compras
        user = await Database.get_or_create_user(id_tg, None)
        new_balance = float(user['balance']) + amount
        supabase.table("users").update({"balance": new_balance}).eq("id_tg", id_tg).execute()
        return new_balance

    @staticmethod
    async def create_ticket(user_id, category, subject):
        ticket = supabase.table("tickets").insert({
            "user_id": user_id,
            "category": category,
            "subject": subject
        }).execute()
        return ticket.data[0]

    @staticmethod
    async def get_stock_item(category):
        # Busca um item disponível e marca como vendido (Lógica do BOTCC_GG)
        item = supabase.table("stock").select("*").eq("category", category).eq("is_sold", False).limit(1).execute()
        if item.data:
            supabase.table("stock").update({"is_sold": True}).eq("id", item.data[0]['id']).execute()
            return item.data[0]
        return None