from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Token do seu bot
TELEGRAM_TOKEN = '8037174017:AAElk-QFrQq2wZO6c4GWn4tqPPf9ChvecjA'  # Substitua aqui

# Links dos produtos
checkout_links = {
    "Produto 1": "https://seusite.com/checkout/produto1",
    "Produto 2": "https://seusite.com/checkout/produto2",
    "Produto 3": "https://seusite.com/checkout/produto3",
}

# Botões inline para produtos
def get_botoes():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🛒 Produto 1", url=checkout_links["Produto 1"])],
        [InlineKeyboardButton("📦 Produto 2", url=checkout_links["Produto 2"])],
        [InlineKeyboardButton("💳 Produto 3", url=checkout_links["Produto 3"])],
    ])

# Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Olá! Seja bem-vindo ao nosso bot de vendas!\n\nClique abaixo para ver os produtos disponíveis:")
    await update.message.reply_photo(
        photo="https://via.placeholder.com/600x300.png?text=Imagem+do+Produto",
        caption="Escolha um produto para comprar:",
        reply_markup=get_botoes()
    )

# Comando /comprar
async def comprar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://i.imgur.com/NEx4B2F.jpeg",
        caption="Escolha um produto para comprar:",
        reply_markup=get_botoes()
    )

# Comando /duvidas
async def duvidas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❓ *Dúvidas Frequentes:*\n\n"
        "- Como funciona o pagamento?\n"
        "Você será redirecionado para um checkout seguro com todas as formas de pagamento disponíveis.\n\n"
        "- Quando recebo o produto?\n"
        "Imediatamente após a confirmação de pagamento, você receberá por e-mail ou diretamente no chat.\n\n"
        "Se precisar de ajuda, fale com o suporte.",
        parse_mode='Markdown'
    )

# Função principal
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("comprar", comprar))
    app.add_handler(CommandHandler("duvidas", duvidas))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
