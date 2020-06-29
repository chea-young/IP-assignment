def get_count(input_str):
    list1 = "aeiou"
    count = 0
    if(input_str == None) :
        return 0

    for i in input_str:
        if(i in list1):
            count +=1
    return count

# tester provided
def test_sample():
    assert get_count("abracadabra") == 5
    assert get_count("") == 0
    assert get_count("bcd,! ?") == 0
    assert get_count("pear tree") == 4
    assert get_count("o a kak ushakov lil vo kashu kakao") == 13
