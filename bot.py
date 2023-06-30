import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from evernote.api.client import EvernoteClient
from evernote.edam.type.ttypes import Note

# Ваш токен Telegram-бота
TELEGRAM_TOKEN = 'YOUR_TELEGRAM_TOKEN'

# Ваши данные для доступа к Evernote API
EVERNOTE_TOKEN = 'YOUR_EVERNOTE_TOKEN'
EVERNOTE_SANDBOX = False  # Установите True, если вы используете Sandbox-среду

# Обработчик команды /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Привет! Отправь мне заметку, и я сохраню ее в Evernote.')

# Обработчик сообщений с заметками
def save_note(update, context):
    note_content = update.message.text  # Получаем содержимое заметки из сообщения
    save_to_evernote(note_content)  # Сохраняем заметку в Evernote
    context.bot.send_message(chat_id=update.effective_chat.id, text='Заметка сохранена в Evernote!')

# Функция сохранения заметки в Evernote
def save_to_evernote(content):
    client = EvernoteClient(token=EVERNOTE_TOKEN, sandbox=EVERNOTE_SANDBOX)
    note_store = client.get_note_store()
    note = Note()
    note.title = "Заметка из Telegram"
    note.content = '&lt;?xml version="1.0" encoding="UTF-8"?&gt;' \
                   '&lt;!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd"&gt;' \
                   '&lt;en-note&gt;' + content + '&lt;/en-note&gt;'
    note_store.createNote(note)

# Создаем экземпляр бота и добавляем обработчики команд и сообщений
def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, save_note))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()