
"""
보낸 만큼 서버가 받는 것은 아니다!!
"""

import socket
import msg

def client(server_addr):
    """Incorrect client
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process

    sent_bytes = []#몇 바이트를 sent했는지 알기위해 list를 만듬
    recv_bytes = []
    for message in msg.msgs(100, length=1400):  # generate 100 msgs(메세지 모듈은 local에 length가 100인)
        n_sent = sock.send(message) # send message to server
        sent_bytes.append(n_sent) #몇 바이트로 보냈는지 나온다.
        data = sock.recv(2048)      # receive response from server 최대 2048까지 받을 수 있는데 이걸 append
        recv_bytes.append(len(data))
    #sock.close() 이렇게 하면 밑에 data에 empty 데이터가 오게된다.그래서 shutdown 써서 해야한다.
    while True:
        data = sock.recv(2048)
        if not data:
            break
    sock.close()                    # send eof mark (FIN), fin을 보내는 거, 끝내자, 더이상 보낼 게 없다는 뜻 (이거전에는 계속 받는다.)

    msg.report(sent_bytes, recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7)) 

"""잘 못 구현된 이유
python client_wrong.py 보낸만큼 받아야 한다. 총 140000만 바이트를 보냈는데 hash써서 보니깐 다 못 받음 -> send 저장하는 것(버퍼링만 성공)이지 실제로 상대방에게 
다 전달되는 것은 아니다. recv에 있으면 데이터를 꺼내보니깐 보낸만큼 받은 것이 아니였던 것 
그래서 받는 양이 다양한데 2048까지만 받을 수 있는거 어떨땐 적기도 하고 어떨땐 크기도 한거 """
"""돌리기 cd echo/clients"""
#양방향 서비스를 제공한다.
