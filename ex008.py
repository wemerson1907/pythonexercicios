#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

metro = float(input('Quantos metros? '))
dm = metro * 10
cm = metro * 100
mm = metro * 1000
dam = metro / 10
hm = metro / 100
km = metro / 1000

print(f'{metro} Metros,\n '
      f'Convertido em CM é {cm:.0f}\n'
      f'Convertido em MM é {mm:.0f}\n'
      f'Convertido em DM é {dm:.0f}\n'
      f'Convertido em DAM é {dam}\n'
      f'Convertido em HM é {hm}\n'
      f'Convertido em KM é {km}')



