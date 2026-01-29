📂 Estrutura de Pastas (Boilerplate)
Plaintext
DarkIrisHallBot/
├── main.py                # Ponto de entrada (Inicia o bot)
├── config.py              # Carrega variáveis do .env
├── database/
│   ├── supabase_db.py     # Conexão e Queries (Supabase)
│   └── models.py          # Definição das tabelas
├── handlers/              # Lógica de cada seção
│   ├── start.py           # Boas-vindas e Menu Principal
│   ├── shopping.py        # XDeals, Streamings, Viagens
│   ├── darkmarket.py      # GG, CC, Logins, Docs
│   ├── bank.py            # Saldo, Extrato, Pix/Crypto
│   └── darklabs.py        # AcademiaGhost e Tools
├── keyboards/             # Todos os InlineButtons e Menus
│   ├── main_menu.py
│   ├── shop_menus.py
│   └── bank_menus.py
├── utils/                 # Tickets, Gerador de Pix, Formatação
│   └── ticket_system.py
├── assets/                # IDs de imagens/midia (para não reenviar o arquivo sempre)
└── .env                   # Referência de variáveis