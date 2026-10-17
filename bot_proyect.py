import os
import random

from dotenv import load_dotenv
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler,
    MessageHandler,
    filters
)

# 1. /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎬 ¡Bienvenido a CINEBOT! 🍿\n\n"
        "Tu asistente de películas en Telegram.\n\n"
        "Escribe /ayuda para ver los comandos."
    )


# 2. /ayuda
async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎬🍿 CINEBOT - LISTA DE COMANDOS 🍿🎬\n\n"

        "1️⃣ /start\n"
        "Inicia CINEBOT y muestra el mensaje de bienvenida.\n\n"

        "2️⃣ /ayuda\n"
        "Muestra todos los comandos disponibles y qué hacen.\n\n"

        "3️⃣ /cartelera\n"
        "Muestra las películas disponibles en cartelera.\n\n"

        "4️⃣ /estrenos\n"
        "Muestra los próximos estrenos de películas.\n\n"

        "5️⃣ /recomendar\n"
        "Recomienda una película al azar y te muestra un link con la informacion de la pelicula.\n\n"

        "6️⃣ /generos\n"
        "Muestra los géneros de películas disponibles.\n\n"

        "7️⃣ /horarios\n"
        "Muestra los horarios de las películas.\n\n"

        "8️⃣ /precios\n"
        "Muestra los precios de las entradas.\n\n"

        "9️⃣ /pelicula\n"
        "Permite buscar una película por su nombre.\n"
        "Ejemplo: /pelicula Avengers Doomsday y te da informacion relacionada\n\n"

        "🔟 /imagen\n"
        "Muestra la portada de una película.\n\n"

        "1️⃣1️⃣ /trailer\n"
        "Muestra el tráiler de una película.\n\n"

        "1️⃣2️⃣ /musica\n"
        "Reproduce música en CINEBOT.\n\n"

        "━━━━━━━━━━━━━━━━━━\n"
        "Escribe un comando para comenzar."
    )


# 3. /cartelera
async def cartelera(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎥 CARTELERA CINEBOT 🍿\n\n"
        "1. DIGGER\n"
        "2. VERITY: LA SOMBRA DE UN ENGAÑO\n"
        "3. STREET FIGHTER\n"
    )


# 4. /estrenos
async def estrenos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🆕 ESTRENOS CINEBOT\n\n"
        "PRONTO TENDREMOS MAS ESTRENOS SI EL GOLI LO SUBE"
    )


# 5. /recomendar
async def recomendar(update: Update, context: ContextTypes.DEFAULT_TYPE):

    peliculas = [
        {
            "nombre": "🎬 Digger",
            "link": "https://www.google.com/search?q=Digger+pelicula+Tom+Cruise"
        },
        {
            "nombre": "🔎 Verity: La Sombra de un Engaño",
            "link": "https://www.google.com/search?q=Verity+pelicula+2026"
        },
        {
            "nombre": "🥊 Street Fighter",
            "link": "https://www.google.com/search?q=Street+Fighter+pelicula+2026"
        }
    ]

    seleccion = random.choice(peliculas)

    await update.message.reply_text(
        f"⭐ CINEBOT TE RECOMIENDA:\n\n"
        f"{seleccion['nombre']}\n\n"
        f"📅 Consulta información sobre su estreno:\n"
        f"{seleccion['link']}"
    )


# 6. /generos
async def generos(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎭 GÉNEROS DISPONIBLES\n\n"
        "Acción\n"
        "Terror\n"
        "Comedia\n"
        "Ciencia ficción\n"
        "Romance\n"
        "Fantasía\n"
        "Drama\n"
        "Animación\n"
        "PROXIMAMENTE"
    )


# 7. /horarios
async def horarios(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🕒 HORARIOS\n\n"
        "🎬 Digger: 14:00 | 17:00 | 20:00\n"
        "🎬 Verity: La Sombra de un Engaño: 15:30 | 18:30 | 21:30\n"
        "🎬 Street Fighter: 13:00 | 16:00 | 19:00"
    )


# 8. /precios
async def precios(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "💰 PRECIOS\n\n"
        "🎫 General: Bs 35\n"
        "🎓 Estudiante: Bs 25\n"
        "🧒 Niños: Bs 20\n"
        "🎥 Sala 3D: Bs 45"
    )


# 9. /pelicula
async def pelicula(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Si el usuario no escribe una película
    if not context.args:

        await update.message.reply_text(
            "🔎 Escribe el nombre de una película.\n\n"
            "Ejemplo:\n"
            "/pelicula Avengers Doomsday"
        )

        return

    # Guarda el nombre escrito por el usuario
    nombre = " ".join(context.args)

    # Muestra la película buscada
    await update.message.reply_text(
        "📄 Información del estreno:"
    )

    # Envía el archivo de texto
    try:

        with open("estreno.txt", "rb") as archivo:

            await update.message.reply_document(
                document=archivo,
                filename="estreno.txt",
                caption=f"🎬 Información sobre: {nombre}"
            )

    except FileNotFoundError:

        await update.message.reply_text(
            "❌ No encontré el archivo estreno.txt"
        )


# 10. /imagen
async def imagen(update: Update, context: ContextTypes.DEFAULT_TYPE):

    botones = [
        [
            InlineKeyboardButton(
                "🎬 Digger",
                callback_data="imagen_digger"
            )
        ],
        [
            InlineKeyboardButton(
                "🔎 Verity",
                callback_data="imagen_verity"
            )
        ],
        [
            InlineKeyboardButton(
                "🥊 Street Fighter",
                callback_data="imagen_streetfighter"
            )
        ]
    ]

    teclado = InlineKeyboardMarkup(botones)

    await update.message.reply_text(
        "🖼️ ELIGE UNA PORTADA:",
        reply_markup=teclado
    )


# 11. /trailer
async def trailer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    botones = [
        [
            InlineKeyboardButton(
                "🎬 Digger",
                callback_data="trailer_digger"
            )
        ],
        [
            InlineKeyboardButton(
                "🔎 Verity",
                callback_data="trailer_verity"
            )
        ],
        [
            InlineKeyboardButton(
                "🥊 Street Fighter",
                callback_data="trailer_streetfighter"
            )
        ]
    ]

    teclado = InlineKeyboardMarkup(botones)

    await update.message.reply_text(
        "🎥 ELIGE UN TRÁILER:",
        reply_markup=teclado
    )


# 12. /musica
async def musica(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # Primero muestra la bienvenida
    await update.message.reply_text(
        "🎬 ¡BIENVENIDO A CINEBOT! 🍿\n\n"
    )

    try:

        with open("cine_musica.mp3", "rb") as audio:

            await update.message.reply_audio(
                audio=audio,
                title="Música CINEBOT",
                performer="CINEBOT",
            )

    except FileNotFoundError:

        await update.message.reply_text(
            "❌ No encontré cine_musica.mp3.\n\n"
        )


# ─────────────────────────────────────────────
# ACTIVADORES (palabras clave, sin "/")
# ─────────────────────────────────────────────

# Activador: DIGGER
async def activador_digger(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🎬 DIGGER\n\n"
        "Acción / Drama\n"
        "Tom Cruise, Sandra Hüller, Riz Ahmed\n\n"
        "Escribe /trailer o /imagen para ver más."
    )


# Activador: VERITY
async def activador_verity(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🔎 VERITY: LA SOMBRA DE UN ENGAÑO\n\n"
        "Suspenso / Drama\n"
        "Anne Hathaway, Dakota Johnson, Josh Hartnett\n\n"
        "Escribe /trailer o /imagen para ver más."
    )


# Activador: STREET FIGHTER
async def activador_streetfighter(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🥊 STREET FIGHTER\n\n"
        "Acción / Videojuego\n"
        "Noah Centineo, Andrew Koji, Callina Liang\n\n"
        "Escribe /trailer o /imagen para ver más."
    )


# ─────────────────────────────────────────────
# MENSAJES (respuesta por defecto / fallback)
# ─────────────────────────────────────────────
async def mensaje_generico(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤔 No entendí tu mensaje.\n"
        "Escribe /ayuda para ver todo lo que puedo hacer."
    )


# BOTONES INTERACTIVOS (callback de imagen/trailer)
async def seleccionar_opcion(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    # PORTADA DIGGER
    if query.data == "imagen_digger":

        await query.message.reply_text(
            "🎬 DIGGER\n\n"
            "Acción / Drama\n"
            "Tom Cruise, Sandra Hüller, Riz Ahmed\n\n"
            "🖼️ Ver póster e información:\n"
            "https://en.wikipedia.org/wiki/Digger_(2026_film)"
        )

    # PORTADA VERITY
    elif query.data == "imagen_verity":

        await query.message.reply_text(
            "🔎 VERITY: LA SOMBRA DE UN ENGAÑO\n\n"
            "Suspenso / Drama\n"
            "Anne Hathaway, Dakota Johnson, Josh Hartnett\n\n"
            "🖼️ Ver póster e información:\n"
            "https://en.wikipedia.org/wiki/Verity_(film)"
        )

    # PORTADA STREET FIGHTER
    elif query.data == "imagen_streetfighter":

        await query.message.reply_text(
            "🥊 STREET FIGHTER\n\n"
            "Acción / Videojuego\n"
            "Noah Centineo, Andrew Koji, Callina Liang\n\n"
            "🖼️ Ver póster e información:\n"
            "https://en.wikipedia.org/wiki/Street_Fighter_(2026_film)"
        )

    # TRAILER DIGGER
    elif query.data == "trailer_digger":

        await query.message.reply_text(
            "🎬 DIGGER\n\n"
            "🎥 Tráiler oficial doblado:\n"
            "https://www.youtube.com/watch?v=-JL3J9qFjVI\n\n"
            "🍿 CINEBOT"
        )

    # TRAILER VERITY
    elif query.data == "trailer_verity":

        await query.message.reply_text(
            "🔎 VERITY: LA SOMBRA DE UN ENGAÑO\n\n"
            "🎥 Tráiler oficial doblado:\n"
            "https://www.youtube.com/watch?v=2f_JoPuescs\n\n"
            "🍿 CINEBOT"
        )

    # TRAILER STREET FIGHTER
    elif query.data == "trailer_streetfighter":

        await query.message.reply_text(
            "🥊 STREET FIGHTER\n\n"
            "🎥 Tráiler oficial doblado:\n"
            "https://www.youtube.com/watch?v=mzYHS4VIjgY\n\n"
            "🍿 CINEBOT"
        )


if __name__ == "__main__":

    # El token ya NO va escrito en el código: se lee del archivo .env
    load_dotenv()
    TOKEN = os.getenv("TELEGRAM_TOKEN")

    if not TOKEN:
        print("❌ No se encontró TELEGRAM_TOKEN.")
        print("Crea un archivo .env junto a este archivo con la línea:")
        print("TELEGRAM_TOKEN=tu_token_de_botfather")
        raise SystemExit(1)

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .connect_timeout(30)
        .read_timeout(30)
        .write_timeout(30)
        .pool_timeout(30)
        .build()
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))
    app.add_handler(CommandHandler("cartelera", cartelera))
    app.add_handler(CommandHandler("estrenos", estrenos))
    app.add_handler(CommandHandler("recomendar", recomendar))
    app.add_handler(CommandHandler("generos", generos))
    app.add_handler(CommandHandler("horarios", horarios))
    app.add_handler(CommandHandler("precios", precios))
    app.add_handler(CommandHandler("pelicula", pelicula))
    app.add_handler(CommandHandler("imagen", imagen))
    app.add_handler(CommandHandler("trailer", trailer))
    app.add_handler(CommandHandler("musica", musica))

    # BOTONES DE IMAGEN Y TRAILER
    app.add_handler(
        CallbackQueryHandler(seleccionar_opcion)
    )

    # ─────────────────────────────────────────
    # ACTIVADORES (deben ir ANTES del mensaje genérico,
    # si no, el genérico capturaría todo primero)
    # ─────────────────────────────────────────
    app.add_handler(
        MessageHandler(filters.Regex(r"(?i)digger"), activador_digger)
    )
    app.add_handler(
        MessageHandler(filters.Regex(r"(?i)verity"), activador_verity)
    )
    app.add_handler(
        MessageHandler(filters.Regex(r"(?i)street"), activador_streetfighter)
    )

    # ─────────────────────────────────────────
    # MENSAJE GENÉRICO (fallback) — SIEMPRE AL FINAL
    # ─────────────────────────────────────────
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, mensaje_generico)
    )

    print("CINEBOT INICIANDO...")
    print("BOT ACTIVO")

    app.run_polling()
