import random

import matplotlib
import pandas as pd
def kubik(n, low, up) :
    rand_list = []

    for i in range(n):
        rand_list.append(random.randint(low, up))
    return rand_list
def count_rate(kub_data: list):
    """
    Возвращает частоту выпадания значений кубика,
    согласно полученным данным
    :param kub_data: данные эксперимента
    :return:
    """
    kub_rate = {}
    for i in kub_data:
        if i in kub_rate:
            continue
        else:
            kub_rate[i] = kub_data.count(i)
    for i in range(1, 7):
        if i not in kub_rate:
            kub_rate[i] = 0
    return kub_rate

def sort_rate(counted_rate: dict):
    """
    Возвращает отсортированную частоту по ключу
    :param counted_rate: Наша неотсортированная частота
    :return:
    """
    sorted_rate = {}
    for key in sorted(counted_rate.keys()):
        sorted_rate[key] = counted_rate[key]
    return sorted_rate

def crate_dataframe(sorted_rate):
    """
    Создание и преобразование данных в Pandas dataframe
    :param sorted_date: dict
    :return: pd.Dataframe
    """
    df = pd.DataFrame(sorted_rate, index=[0])
    df = df.T
    df = df.rename(columns={0: 'Частота'})
    df.insert(0, 'Количество выпаданий', range(1, 1 + len(df)))
    return df

def probability_solving(crate_dataframe):
    """
    Вычисление вероятности полученных результатов
    :param dataframe:
    :return:
    """
    sum_rate = crate_dataframe['Частота'].sum()
    probability = []
    for i in crate_dataframe['Частота']:
        probability.append(i / sum_rate)
    crate_dataframe['Вероятность'] = probability
    return crate_dataframe

# print(kubik(100000))
# print(sort_rate(count_rate(kubik(100000))))
# print(crate_dataframe(sort_rate(count_rate(kubik(100000)))))
# df = probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100000)))))
# print(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100000))))))

import matplotlib.pyplot as plt

def histogram(crate_dataframe, n):
    a = crate_dataframe['Вероятность'].plot (kind='bar', legend=True, color='blue')
    plt.title(f'Гистограмма для значений n = {n}')
    plt.show()

print(histogram(probability_solving(crate_dataframe(sort_rate(count_rate(kubik(100000, 1, 6))))), 100000))