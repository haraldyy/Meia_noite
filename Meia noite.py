#Entrada de dados
hora = int(input('Digite as horas: '))
minuto = int(input('Digite os minutos: '))
segundos = int(input('Digite os segundos: '))
#variáveis e processamento
horax = hora * 3600
minutox = minuto * 60
tsegundos = horax + minutox + segundos
noite = int(86400)
total = (noite + tsegundos - noite)
#Saída de dados
print(f'Se passaram {total} segundos desde meia-noite')
