def most_frequent_days(year):
    day = ['Sunday,','Monday','Tuseday','Wednesday','Thursday','Friday','Saturday']
    start = 1
    # 윤년 갯수 세기
    a_year = 0
    for i in range(1583,year+1):
        if(i %4 == 0):
            a_year +=1
    
    all_year = year-1583
    not_a = all_year-a_year
    all_day = not_a*365 + a_year*366

    now_year = 365
    if(year %4 ==0):
        now_year = 366
    m_day = all_day-now_year
    start_day = 0
    if(m_day%7==1):
        start_day = 6
    elif(m_day%7==2):
        start_day = 0
    elif(m_day%7==3):
        start_day = 1
    elif(m_day%7==4):
        start_day = 2
    elif(m_day%7==5):
        start_day = 3
    elif(m_day%7==6):
        start_day = 4
    elif(m_day%7==0):
        start_day = 5
    print(start_day)

    day_num = [0,0,0,0,0,0,0]
    for i in range(now_year):
        if(i%7 ==1):
            day_num[6]+=1
        elif(i%7==2):
            day_num[0] +=1
        elif(i%7==3):
            day_num[1] +=1
        elif(i%7==4):
            day_num[2] +=1
        elif(i%7==5):
            day_num[3] +=1
        elif(i%7==6):
            day_num[4] +=1
        elif(i%7==0):
            day_num[5] +=1

    day_name = []
    max_num = max(day_num)
    ans_num = day_num.count(max_num)
    for i in range(ans_num):
        index = day_num.index(max_num)
        index = index+start_day-2
        if(index>7):
            index-=7
        day_name.append(day[index])
        del day[index]

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