import socket
import msg

def client(server_addr):
    """Client - read more date after shut-down
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process

    sent_bytes = []
    recv_bytes = []
    for message in msg.msgs(20, length=2000):  # generate 20 msgs
        n_sent = sock.send(message)          # send message to server(outgoing 스트림)
        sent_bytes.append(n_sent)
        data = sock.recv(2048)      # receive response from server(incoming스트림) 
        if not data:                # check if server terminates abnormally(fin을 내가 보내지 않았는데 에코 서비가 fin을 보내면)(서버가 비정상적으로 먼저 종류된거 아마 서버 프로세스가 죽은거)
            print('Server abnormally terminated')
            break
        recv_bytes.append(len(data))
    else:# for문 나오기 전에 else 감
        # Now all the messages sent. Terminate outgoing TCP connection.
        sock.shutdown(socket.SHUT_WR) # send eof mark (FIN) (WR 보내는 방향으로 shutdown 하겠다.)(서버가 내가 받는 스트림의 끝이라는 것을 알게된다.)
        # Receive more for the remaining messages
        while True:# 서버가 fin을 보낼 때 까지 기다린다.
            data = sock.recv(2048)
            if not data:
                break
            recv_bytes.append(len(data))
    sock.close()
    msg.report(sent_bytes, recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7))
