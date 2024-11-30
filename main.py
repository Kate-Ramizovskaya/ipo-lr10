import requests
import json
from bs4 import BeautifulSoup as bs
url = "https://www.scrapethissite.com/pages/simple/"
response = requests.get(url)
soup = bs(response.text, "html.parser")
countries=soup.find_all("div", class_="col-md-4 country")
for i, country in enumerate(countries, start=1): 
    country_name = country.find('h3').text.strip()
    capital = country.find('span', class_='country-capital').text.strip()
    print(f"{i}. Country: {country_name}; Capital: {capital};")

data = []

for country in countries:
    country_name = country.find('h3').text.strip()
    capital = country.find('span', class_='country-capital').text.strip()
    data.append({
        'Country': country_name,
        'Capital': capital
    })

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

import json

# Загружаем данные из JSON файла
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Создаем HTML страницу
html_content = '''
<!DOCTYPE html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Список стран и столиц</title>
    <style>
        body {
            background: linear-gradient(45deg, #83a4d4, #b6fbff);
            font-family: Arial, sans-serif;
        }
        h1 {
            text-align: center;
            margin-top: 20px;
        }
        table {
            width: 80%;
            margin: 20px auto;
            border-collapse: collapse;
        }
        th, td {
            padding: 10px;
            border: 1px solid #ddd;
            text-align: left;
        }
        th {
            background-color: #f4b084;
        }
    </style>
</head>
<body>
    <h1>Информация о странах</h1>
    <table>
        <tr>
            <th>Страна</th>
            <th>Столица</th>
        </tr>
'''

for item in data:
    html_content += f'''
        <tr>
            <td>{item['Country']}</td>
            <td>{item['Capital']}</td>
        </tr>
    '''

html_content += '''
    </table>
    <footer>
        <p style="text-align: center; margin-top: 20px;">
            <a href="https://www.scrapethissite.com/pages/simple/">Источник: Соскребите этот сайт</a>
        </p>
    </footer>
</body>
</html>
'''

# Сохраняем HTML контент в файл
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("HTML файл успешно создан: index.html")
