name = str(input('Enter your name: '))
math_grade = float(input('Enter your math grade: '))
science_grade = float(input('Enter your science grade: '))
english_grade = int(input('Enter your english grade: '))

average = float(((math_grade + science_grade + english_grade)/3))

print('Name:', name)
print('Math Grade:', math_grade)
print('Science Grade:', science_grade)
print('English Grade:', english_grade)
print('Average:', average)
