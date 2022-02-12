
def vvod_XO(bukva_,n):
    x=int(input('куда поставить' + ' '+ bukva_ +'?'))
    if not(x<=n**2 or x>0):
       print('введи адекватное число')
       vvod_XO(bukva_)       
    else:
       array[x-1]=bukva_

def vuvod_stroka(setk_,k): 
    stroka='|'
    for i in range(k,k+setk_):
        stroka+=str(array[i])
        
        stroka+='|'
    return stroka

def ToConsoleArray(setk):
    
    t=0
    for i in range(setk):
        stroka=vuvod_stroka(setk,t)
        print(stroka)
        t+=setk

def win(win_combinations):   
    for i in range(len(win_combinations)-1):
        if win_combinations[i]!=win_combinations[i+1]:
            return False
    return True

def predwin(n):
    k=0
    mass=[]
    for i in range(n):
        for s in range(k,k+n):
            mass.append(array[s])
        if win(mass):
            return True
        else:
            k+=n

    mass.clear
    for i in range(n):        
        for s in range(i,i+n(n-1)+1,n):
            mass.append(array[s])
        if win(mass):
            return True

    mass.clear
    for i in range(0,n**2,n+1):
        mass.append(array[s])
    if win(mass):
            return True

    mass.clear
    for i in range(n-1,n**2-n+1,n-1):
        mass.append(array[s])
    if win(mass):
            return True
        
    return False


setka=int(input('введи размер желаемого поля'))
array=[]
for i in range(1,setka**2+1):
    array.append(i)
ToConsoleArray(setka)
count=0
while True:
    if count%2==0:
        vvod_XO('X',setka)
        
        count+=1
    else:
        vvod_XO('O',setka)
        count+=1
    ToConsoleArray(setka)    
    if predwin(setka):
       print('Win!')
       break




    
