import decimal_para_base_x
import base_x_para_decimal

def main():
  print('\n[1] => Decimal para base x')
  print('[2] => Base x para decimal')
  e = input('>: ')
  print('\n----------')
  if e == '1':
    decimal_para_base_x.main()
  elif e == '2':
    base_x_para_decimal.main()

if __name__ == '__main__':
  main()
