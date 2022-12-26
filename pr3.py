from random import *
def nnn(alf,a,b):
    a=a.upper()
    new_a=''
    for i in range(len(a)):
        if alf.find(a[i])!=-1:
            new_a+=str(a[i])
#удаление всех символов не входящих в алфавит
    seed(b)
    s=[]
    shifr=''
    for i in range(len(new_a)):
        s.append(randrange(0,33))
    #print(s)
    if zapros=='1':
        for i in range(len(new_a)):
            if alf.find(new_a[i])+s[i]+1>34:
                shifr+=alf[alf.find(new_a[i])+s[i]-34]
            else:
                shifr+=alf[alf.find(new_a[i])+s[i]]
        return (shifr)
#зашифровка текста
    elif zapros=='0':
        for i in range(len(new_a)):
            if alf.find(new_a[i])-s[i]+1<0:
                shifr+=alf[alf.find(new_a[i])-s[i]+34]
            else:
                shifr+=alf[alf.find(new_a[i])-s[i]]
        return (shifr)
#расшифровка текста
print('если шифр введите - 1')
print('если расшифр - 0')
zapros=input()
alf='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ '
print('введите исходный текст для зашифровки/расшифровки:')
tekst=input()
print('введите ключ:')
key=input()
print('зашифрованный/расшифрованный текст -',nnn(alf,tekst,key))
