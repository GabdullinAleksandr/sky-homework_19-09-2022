import json

def load_question() -> list:
    '''
    Загружает и конвертирует в список данные из question.json
    :return: Возвращает список
    '''
    list_questions: list = []
    with open('question.json') as file:
        list_questions = json.loads(file.read())
    return list_questions


def get_statistic(questions) -> None:
    '''
    Считает статистику после того как заданы все вопросы
    '''
    score: int = 0
    count: int = 0
    for quest in questions:
        if quest.cor_answer == quest.user_answer:
            score += quest.point_answer
            count += 1
    print(f'Вот и все!\nОтвечено на {count} вопроса из {len(questions)}\nНабрано баллов: {score}')
