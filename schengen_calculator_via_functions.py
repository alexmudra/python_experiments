RESIDENCE_LIMIT = 90  # 45, 60 (КОНСТАНТА)
SCHENGEN_CONSTRAINT = 180 #(КОНСТАНТА)
visits = [[1, 10], [61, 90], [101, 140], [141, 160], [271, 290]] #список візитів


def get_visit_length(visit):
    return visit[1] - visit[0] + 1


def calc_days_for_visits(visits):
    days_for_visits = []
    for visit in visits:
        days_for_visit = 0
        for past_visit in visits:
            if visit[0] - SCHENGEN_CONSTRAINT < past_visit[0] < visit[0]:
                days_for_visit += get_visit_length(past_visit)
        days_for_visit += get_visit_length(visit)
        days_for_visits.append(days_for_visit)
    return days_for_visits


days_for_visits = calc_days_for_visits(visits)

for visit, total_days in zip(visits, days_for_visits):
    if total_days > RESIDENCE_LIMIT:
        overstay_time = total_days - RESIDENCE_LIMIT #рахує перевищення ліміту в перебування країнаї ЄС
        print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')


def predict_visit_days(day_in_future):
    visits_with_future = visits + [[day_in_future, day_in_future]] #підрахує візити у майбутньому
    days_for_visits_in_future = calc_days_for_visits(visits_with_future)

    days_in_es_for_future_visit = days_for_visits_in_future[len(days_for_visits_in_future) - 1]

    days_we_can_stay_in_es = RESIDENCE_LIMIT - days_in_es_for_future_visit + 1
    print('Я смогу пробыть в шенеге {0} дней, если въеду {1} числа'.format(days_we_can_stay_in_es, day_in_future))


def predict_visit(): #ф-ія нічого не повертає (в код), а просто друкує дані
    print('Планировние поездки в Шенген')
    print('Введите день поездки')
    day_of_visit = int(input())
    predict_visit_days(day_of_visit)



while True:
    print('Введи команду:')
    print('p - узнать сколько дней смогу пребывать в Шенгене:')
    print('e - закрыть программу')
    user_input = input()
    if user_input == 'p':
        predict_visit()
    if user_input == 'e':
        break

# # робим безкінечний цикл
#
# while True:
#     user_input = input()
#     if user_input == 'v':
#         start = int(input())
#         end = int(input())
#         visits.append([start, end])