import sys, socket

def echo_client(server_addr):
    """Echo client"""
    # make TCP/IP socket obj
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #소켓 스트링 생성, TCP형 소켓이라는 것이 정의하고 밑에서 서버하고 connect
    sock.connect(server_addr)   # connect to server process
    print(sock)
    while True:
        message = sys.stdin.readline()
        if not message:
            break
        sock.send(message.encode('utf-8'))      # send message to server
        data = sock.recv(1024).decode('utf-8')  # receive response up to 1KB
        print(data)
    sock.close()                # send FIN(no more data) and close the socket
    
if __name__ == '__main__':
    echo_client(('localhost', 10007)) #10007번이라는 서버 address줌
    # echo_client(('np.hufs.ac.kr', 7))

"""
cd intro
python echocli.py 하면 이것만 하면 거절됨 이유는 10007 기다리고 listening 소켓이 없어서 연결이 거부
서버를 돌리고 이걸 해야된다. 하면 connect
socket.socket fd 프로세서에 local에 새로운게 계속 붙는다 이게 진짜 커널에 있는 소켓
0, laddr 이 local address raddr 이게 remote address
# 순서가 accept를 하는 와중에 connent를 해서 tcp연결이 완료된거를 하나를 가져와서 conn send recv 할 수 있게 된거 
conn는 0, laddr = ('127.0.) raddr =('127.0.0.1',59048) 이렇게 print
readline에서 기다리명 recv에서 기다림 blocked client가 일해서 보내주면 (empty string이면 while문 빠져나온다.)(socket은 받을 때 줄 때 utf-8 해야한다.)
client가 send하고 커널한테 전달해줌(tcp 버퍼에 넣어줌, send 버퍼에 넣어줬다는 뜻 나중에 시간이 될 때 넣어줘) recv를 기다리는거
서버에 recv 버퍼에 있으면 최대 1024바이트까지만 copy 할 게, decode 하서 찍어봄 그러고 send(data)를 클라이언트로 보내줌
클라이언트는 zero byte 로 돌리면 멈춘다.(ctrl+z zero뭐 어쩌구 저쩌구)
socket.close() 상대방에게 이게 끝이라고 보내주는 것 그래서 서버가 zero length data로 받아서 끝냄 또 accept를 보낸다.
그래서 client만 다시 돌리면 된다
이때 또 다른 클라이언트를 돌리면 전에 만약에 전에 클라이어트랑 connect가 되어있으면 while문안에 있으면 다른 클라이언트를 받지 못한다. conn.recv 상태라서 계속 기다리고 있어서
client를 서버를 다 받을 수 있어야 하는데 현재 코드는 하나만 받을 수 있도록 되어있다. 원래 n개의 소켓을 받을 수 있어야 되는데 어떤 blocked에서도 멈추지 않고
하나의 client와 server가 connection되면 다른얘를 받지 못한다. 서버는 죽지않고 영원히 돌아간다. exception이 있어도 handler가 돌아서demon 프로세스가 돌아서 죽지 않아야 한다pygame.examples.aliens.main()
리녹스는 ctrl+c 써서 죽을 수 있는데 다른얘는 아닐 때도 있다. ctrl+break를 하면 죽일 수 있다. 안전하게는 그냥 terminal 자체를 죽이는게 안전하다.
"""

