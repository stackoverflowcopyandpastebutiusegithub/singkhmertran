import logging
from telegram import Update
from telegram.ext import *
import pandas as pd
import os
import re

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

inputtoken = input()

def singinoutkhmer(inputin):
    # Function to generate lowercase and original capitalization
    def generate_lowercase_and_original(word):
        lowercase_word = word.lower().strip()
        if lowercase_word == word:
            return [lowercase_word]
        else:
            return [lowercase_word, word]

    # Function to split text into words and symbols while keeping their positions
    def split_text(text):
        return re.findall(r"[a-zA-Z0-9']+|[^\w\s]", text, re.UNICODE)

    # Get the current directory of the script
    script_dir = os.getcwd()  # Use os.getcwd() to get the current working directory
    # Construct the full path to the TSV file
    tsv_path = os.path.join(script_dir, 'sing khmer translator', r'R:\\sing khmer translator\\dic.tsv')

    # Read the TSV file into a DataFrame
    df = pd.read_csv(tsv_path, sep='\t')

    # Split the input string into words and symbols
    words_and_symbols = split_text(inputin)

    # Create a dictionary to store the variables
    invar = {}

    # Generate lowercase and original capitalization for each word and assign to variables
    for word in words_and_symbols:
        if re.match(r"[a-zA-Z0-9']+", word):  # Only process alphanumeric words and words with apostrophes
            invar[word.lower().strip()] = generate_lowercase_and_original(word)

    # Compare with data in the 3rd column from the start (left)
    third_column_data = df.iloc[:, 2].str.lower().str.strip().tolist()
    fourth_column_data = df.iloc[:, 3].tolist()

    # Create a dictionary to store comparison results and replacements
    replacements = {}

    # Compare each variable with the 3rd column data and find replacements from the 4th column
    for var, values in invar.items():
        for value in values:
            value = value.lower().strip()
            if value in third_column_data:
                index = third_column_data.index(value)
                replacements[var] = fourth_column_data[index]
                break

    # Replace words in the input string with their corresponding words from the 4th column and keep symbols unchanged
    output_list = []
    for word in words_and_symbols:
        replacement = replacements.get(word.lower().strip(), None)
        if replacement:
            output_list.append(replacement)
        else:
            output_list.append(word)

    # Ensure there is no space between words found in the TSV file but space for words not found
    output_string = ''
    last_replacement_index = -1

    for i in range(len(output_list)):
        if i > 0 and output_list[i-1] not in replacements.values() and output_list[i] not in replacements.values():
            output_string += ' '
        if output_list[i] not in replacements.values() and last_replacement_index != -1 and i == last_replacement_index + 1:
            output_string += ' '
        output_string += output_list[i]
        if output_list[i] in replacements.values():
            last_replacement_index = i

    return(output_string)

def respones(text: str) -> str:
    greetings = ["hello", "good morning", "good afternoon", "good evening", "hi"]
    slang_words = ["kdmh", "ah jm", "jm", "kdor", "jui", "juii", "kdouy", "Kdet", "ejui", "ng", "jg", "mea hg", "ah slab"]
    identity_questions = ["who are you", "what are you", "what is your name"]
    well_being_questions = ["how are you", "how are you doing"]
    thanks_phrases = ["thank you", "thanks"]
    creator_questions = ["who created you", "who made you", "who is your creator", "who created you?", "who made you?", "who is your creator?"]
    creator_likes_questions = ["does your creator like anyone?", "does your creator like anyone" "did the person who made you like anyone", "does he like anyone", "does he like anyone?", "does she like anyone", "does she like anyone?"]

    if any(phrase in text for phrase in greetings):
        return "oh thanks now lets get to work"
    
    if any(phrase in text for phrase in slang_words):
        return "ng"
    
    if any(phrase in text for phrase in identity_questions):
        return "I am THE sing khmer bot"
    
    if any(phrase in text for phrase in well_being_questions):
        return "I'm fine thanks"
    
    if any(phrase in text for phrase in thanks_phrases):
        return "you're welcome"
    
    if any(phrase in text for phrase in creator_questions):
        return "I was created by @stack_overflow_copy_and_paste_py"
    
    if any(phrase in text for phrase in creator_likes_questions):
        return "yeah he likes a person named lyka in his class or jessica idk?"
    
    else:
        return "sorry didn't get that, i think we should just start use \n/help of you don't know"
    
def singoutinkhmer(inputout):
    print("sorry this function is not available yet, Maybe in the future")

async def change_lan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="sorry this function is not available yet, Maybe in the future")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! what brings you here today?, I am here to help you translate khmer slang(sing khmer) in to normal khmer")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="here are the commands you can use:\n/start\n/help\n/translatein\n/translateout")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="if you want to translate khmer slang (sing khmer) normal khmer use the \n/tranlatein command if you want to translate normal khmer to khmer slang (sing khmer). and for the other way just use the \n/translateout command")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="if you wnt to go back to default mode then use \n/back. or \n/changelan to change the language hope this helps!")

async def translatein(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="please enter the text you want to translate from sing khmer to normal khmer")
    context.user_data['mode'] = 'translatein'

async def translateout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="please enter the text you want to translate from normal khmer to sing khmer")
    context.user_data['mode'] = 'translateout'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mode = context.user_data.get('mode', 'default')
    if mode == 'translatein':
        translated_text = singinoutkhmer(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)
    elif mode == 'translateout':
        translated_text = singoutinkhmer(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=translated_text)
    else:
        response_text = respones(update.message.text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response_text)

async def back(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['mode'] = 'default'
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Back to default mode.")

if __name__ == '__main__':
    application = ApplicationBuilder().token(inputtoken).build()
    
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help', help)
    translatein_handler = CommandHandler('translatein', translatein)
    translateout_handler = CommandHandler('translateout', translateout)
    back_handler = CommandHandler('back', back)
    change_language = CommandHandler('changelan', change_lan)
    message_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(translatein_handler)
    application.add_handler(translateout_handler)
    application.add_handler(back_handler)
    application.add_handler(change_language)
    application.add_handler(message_handler)
    
    application.run_polling()