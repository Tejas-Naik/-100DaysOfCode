import pandas as pd

red = []
black = []
gray = []

data = pd.read_csv('squirrel_data.csv')
fur_column = data['Primary Fur Color']
for squirrel_color in fur_column:
    if squirrel_color == 'Gray':
        gray.append(squirrel_color)
    elif squirrel_color == 'Black':
        black.append(squirrel_color)
    elif squirrel_color == 'Cinnamon':
        red.append(squirrel_color)

df = pd.DataFrame(
    {
        'squirrels': ['red', 'black', 'gray'],
        'numbers': [len(red), len(black), len(gray)]
    }
)
df.to_csv('squirrel_data_analyzed.csv')
