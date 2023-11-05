import re

text = ("Добро пожаловать в наш магазин, вот наши цены: 1 кг. яблоки - 90 руб., 2 кг. апельсины - 130 руб. Также в "
        "ассортименте орехи в следующей фасовке: 0.5 кг. миндаль - 500 руб.")

pattern = r'(\d+(\.\d+)?) кг\. (\w+) - (\d+) руб\.'
matches = re.findall(pattern, text)

for match in matches:
    weight = float(match[0])
    product = match[2]
    price = int(match[3])
    price_per_kg = price / weight
    print(f"{product} - {price_per_kg:.0f} руб/кг")
