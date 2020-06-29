def ipv4_address(address):
    pass

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