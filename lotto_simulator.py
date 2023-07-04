import random as r
print('\t<로또 복권 당첨 시뮬레이터>\n')
print('Enter 버튼을 누를 때마다 복권 당첨 결과가 나옵니다\n')
print('\'x\' Enter 입력 시 추첨이 종료됩니다')
print('\'m\' Enter 입력 시 잔액을 알려드립니다')
print('\'r\' Enter 입력 시 모든 것이 리셋됩니다')
print('\'h\' Enter 입력 시 도움말을 펼칩니다')
print('\n1등: 1/8145060\n2등: 1/1357510\n3등: 1/35724\n4등: 1/733\n5등: 1/45\n\n현재 나의 용돈: 1000만원\n복권 한장 가격: 5000원')

a777 = '1'
trynum = 0
win1 = 0
win2 = 0
win3 = 0
win4 = 0
win5 = 0
nope6 = 0
money = 10000000

def zz(a) : # 절댓값 함수 선언
    if a < 0 :
        return -a
    else :
        return a
    
while a777 != 'x' :
    a777 = input('')
    if a777 != 'x' and a777 != 'm' and a777 != 'r' and a777 != 'h' :
        s = 0
        b = 0
        trynum = trynum + 1
        money = money - 5000
        a1 = r.randint(1,45)
        a2 = r.randint(1,45)
        while a1 == a2 :
            a2 = r.randint(1,45)
        a3 = r.randint(1,45)
        while a1 == a3 or a2 == a3 :
            a3 = r.randint(1,45)
        a4 = r.randint(1,45)
        while a1 == a4 or a2 == a4 or a3 == a4 :
            a4 = r.randint(1,45)
        a5 = r.randint(1,45)
        while a1 == a5 or a2 == a5 or a3 == a5 or a4 == a5 :
            a5 = r.randint(1,45)
        a6 = r.randint(1,45)
        while a1 == a6 or a2 == a6 or a3 == a6 or a4 == a6 or a5 == a6 :
            a6 = r.randint(1,45)

        aa1 = r.randint(1,45)
        aa2 = r.randint(1,45)
        while aa1 == aa2 :
            aa2 = r.randint(1,45)
        aa3 = r.randint(1,45)
        while aa1 == aa3 or aa2 == aa3 :
            aa3 = r.randint(1,45)
        aa4 = r.randint(1,45)
        while aa1 == aa4 or aa2 == aa4 or aa3 == aa4 :
            aa4 = r.randint(1,45)
        aa5 = r.randint(1,45)
        while aa1 == aa5 or aa2 == aa5 or aa3 == aa5 or aa4 == aa5 :
            aa5 = r.randint(1,45)
        aa6 = r.randint(1,45)
        while aa1 == aa6 or aa2 == aa6 or aa3 == aa6 or aa4 == aa6 or aa5 == aa6 :
            aa6 = r.randint(1,45)
        aa7 = r.randint(1,45)
        while aa1 == aa7 or aa2 == aa7 or aa3 == aa7 or aa4 == aa7 or aa5 == aa7 or aa6 == aa7 :
            aa7 = r.randint(1,45)

        if aa1 == a1 or aa1 == a2 or aa1 == a3 or aa1 == a4 or aa1 == a5 or aa1 == a6 :
            s = s + 1
        if aa2 == a1 or aa2 == a2 or aa2 == a3 or aa2 == a4 or aa2 == a5 or aa2 == a6 :
            s = s + 1
        if aa3 == a1 or aa3 == a2 or aa3 == a3 or aa3 == a4 or aa3 == a5 or aa3 == a6 :
            s = s + 1
        if aa4 == a1 or aa4 == a2 or aa4 == a3 or aa4 == a4 or aa4 == a5 or aa4 == a6 :
            s = s + 1
        if aa5 == a1 or aa5 == a2 or aa5 == a3 or aa5 == a4 or aa5 == a5 or aa5 == a6 :
            s = s + 1
        if aa6 == a1 or aa6 == a2 or aa6 == a3 or aa6 == a4 or aa6 == a5 or aa6 == a6 :
            s = s + 1
        if aa7 == a1 or aa7 == a2 or aa7 == a3 or aa7 == a4 or aa7 == a5 or aa7 == a6 :
            b = 1

        if s == 6 :
            print('1등 당첨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n상금은 10억원 입니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            win1 = win1 + 1
            money = money + 1000000000
        elif s == 5 and b == 1 :
            print('2등 당첨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n상금은 5천만원 입니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            win2 = win2 + 1
            money = money + 50000000
        elif s == 5 and b == 0 :
            print('3등 당첨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n상금은 100만원 입니다!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            win3 = win3 + 1
            money = money + 1000000
        elif s == 4 :
            print('4등 당첨!!!!!!!!!! 상금은 5만원 입니다!!!!!')
            win4 = win4 + 1
            money = money + 50000
        elif s == 3 :
            print('5등 당첨!!! 상금은 5천원 입니다!!')
            win5 = win5 + 1
            money = money + 5000
        else :
            print('꽝')
            nope6 = nope6 + 1
            
    elif a777 == 'm' :
        print('복권 구매 {}번  -{}원\n'.format(trynum,5000*trynum))
        if win1 == 0 :
            print('1등 0번  +0원')
        else :
            print('1등 {}번  +{}억원'.format(win1,win1*10))
        wwin2 = win2 # 바뀌어도 되는 2등 횟수 변수 선언
        wwwin2 = 0 # 억단위의 변수 선언
        if win2 == 0 :
            print('2등 0번  +0원')
        
        elif win2 < 2 :
            print('2등 {}번  +{}천만원'.format(win2,win2*5))
        else :
            while wwin2 >= 2 :
                wwin2 = wwin2 - 2
                wwwin2 = wwwin2 + 1
            if wwin2 == 0 :
                print('2등 {}번  +{}억원'.format(win2,wwwin2))
            if wwin2 == 1 :
                print('2등 {}번  +{}억 {}천만원'.format(win2,wwwin2,wwin2*5))
        if win3 == 0 :
            print('3등 0번  +0원')
        else :
            print('3등 {}번  +{}만원'.format(win3,win3*100))
        if win4 == 0 :
            print('4등 0번  +0원')
        else :
            print('4등 {}번  +{}만원'.format(win4,win4*5))
        wwin5 = win5 # 바뀌어도 되는 5등 횟수 변수 선언
        wwwin5 = 0 # 만단위의 변수 선언
        if win5 == 0 :
            print('5등 0번  +0원')
        elif win5 < 2 :
            print('5등 {}번  +{}천원'.format(win5,win5*5))
        else :
            while wwin5 >= 2 :
                wwin5 = wwin5 - 2
                wwwin5 = wwwin5 + 1
            if wwin5 == 0 :
                print('5등 {}번  +{}만원'.format(win5,wwwin5))
            if wwin5 == 1 :
                print('5등 {}번  +{}만 {}천원'.format(win5,wwwin5,wwin5*5))
        print('꽝 {}번\n'.format(nope6))
       
        zzmoney = zz(money)
        okk = man = 0
        while zzmoney >= 100000000 :
            zzmoney = zzmoney - 100000000
            okk = okk + 1
        while zzmoney >= 10000 :
            zzmoney = zzmoney - 10000
            man = man + 1
        if money < 0 :
            if zzmoney != 0 :
                if okk != 0 and man != 0 :
                    print('잔액 -{}억 {}만 {}원\n'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 -{}억 {}원\n'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 -{}만 {}원\n'.format(man,zzmoney))
                else :
                    print('잔액 -{}원\n'.format(zzmoney))
            else :
                if okk != 0 and man != 0 :
                    print('잔액 -{}억 {}만원\n'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 -{}억원\n'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 -{}만원\n'.format(man,zzmoney))
                else :
                    print('잔액 -{}원\n'.format(zzmoney))
        else :
            if zzmoney != 0 :
                if okk != 0 and man != 0 :
                    print('잔액 {}억 {}만 {}원\n'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 {}억 {}원\n'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 {}만 {}원\n'.format(man,zzmoney))
                else :
                    print('잔액 {}원\n'.format(zzmoney))
            else :
                if okk != 0 and man != 0 :
                    print('잔액 {}억 {}만원\n'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 {}억원\n'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 {}만원\n'.format(man,zzmoney))
                else :
                    print('잔액 {}원\n'.format(zzmoney))

    elif a777 == 'r' :
        print('리셋을 하면 잔액이 1000만원으로 초기화되고\n복권 현황도 전부 0개로 초기화됩니다\n')
        print('정말로 리셋하시겠습니까?\n')
        reset = input('1을 누르면 리셋합니다 : ')
        if reset == '1' :
            trynum = 0
            win1 = 0
            win2 = 0
            win3 = 0
            win4 = 0
            win5 = 0
            nope6 = 0
            money = 10000000
            print('성공적으로 리셋되었습니다')
        else :
            print('리셋이 실패했습니다')

    elif a777 == 'h' :
        print('\t<로또 복권 당첨 시뮬레이터>\n')
        print('Enter 버튼을 누를 때마다 복권 당첨 결과가 나옵니다\n')
        print('\'x\' Enter 입력 시 추첨이 종료됩니다')
        print('\'m\' Enter 입력 시 잔액을 알려드립니다')
        print('\'r\' Enter 입력 시 모든 것이 리셋됩니다')
        print('\'h\' Enter 입력 시 도움말을 펼칩니다')
        print('\n1등: 1/8145060\n2등: 1/1357510\n3등: 1/35724\n4등: 1/733\n5등: 1/45\n')
        zzmoney = zz(money)
        okk = man = 0
        while zzmoney >= 100000000 :
            zzmoney = zzmoney - 100000000
            okk = okk + 1
        while zzmoney >= 10000 :
            zzmoney = zzmoney - 10000
            man = man + 1
        if money < 0 :
            if zzmoney != 0 :
                if okk != 0 and man != 0 :
                    print('잔액 -{}억 {}만 {}원\n복권 한장 가격: 5000원'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 -{}억 {}원\n복권 한장 가격: 5000원'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 -{}만 {}원\n복권 한장 가격: 5000원'.format(man,zzmoney))
                else :
                    print('잔액 -{}원\n복권 한장 가격: 5000원'.format(zzmoney))
            else :
                if okk != 0 and man != 0 :
                    print('잔액 -{}억 {}만원\n복권 한장 가격: 5000원'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 -{}억원\n복권 한장 가격: 5000원'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 -{}만원\n복권 한장 가격: 5000원'.format(man,zzmoney))
                else :
                    print('잔액 -{}원\n복권 한장 가격: 5000원'.format(zzmoney))
        else :
            if zzmoney != 0 :
                if okk != 0 and man != 0 :
                    print('잔액 {}억 {}만 {}원\n복권 한장 가격: 5000원'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 {}억 {}원\n복권 한장 가격: 5000원'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 {}만 {}원\n복권 한장 가격: 5000원'.format(man,zzmoney))
                else :
                    print('잔액 {}원\n복권 한장 가격: 5000원'.format(zzmoney))
            else :
                if okk != 0 and man != 0 :
                    print('잔액 {}억 {}만원\n복권 한장 가격: 5000원'.format(okk,man,zzmoney))
                elif okk != 0 and man == 0 :
                    print('잔액 {}억원\n복권 한장 가격: 5000원'.format(okk,zzmoney))
                elif okk == 0 and man != 0 :
                    print('잔액 {}만원\n복권 한장 가격: 5000원'.format(man,zzmoney))
                else :
                    print('잔액 {}원\n복권 한장 가격: 5000원'.format(zzmoney))

    elif a777 == 'x' :
        
        print('정말로 종료하시겠습니까?\n')
        exitt = input('1을 누르면 종료합니다 : ')
        if exitt == '1' :
            
            print('='*50)
        else :
            print('추첨을 계속합니다\n')
            a777='1'



