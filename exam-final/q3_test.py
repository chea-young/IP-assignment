def ipv4_address(address):
    iplist = address.split('.')
    if(len(iplist) != 4):
        return False
    if( '' in iplist):
        return False
    for i in iplist:
        int_i = int(i)
        if(int_i<=255 and int_i>= 0):
            if(i != str(int_i)):
                return False
        else:
            return False
    return True

def test_q():
    assert ipv4_address("") == False
    assert ipv4_address("127.0.0.1") == True
    assert ipv4_address("0.0.0.0") == True
    assert ipv4_address("255.255.255.255") == True
    assert ipv4_address("10.20.30.40") == True
    assert ipv4_address("10.256.30.40") == False
    assert ipv4_address("10.20.030.40") == False
    assert ipv4_address("127.0.1") == False
    assert ipv4_address("127.0.0.0.1") == False
    assert ipv4_address("..255.255") == False
    assert ipv4_address("127.0.0.1\n") == False
    assert ipv4_address("\n127.0.0.1") == False
    assert ipv4_address(" 127.0.0.1") == False
    assert ipv4_address("127.0.0.1 ") == False
    assert ipv4_address(" 127.0.0.1 ") == False    