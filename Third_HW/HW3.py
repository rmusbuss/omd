import csv
from typing import Iterable, Optional, Union
# from pprint import pprint


def read_csv(filename: str) -> tuple:
    """
    Эта функция нужна для чтения данных с csv файлов.
    Она вытаскивает и выводит заголовок и данные отдельно
    """
    with open(filename) as f:
        reader = csv.reader(f, delimiter=';')
        # reader_dict = csv.DictReader(f)
        headers = next(reader)
        data = list(reader)
        return headers, data


def save_csv(data: Iterable) -> None:
    """
    Эта функция нужна для чтения данных с csv файлов.
    Она вытаскивает и выводит заголовок и данные отдельно
    """
    with open('solution.csv', 'w') as f:
        writer = csv.writer(f)
        for row in data:
            writer.writerow(row)


def department_teams(hierarchy_dict_unique: dict, data: list) -> dict:
    """
    Эта функция принимает на вход уникальные данные и исходные данные
    и для каждого департамента записывает входящие в него команды
    """
    departments_dict = {hierarchy: [] for hierarchy in
                        hierarchy_dict_unique['Департамент']}
    for department_name in hierarchy_dict_unique['Департамент']:
        for row in data:
            if department_name in row:
                team_name = row[2]
                if team_name not in departments_dict[department_name]:
                    departments_dict[department_name].append(team_name)
    return departments_dict


def summary_maker(salary_col: list) -> list:
    """
    Эта функция принимает на вход колонку (список) с ЗП
    и на основе данных в ней подсчитывает min-max вилку,
    среднюю зп, а также численность (т.е. количество значений в массиве)
    """
    num_people = len(salary_col)
    min_max_salary = f'{min(salary_col)}-{max(salary_col)}'
    avg_salary = sum(salary_col) / num_people
    return [num_people, min_max_salary, avg_salary]


def salary_in_departments(hierarchy_dict_unique: dict, data: list) -> list:
    """
    Эта функция принимает на вход уникальные данные и исходные данные
    и для каждого департамента выполняет сводный отчет - находит численность,
    вилку зп и среднюю зп
    """
    summary_dict = {hierarchy: [] for hierarchy in
                    hierarchy_dict_unique['Департамент']}
    for department_name in hierarchy_dict_unique['Департамент']:
        for row in data:
            if department_name in row:
                salary = int(row[5])
                summary_dict[department_name].append(salary)
    _dict = {key: summary_maker(value) for key, value in summary_dict.items()}
    column_names = ['Название', 'Численность', '"Вилка" зарплат',
                    'Средняя зарплата']
    final_list = []
    final_list.append(column_names)
    final_list.extend([[key] + value for key, value in _dict.items()])
    return final_list


def solution(filename: str = 'Corp_Summary.csv') -> Optional[Union[list, dict]]:
    """
    Это итоговая функция
    Она принимает на вход имя файла с данными,
    далее спрашивает у пользователя, что ему нужно предоставить
    и выполняет определенные указания в зависимости от того,
    что он хочет (либо выводит, либо сохраняет)
    """

    choose = input('1. Вывести в понятном виде иерархию команд, \n\
т.е. департамент и все команды, которые входят в него\n\n\
2.Вывести сводный отчёт по департаментам: \n\
название, численность, "вилка" зарплат в виде мин – макс, среднюю зарплату\n\n\
3.Сохранить сводный отчёт из предыдущего пункта в виде csv-файла. \n\
При этом необязательно вызывать сначала команду из п.2\n')
    # Считывание с файла csv
    headers, data = read_csv(filename)

    # Создание файла csv
    save_csv(data)

    # Записываем данные в файл, а далее оставляем только уникальные
    hierarchy_dict = {header: [] for header in headers}
    for row in data:
        for ind, element in enumerate(row):
            hierarchy_dict[headers[ind]].append(element)
    hierarchy_dict_unique = {key: set(value) for key, value in
                             hierarchy_dict.items()}

    # Обработка команд пользователя
    if choose == '1':
        departments_dict = department_teams(hierarchy_dict_unique, data)
        # pprint(departments_dict)
        # В качестве вывода можно сделать pprint()
        # чтобы иерархия красиво выводилась
        return departments_dict
    elif choose == '2':
        final_list = salary_in_departments(hierarchy_dict_unique, data)
        # pprint(final_dict)
        # В качестве вывода можно сделать pprint()
        # чтобы иерархия красиво выводилась
        return final_list
    elif choose == '3':
        final_list = salary_in_departments(hierarchy_dict_unique, data)
        save_csv(final_list)
        # return 'Saving completed'
    else:
        print('Вы ввели неверную команду. Попробуйте еще раз')
        return solution(filename)


print(solution())
