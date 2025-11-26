from pathlib import Path
import json

import plotly.express as px

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

mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# Строим карту мира.
title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title)
fig.show()