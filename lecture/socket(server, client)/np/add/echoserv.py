"""Serve only one client at a time
"""
#여기가 소켓
from socket import socket, AF_INET, SOCK_STREAM

def echo_server(my_port):   
    """Echo Server - iterative"""

    sock = socket(AF_INET, SOCK_STREAM) # socket for listening clients' connection (TCP 패킷으로 만드는 것은 echocli와 동일한데 밑에 bind가 다르다)
    sock.bind(('', my_port))        # bind it to my any IP and port number (주어진 parameter대로 bind해라 내 소켓한테, '' 이거는 내 ip 아무거나)
    # 내 ip는 ipconfig /all
                                    # '' represents all available interfaces on host
    sock.listen(5)                  # listen, allow 5 pending connects( listening 소켓으로 바꿔라 client가 connection하는 걸 listening하는 소켓)(5개 queue, 꼭 5개는 아니라 많은 거를 accept)
    print('Server started')
    while True:                     # do forever (until process killed)
        conn, cli_addr = sock.accept()  # wait for next client connect (connection한걸 받아드림, 그리고 return, 이걸 accept하는 거는 listening 소켓)
                                    # conn: new socket, addr: client addr(이거는 connected 소켓, 얘는 send recv 가능(주고 받는거))
                                    #cli_addr 상대측 클라이언트 address
        print(conn)
        print('Connection from', cli_addr)
        while True:
            data = conn.recv(1024)  # recv next message on connected socket
            if not data:
                break               # no more data. TCP FIN arrival
            print(data.decode(), end='')
            conn.send(data)         # send a reply to the client
        print('Client closed', cli_addr)
        conn.close()               # close the connected socket
        
if __name__ == '__main__':
    echo_server(10007)

"""
# cd intro
# python echoserrv.py
''이거는 0.0.0.0으로 표시 my_port는 10007
"""

