print('№9 виконала Григореко Катерина Вікторівна з групи КМ-82')
print('Функція - Insert(s,s1,n). Призначення - вставка в рядок s підрядка s1, починаючи з позиції n.')

def insert(s,s1,number):
    d=' '
    if len(s) <= number:#перевірка довжини строки
        s += d*(number-len(s))#дописати пустоти
        s += s1#додати рядок
    else:
        s=s[:number] + s1 + s[number:] #додати рядок зріз
    return s
def forRepeat ():#запис даних
    s=input('s:')
    return s
def forRepeat1():#запис даних
    s1=input('s1:')
    return s1
def forRepeat2():
    while True:#запис і перевірка довжини
            try:
                number=int(input('number:'))
                if number == abs(number):
                    break
                else:
                    continue
            except valueError:
                continue
    return number


print(insert(forRepeat(),forRepeat1(),forRepeat2()))

correct=False
while (not correct):#повтор коду
    print('do you want to repeat(press 1)')
    answer=input()
    if answer in '1':
        print(insert(forRepeat(),forRepeat1(),forRepeat2()))
    else:
        break
        
    
    
