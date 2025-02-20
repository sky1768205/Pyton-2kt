
questions = [
    {"question": "Сколько планет в Солнечной системе?", "answer": "8"},
    {"question": "Какой язык программирования мы изучаем?", "answer": "Python"},
    {"question": "Столица Франции?", "answer": "Париж"},
    {"question": "2 + 2 * 2 = ?", "answer": "6"}
]

correct_answers = 0


for q in questions:
    print(q["question"])
    user_answer = input("Ваш ответ: ") 
    
    
    if user_answer.lower() == q["answer"].lower():
        print("Правильно!\n")
        correct_answers += 1
    else:
        print(f"Неправильно! Правильный ответ: {q['answer']}\n")


print(f"Викторина завершена! Вы ответили правильно на {correct_answers} из {len(questions)} вопросов.")