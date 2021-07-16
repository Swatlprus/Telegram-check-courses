from telethon import TelegramClient
import datetime, time
import settings

# Данные от Telegram Client
api_id = settings.api_id
api_hash = settings.api_hash

# Создаем Telegram сессию
client = TelegramClient('session_telegram', api_id, api_hash)

async def main():
    await client.get_dialogs() # Получение диалогов
    lest = []
    async for user in client.iter_participants(1265760150): # Проходимся по тем людям, которые состоят в данной группе
        if str(user.last_name) == 'None':
            name = str(user.first_name)
        else:
            name = str(user.first_name) + ' ' + str(user.last_name)
        if name != 'Ринат Софт Гильмияров' and name != 'RAMİN' and name != 'Admin' and name != 'None': # Исключаем некоторые имена
            lest.append(name)

    userCount = len(lest)
    year = int(input('Введите год. Пример 2020: '))
    month = int(input('Введите месяц. Пример 9: '))
    chislo = int(input('Введите число. Пример 14: '))
    i = 0
    while i != userCount:
        time.sleep(0.05)
        flag = False
        async for message in client.iter_messages((lest[i]), offset_date=(datetime.datetime(year, month, chislo)), reverse=True):
            if message.file is not None:
                flag = True
                print(str(lest[i]) + ' ----- ЕСТЬ оплата')
                break

    if flag == False:
        print(str(lest[i]) + ' ----- НЕТ оплаты')
        result = open('result.txt', 'a', encoding='utf8') # Вывод результата в текстовой файл
        nameSpace = str(lest[i]) + '\n'
        result.write(nameSpace)
        result.close()
    i += 1

    time.sleep(10) # Задержка


with client:
    client.loop.run_until_complete(main())