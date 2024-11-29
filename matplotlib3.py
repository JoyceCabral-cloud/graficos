import matplotlib.pyplot as plt

#Exemplo de um gráfico circular

frutas = ['Bananas', 'Maçãs', 'Pêras', 'Morangos', 'Uvas']
quantidades_vendidas = [40, 55, 25, 50, 68]

plt.pie(quantidades_vendidas, labels=frutas, autopct='%1.2f%%')
plt.title('Gráfico Circular')
plt.show()
