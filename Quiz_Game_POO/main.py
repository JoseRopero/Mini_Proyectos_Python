from question_model import Question
from data import *
from quiz_brain import QuizBrain

question_bank = []  # Aquí guardaremos los objetos con las preguntas y respuestas

for questions in question_data:
    question_text = questions['text']
    question_answer = questions['answer']
    q = Question(question_text, question_answer)
    question_bank.append(q)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Has completado el cuestionario.")
print(f"Su puntuación total es de: {quiz.score}/{quiz.question_number}")

# Para usar la question_data_2 reemplazamos las líneas 8 y 9 por:
# question_text = questions['question']
# question_answer = questions['correct_answer']
