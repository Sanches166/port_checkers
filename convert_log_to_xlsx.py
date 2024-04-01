import re
import pandas as pd

# Создаем пустой список для хранения данных
data = []

# Открываем лог-файл и читаем его построчно
with open('server.log', 'r') as file:
    for line in file:
        # Используем регулярное выражение для поиска данных
        match = re.search(r".*\('(.+)', (\d+).+?(\d+)", line)
        if match:
            # Извлекаем данные из найденных групп
            ip_address = match.group(1)
            source_port = match.group(2)
            destination_port = match.group(3)
            
            # Добавляем данные в список
            data.append([ip_address, source_port, destination_port])

# Создаем DataFrame из списка данных
df = pd.DataFrame(data, columns=['IP Address', 'Source Port', 'Destination Port'])

# Сохраняем DataFrame в файл Excel
df.to_excel('log_data.xlsx', index=False)
