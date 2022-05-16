year=int(input('년도를 입력하세요(숫자만 입력): '))
month=int(input('월을 입력하세요(숫자만 입력): '))
day=int(input('일을 입력하세요(숫자만 입력): '))

if year%400==0:
    if month==2:
        if day==29:
            print('%d-3-1' %year)
        elif 1<=day<29:
            print('%d-3-%d' %(year, (day+1)))
    elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
        if day==31:
            print('%d-%d-1' %(year, (month+1)))
        elif 1<=day<31:
            print('%d-%d-%d' %(year, month, (day+1)))
    elif  month==4 or month==6 or month==9 or month==11:
        if day==30:
            print('%d-%d-1' %(year, (month+1)))
        elif 1<=day<30:
            print('%d-%d-%d' %(year, month, (day+1)))
    elif month==12:
        if day==31:
            print('%d-1-1' %(year+1))
        elif 1<=day<31:
            print('%d-%d-%d' %(year, month, (day+1)))
else:
    if year%4==0:
        if year%100==0:
            if month==2:
                if day==28:
                    print('%d-3-1' %year)
                elif 1<=day<28:
                    print('%d-3-%d' %(year, (day+1)))
            elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                if day==31:
                    print('%d-%d-1' %(year, (month+1)))
                elif 1<=day<31:
                    print('%d-%d-%d' %(year, month, (day+1)))
            elif  month==4 or month==6 or month==9 or month==11:
                if day==30:
                    print('%d-%d-1' %(year, (month+1)))
                elif 1<=day<30:
                    print('%d-%d-%d' %(year, month, (day+1)))
            elif month==12:
                if day==31:
                    print('%d-1-1' %(year+1))
                elif 1<=day<31:
                    print('%d-%d-%d' %(year, month, (day+1)))
        else:
            if month==2:
                if day==29:
                    print('%d-3-1' %year)
                elif 1<=day<29:
                    print('%d-3-%d' %(year, (day+1)))
            elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
                if day==31:
                    print('%d-%d-1' %(year, (month+1)))
                elif 1<=day<31:
                    print('%d-%d-%d' %(year, month, (day+1)))
            elif  month==4 or month==6 or month==9 or month==11:
                if day==30:
                    print('%d-%d-1' %(year, (month+1)))
                elif 1<=day<30:
                    print('%d-%d-%d' %(year, month, (day+1)))
            elif month==12:
                if day==31:
                    print('%d-1-1' %(year+1))
                elif 1<=day<31:
                    print('%d-%d-%d' %(year, month, (day+1)))
    else:
        if month==2:
            if day==28:
                print('%d-3-1' %year)
            elif 1<=day<28:
                print('%d-3-%d' %(year, (day+1)))
        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10:
            if day==31:
                print('%d-%d-1' %(year, (month+1)))
            elif 1<=day<31:
                print('%d-%d-%d' %(year, month, (day+1)))
        elif  month==4 or month==6 or month==9 or month==11:
            if day==30:
                print('%d-%d-1' %(year, (month+1)))
            elif 1<=day<30:
                print('%d-%d-%d' %(year, month, (day+1)))
        elif month==12:
            if day==31:
                print('%d-1-1' %(year+1))
            elif 1<=day<31:
                print('%d-%d-%d' %(year, month, (day+1)))
