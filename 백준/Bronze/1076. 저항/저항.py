color = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}

resistance = []
for _ in range(3):
    resistance.append(input())

value = ''
for i in range(2):
    value += color[resistance[i]]

print(int(value) * (10 ** int(color[resistance[2]])))