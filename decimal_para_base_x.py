def main():
  decimal = input('\nDigite um número: ')
  base = input('Digite a base de destino: ')
  if ',' in decimal or '.' in decimal:
    bits_de_precisão = input('Digite a quantidade de bits de precisão desejada: ')
    decimal = decimal.replace(',', '.')
    parte_inteira = decimal.split('.')[0]
    parte_decimal = decimal.split('.')[1]
    print('\n{}'.format(com_virgula(int(parte_inteira), int(parte_decimal), int(base), int(bits_de_precisão))))
  else:
    print('\n{}'.format(sem_virgula(int(decimal), int(base))))

def sem_virgula(parte_inteira, base):
  resultado = ''
  while True:
    resultado += str(parte_inteira % base)
    parte_inteira /= base
    if ',' in str(parte_inteira):
      parte_inteira = int(str(parte_inteira).split(',')[0])
    elif '.' in str(parte_inteira):
      parte_inteira = int(str(parte_inteira).split('.')[0])
    if parte_inteira < base:
      resultado += str(parte_inteira)
      return resultado[::-1]
      break

def com_virgula(parte_inteira, parte_decimal, base, bits_de_precisão):
  resultado = sem_virgula(parte_inteira, base) + ','
  while int(str(parte_decimal)[0]) > 0:
    parte_decimal /= 10
  for i in range(bits_de_precisão):
    j = parte_decimal * base
    if ',' in str(j):
      k = int(str(j).split(',')[0])
    elif '.' in str(j):
      k = int(str(j).split('.')[0])
    parte_decimal = j - k
    resultado += str(k)
  return resultado


if __name__ == '__main__':
  main()