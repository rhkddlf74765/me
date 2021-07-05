from random import*
from tkinter import*
def tk():
    window=Tk()
    button=Button(window,text="네",command=main)
    label=Label(window,text="돌리겠습니까?")
    button.pack(side=BOTTOM)
    label.pack(side=TOP)
    window.mainloop()
TOTALLIST=['str','dex','int','luk',['str','dex'],['str','int'],['str','luk'],['dex','int'],['dex','luk'],['int','luk'],'착용렙 감소','공격력','마력','보공','데미지','올스텟']
def choose():#숫자
   a=randint(1,14)#a는 1초과 15미만
   b=randint(0,a-1)#b는 위쪽에 있는거
   c=randint(a+1,15)#c는 아래에 있는거
   return b,a,c
def weight(choosenum,weightlist):
    if choosenum<4:
        weightlist.append((TOTALLIST[choosenum],randint(10,70)))
    elif choosenum<10:
        a=randint(10,70)
        weightlist.append((TOTALLIST[choosenum][0],a))
        weightlist.append((TOTALLIST[choosenum][1],70-a))
    elif choosenum==10 :
        aaa=randint(0,5)
        wearlist=[5,10,15,20,25,30]
        weightlist.append((TOTALLIST[choosenum],wearlist[aaa]))
    elif choosenum==11:
        weightlist.append((TOTALLIST[choosenum],randint(1,7)))
    elif choosenum==12:
        weightlist.append((TOTALLIST[choosenum],randint(1,7)))
    elif choosenum==13:
        aaa=randint(0,1)
        bosslist=[5,10]
        weightlist.append((TOTALLIST[choosenum],bosslist[aaa]))
    elif choosenum==14:
        weightlist.append((TOTALLIST[choosenum],randint(1,7)))
    elif choosenum==15:
        weightlist.append((TOTALLIST[choosenum],randint(1,7)))
def final(list):
    lll=[]
    ttt=[]
    aaa=len(list)
    for i in range(aaa):
        for a in range(i+1,aaa):
            if list[i][0]==list[a][0]:
                lll.append((list[i][0],list[i][1]+list[a][1]))
                ttt.append(list[i][0])
    for i in range(aaa):
        if list[i][0] not in ttt:
            lll.append(list[i])
    dic=dict(lll)
    return dic
def main():
    choosen=choose()
    weightlist=[]
    for i in choosen:
        weight(i,weightlist)
    dic=final(weightlist)
    for i in dic:
        print(f'{i} : +{dic[i]}')
    print()
tk()