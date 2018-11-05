print('№9 виконала Григореко Катерина Вікторівна з групи КМ-82')
print('Мішень для стрільби являє собою  концентричні кільця з центром на початку координат. радіус внутрішнього кільця ("десятки") - 1см.')
print('Ширина всіх інших кілець - по 1см. Написати функцію, яка за координатами трьох точок попадання (х1, у1), (х2, у2) і (х3, у3) обчислює суму вибитих очок.')
import math
def record(x):#запис данних
    while True:
        try:
            x=int(input('x='))
            break
        except ValueError:
            continue
    return x
def record1  (y):#запис данних
    while True:
        try:
            y=int(input('y='))
            break
        except ValueError:
            continue
    return y

def find (a,b):#отримати радіус точки
    d=math.sqrt(a**2+b**2)
    return d               

def roun(q1,w1,q2,w2,q3,w3):#основний код
    control=10-int(find(record(q1),record1(w1)))
    if control <= 0:#перевірка на вихід із кола
        print('out of horizont')
    else:
        print(control)
    control=10-int(find(record(q2),record1(w2)))
    if control <= 0:
        print('out of horizont')
    else:
        print(control)
    control=10-int(find(record(q3),record1(w3)))
    if control <= 0:
        print('out of horizont')
    else:
        print(control) 
    while True:#повтор коду
        try:
            answer=int(input('if you want continue print 1'))
            break
        except ValueError:
            continue
    if answer != 1:
        print('goodbye')
    else:
        roun(q1,w1,q2,w2,q3,w3)
    return 

x1=int(0)
x2=int(0)
x3=int(0)
y1=int(0)
y2=int(0)
y3=int(0)


roun(x1,y1,x2,y2,x3,y3)



    
            

            
