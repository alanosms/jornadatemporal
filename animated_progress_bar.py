import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

percentage_of_month_passed = 5.71
percentage_of_week_passed = 0.86
percentage_of_year_passed = 36.89

labels = ['Mês', 'Semana', 'Ano']
values = [percentage_of_month_passed, percentage_of_week_passed, percentage_of_year_passed]

fig, ax = plt.subplots()
bars = ax.bar(labels, [0, 0, 0])
texts = [ax.text(bar.get_x() + bar.get_width() / 2, 0, '', ha='center', va='bottom') for bar in bars]

def update_bars(frame):
    for bar, text, value in zip(bars, texts, values):
        bar.set_height(value * frame / 100)
        text.set_text('{:.2f}%'.format(value * frame / 100))

ani = FuncAnimation(fig, update_bars, frames=np.linspace(0, 100, 100), interval=50)

plt.xlabel('Tempo percorrido')
plt.ylabel('Porcentagem')
plt.title('Progress Bar Animation')
plt.ylim(0, 100)
plt.show()
plt.pause(8)