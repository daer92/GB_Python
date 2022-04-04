
# duration = int(input('Введите время в секундах: '))
#
#
# def conversion(duration):
#     sec_conv = duration % (24 * 3600)      # Преобразование входных секунд
#     hour_value = sec_conv // 3600
#     day_value = sec_conv // 86400
#     min_value = sec_conv // 60
#     seconds_value = sec_conv % 60
#     if duration < 60:
#         print('секунд: ', seconds_value)
#     if duration >= 60 and duration < 3600:
#         print(f'минут: {min_value} секунд: {seconds_value}')
#     if duration >= 3600 and duration < 86400:
#         print(f'часов: {hour_value} минут: {min_value} секунд: {seconds_value}')
#     if duration >= 86400:
#         print(f'дней: {day_value} часов: {hour_value} минут: {min_value} секунд: {seconds_value}')
#
# conversion(duration)
