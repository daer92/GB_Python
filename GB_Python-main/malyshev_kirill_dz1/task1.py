
duration = int(input('Введите время в секундах: '))


def conversion(duration):
    day_value = duration // (60 * 60 * 24)
    hour_value = (duration % (60 * 60 * 24)) // 3600
    min_value = (duration % (60 * 60)) // 60
    seconds_value = duration % 60

    if duration < 60:
        print('секунд: ', seconds_value)
    if duration >= 60 and duration < 3600:
        print(f'минут: {min_value} секунд: {seconds_value}')
    if duration >= 3600 and duration < 86400:
        print(f'часов: {hour_value} минут: {min_value} секунд: {seconds_value}')
    if duration >= 86400:
        print(f'дней: {day_value} часов: {hour_value} минут: {min_value} секунд: {seconds_value}')


conversion(duration)
