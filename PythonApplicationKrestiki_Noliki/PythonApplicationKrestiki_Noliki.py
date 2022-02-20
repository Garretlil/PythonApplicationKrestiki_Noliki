setka=int(input('введи размер желаемого поля: '))


def vvod_XO(bukva_,n):
    x=int(input('куда поставить' + ' '+ bukva_ +'?'))
    if not(x<=n**2 and x>0):
       print('введи адекватное число')
       vvod_XO(bukva_,n)       
    else:
       array[x-1]=bukva_

def ResearchOfSize(current_element,maxlensymbol_):    
    dlina=len(str(current_element))
    return maxlensymbol_-dlina


def vuvod_stroka(setka_,k): 
    stroka='|'
    maxlensymbol=len(str(setka_**2))
    for i in range(k,k+setka_):
        stroka+=str(array[i])
        stroka+=' '*ResearchOfSize(array[i],maxlensymbol)
        stroka+='|'
    return stroka

def ToConsoleArray(setk):    
    t=0
    for i in range(setk):
        stroka=vuvod_stroka(setk,t)
        print(stroka)
        t+=setk

def askwin(win_combinations):   
    for i in range(len(win_combinations)-1):
        if win_combinations[i]!=win_combinations[i+1]:
            return False
    return True

def win(n):
    k=0
    mass=[]
    # проверка по строкам
    for i in range(n):
        for s in range(k,k+n):
            mass.append(array[s])
        if askwin(mass):
            return True
        else:
            k+=n

    mass.clear
        # проверка по столбцам
    for i in range(n):        
        for s in range(i,i+n*(n-1)+1,n):
            mass.append(array[s])
        if askwin(mass):
            return True

    mass.clear
     # проверка по диагоналям
    for i in range(0,n**2,n+1):
        mass.append(array[i])
    if askwin(mass):
            return True

    mass.clear
    for i in range(n-1,n**2-n+1,n-1):
        mass.append(array[i])
    if askwin(mass):
            return True
        
    return False

array=[]
for i in range(1,setka**2+1):
    array.append(i)
ToConsoleArray(setka)
CheiHod=True
SetValue=""

while True:
    if CheiHod:
        SetValue="X"  
    else:
        SetValue="O" 
    CheiHod= not CheiHod    
    vvod_XO(SetValue,setka)
 
    ToConsoleArray(setka)    
    if win(setka):
       print('Win!')
       break




    
