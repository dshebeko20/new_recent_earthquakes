from pathlib import Path
import json

# Считываем данные в строковом формате и преобразуем в объект Python.
path = Path('eq_data/d_30_day_m_1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Создаём удобнную для чтения версию файла данных.
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# Обработка всех землетрясений в наборе данных.
all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))