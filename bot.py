import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from questions import Questions
from expert import CarDiagnostic, Symptom

bot = telebot.TeleBot('7519902205:AAHeqnJQe_0iqCbByRlhDELOyWsmtz7bUE8')

diagnosis = {}
user_categories = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        '🚗 Welcome to the Car Troubleshooting Bot! 🛠️\n\nYou can input symptoms like unusual noises, difficulty starting, or check engine light, and the system will suggest potential causes and fixes. 🔧'
    )
    show_categories(message)

def show_categories(message):
    user_categories[message.chat.id] = set()
    markup = build_category_keyboard(user_categories[message.chat.id])
    bot.send_message(
        message.chat.id,
        "Please select the categories you'd like to include in the diagnosis:",
        reply_markup=markup
    )

def build_category_keyboard(selected_categories):
    categories = [
        ("🔋 Battery Issues", "battery"),
        ("🚗 Motor Issues", "motor"),
        ("🛑 Braking Issues", "braking"),
        ("💡 Electronics Issues", "electronics"),
        ("🛞 Tires & Suspension", "tires_suspension"),
        ("💻 Software Issues", "software"),
        ("🔧 Miscellaneous", "misc"),
        ("🚀 Start Diagnosis", "start_diagnosis")
    ]

    markup = InlineKeyboardMarkup(row_width=2)
    for text, callback_data in categories:
        if callback_data != "start_diagnosis":
            text = f"✅ {text}" if callback_data in selected_categories else text
        markup.add(InlineKeyboardButton(text, callback_data=callback_data))

    return markup

@bot.callback_query_handler(func=lambda call: True)
def handle_category_selection(call):
    chat_id = call.message.chat.id

    if call.data == "start_diagnosis":
        selected_categories = list(user_categories.get(chat_id, []))
        if not selected_categories:
            bot.send_message(chat_id, "Please select at least one category before starting the diagnosis.")
            return
        
        global questions_complete, short_questions_complete
        questions_complete, short_questions_complete = Questions.combine_questions(selected_categories)
        bot.send_message(chat_id, "Starting the diagnosis. Please answer with 'yes' or 'no'.")
        send_question(chat_id, 0)
        diagnosis[chat_id] = {'answers': [], 'current_question': 0}
    else:
        if call.data in user_categories[chat_id]:
            user_categories[chat_id].remove(call.data)
        else:
            user_categories[chat_id].add(call.data)

        markup = build_category_keyboard(user_categories[chat_id])
        bot.edit_message_reply_markup(chat_id, call.message.message_id, reply_markup=markup)

def send_question(chat_id, question_index):
    bot.send_message(chat_id, questions_complete[question_index])

@bot.message_handler(func=lambda message: message.chat.id in diagnosis)
def handle_answers(message):
    chat_id = message.chat.id
    text = message.text.lower()

    if text in ['yes', 'no']:
        answer = text == 'yes'
        current_question = diagnosis[chat_id]['current_question']
        diagnosis[chat_id]['answers'].append({short_questions_complete[current_question]: answer})

        current_question += 1
        if current_question < len(questions_complete):
            diagnosis[chat_id]['current_question'] = current_question
            send_question(chat_id, current_question)
        else:
            bot.send_message(chat_id, '✅ Diagnosis complete. Here are the results:')
            run_expert_system(chat_id, diagnosis[chat_id]['answers'])
            del diagnosis[chat_id]
    else:
        bot.send_message(chat_id, 'Please answer with "yes" or "no".')

def run_expert_system(chat_id, answers):
    expert = CarDiagnostic()
    expert.reset()
    for answer in answers:
        for symptom, value in answer.items():
            expert.declare(Symptom(**{symptom: value}))
    expert.run()
    
    if expert.diagnoses:
        for diagnosis, recommendations in expert.diagnoses.items():
            for recommendation in recommendations:
                bot.send_message(chat_id, f"{diagnosis}\n{recommendation}", parse_mode='Markdown')
    else:
        bot.send_message(chat_id, "No issues detected based on the provided symptoms. Please consult a professional mechanic for further assistance.")

bot.polling()