# Task 5
# Вводиться з клавіатури користувачем текст.
# Знайти в ньому найдовше слово та вивести його на екран.

text = input('Enter the text: ')
text1 = text.split(' ')
print(max(text1, key=len))