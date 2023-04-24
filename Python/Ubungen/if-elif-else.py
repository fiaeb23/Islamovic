
grade = int(input('Punktzahl eintrgaen (0-100):' ))

if grade > 100:  # begrenzung bis 100 (max)
  print ('error')
elif grade >= 85:
  print('1')
elif grade >= 75:
  print('2')
elif grade >= 60:
  print('3')
elif grade >= 50:
  print('4')
elif grade >= 35:
  print('5')
elif grade >= 0: #begrenzung bis 0 (min)
  print('6')
else:
  print('Error')


