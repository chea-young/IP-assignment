from datetime import datetime, timedelta

def most_frequent_days(year):
    day = ['Sunday','Monday','Tuseday','Wednesday','Thursday','Friday','Saturday']
    time1 = datetime(1583, 1, 1, 0, 0, 0)
    time2 = datetime(year,1,1,0,0)
    m_day = (time2-time1).days
    start_day = 0

    if(m_day%7==1):
        start_day = 0
    elif(m_day%7==2):
        start_day = 1
    elif(m_day%7==3):
        start_day = 2
    elif(m_day%7==4):
        start_day = 3
    elif(m_day%7==5):
        start_day = 4
    elif(m_day%7==6):
        start_day = 5
    elif(m_day%7==0):
        start_day = 6

    print(start_day)
    now_year = 365
    if(year %4 ==0):
        now_year = 366
    day_num = [0,0,0,0,0,0,0]
    for i in range(now_year):
        if(i%7 ==1):
            day_num[1]+=1
        elif(i%7==2):
            day_num[2] +=1
        elif(i%7==3):
            day_num[3] +=1
        elif(i%7==4):
            day_num[4] +=1
        elif(i%7==5):
            day_num[5] +=1
        elif(i%7==6):
            day_num[6] +=1
        elif(i%7==0):
            day_num[0] +=1

    day_name = [day[start_day]]
    if(now_year ==366):
        if(start_day+1 > 6):
            start_day = -1
        day_name.append(day[start_day+1])

    return day_name

if __name__ == '__main__':
    print(most_frequent_days(2427))
    print(most_frequent_days(2185)) 
    print(most_frequent_days(1770))
    print(most_frequent_days(1785)) 
    print(most_frequent_days(1984))  
    print(most_frequent_days(2000)) 
      
def test_q():
    assert most_frequent_days(2427) == ['Friday']
    assert most_frequent_days(2185) == ['Saturday']
    assert most_frequent_days(1770) == ['Monday']
    assert most_frequent_days(1785) == ['Saturday']
    assert most_frequent_days(1984) == ['Monday', 'Sunday']
    assert most_frequent_days(2000) == ['Saturday', 'Sunday']