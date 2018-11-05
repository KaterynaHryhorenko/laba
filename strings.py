print('№9 виконала Григореко Катерина Вікторівна з групи КМ-82')
print('Замінити всі символи a на d у словах, довжина яких менше обраної. ')

def Change(st,simbol_from,simbol_to):
    result = ''
    for i in st:
        if(i == simbol_from):#перевірка символа
            result += simbol_to
        else:
            result += i#додати елемент
    return result
def Find_words(words,simbol_from,simbol_in):
    result = ''
    for i in words:
        if (len(i) <= number):#перевірка довжини
            result += Change(i, simbol_from, simbol_in) + ' '#додати символи
        else:
            result += i + ' '
    return result
line = input('line:')
Correct=False
while(not Correct):#перевірка числа
    try:
        number = int(input('Nuumber :'))
        Correct=True
    except:
        pass
words = line.split(' ')#розбити на елементи списку

print(Find_words(words,'a','d'))
correct=False
while (not correct):#повтор функції
    print('do you want to repeat(press 1)')
    answer=input()
    if answer in '1':
        line = input('line:')
        Correct=False
        while(not Correct):
            try:
                number = int(input('Nuumber :'))
                Correct=True
            except:
                pass
        words = line.split(' ')
        print(Find_words(words,'a','d'))
    else:
        break
