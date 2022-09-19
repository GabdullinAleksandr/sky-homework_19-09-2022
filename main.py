from random import randint
from functions import load_question, get_statistic

class Question:

    def __init__(self, quest: str, complexity: int,
                 cor_answer: str, asked: bool = False, user_answer: None = None) -> None:
        '''
        Инициализация
        :param quest: Вопрос
        :param complexity: Сложность
        :param cor_answer: Верный ответ
        :param asked: Задавался ли вопрос
        :param user_answer: Ответ игрока
        '''
        self.quest = quest
        self.complexity = complexity
        self.cor_answer = cor_answer
        self.asked = asked
        self.user_answer = user_answer
        self.point_answer = self.get_points(complexity)

    def get_points(self, complexity: int) -> int:
        '''
        Считает кол-во очков взависимости от сложности
        :param complexity: сложность
        :return: очки
        '''
        return int(complexity) * 10

    def is_correct(self, cor_answer: str, user_answer: str) -> bool:
        '''
        Проверяет верный ли ответ
        :param cor_answer: Верный ответ
        :param user_answer: Ответ игрока
        :return:
        '''
        if user_answer == cor_answer:
            return True
        else:
            return False

    def build_question(self, quest: str, complexity: int) -> None:
        '''
        Выводит вопрос и сложность
        :param quest: вопрос
        :param complexity: сложность
        '''
        print(f'Вопрос: {quest}\nСложность: {complexity}/5')

    def build_positive_feedback(self, point_answer: int) -> None:
        '''
        Выводит очки если ответ верный
        :param point_answer: очки
        '''
        print(f'Ответ верный, полученно {point_answer} баллов')

    def build_negative_feedback(self,cor_answer: str) -> None:
        '''
        Выводит верный ответ, если ответ неверен
        :param cor_answer: верный ответ
        '''
        print(f'Ответ неверный, верный ответ - {cor_answer}')


def create_question(list_questions: list) -> list:
    '''
    Создает список экземпляров класса Question
    :param list_questions: Список с вопросами из фала question.json
    :return: Список экземпляров класса
    '''
    questions: list = []
    for i in range(len(list_questions)):
        questions.append(Question(list_questions[i]['q'], list_questions[i]['d'],list_questions[i]['a']))
    return questions


def main() -> None:
    '''
    Основная функция с главным циклом программы
    '''
    questions = create_question(load_question())
    count: int = 0
    while True:
        if count == len(questions):
            get_statistic(questions)
            break
        quest = questions[(randint(0,4))]
        if quest.asked == True:
            continue
        quest.build_question(quest.quest, quest.complexity)
        quest.asked = True
        count += 1
        quest.user_answer = input('Игрок - ')
        if quest.is_correct(quest.cor_answer, quest.user_answer):
            quest.build_positive_feedback(quest.point_answer)
            continue
        else:
            quest.build_negative_feedback(quest.cor_answer)
            continue


if __name__ == '__main__':
    main()
