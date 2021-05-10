import math

valores_hex = {
  'A': 10,
  'B': 11,
  'C': 12,
  'D': 13,
  'E': 14,
  'F': 15
}
lista_hex = ['A', 'B', 'C', 'D', 'E', 'F']

def main():
  numero = list(input('\nQual o número? ').upper())
  base = int(input('Qual a base? '))
  if '.' in numero:
    numero[numero.index('.')] = ','
  if ',' in numero:
    numero_antes_da_virgula = list(''.join(numero).split(',')[0])[::-1]
    numero_depois_da_virgula = list(''.join(numero).split(',')[1])
    print('\n{}'.format(com_virgula(numero_antes_da_virgula, numero_depois_da_virgula, base)))
  else:
    print('\n{}'.format(sem_virgula(numero[::-1], base)))
  

def sem_virgula(numero, base):
  for n in numero:
    for h in lista_hex:
      if n == h:
        numero[numero.index(n)] = valores_hex[h]
  resultado = 0
  for i in range(len(numero)):
    temp = int(numero[i]) * (math.pow(base, i))
    resultado = resultado + temp
  return resultado

def com_virgula(numero_antes_da_virgula, numero_depois_da_virgula, base):
  for n in numero_depois_da_virgula:
    for h in lista_hex:
      if n == h:
        numero_depois_da_virgula[numero_depois_da_virgula.index(n)] = valores_hex[h]
  resultado_antes_da_virgula = sem_virgula(numero_antes_da_virgula, base)
  resultado_depois_da_virgula = 0
  resultado = 0
  for i in range(len(numero_depois_da_virgula)):
    pos = i + 1
    temp = float(int(numero_depois_da_virgula[i]) * float(math.pow(base, (pos * -1))))
    resultado_depois_da_virgula = resultado_depois_da_virgula + temp
  resultado = resultado_antes_da_virgula + resultado_depois_da_virgula
  return str(resultado).replace('.', ',')

if __name__ == '__main__':
  main()