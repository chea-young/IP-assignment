def square_digits(num):
    count_str = ''
    for i in str(num):
        int_i = int(i)
        count_str += str(int(i)*int(i))
    return int(count_str)

def test_q1():
    assert square_digits(9119) == 811181
