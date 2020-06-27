import socket
import msg

def client(server_addr):
    """Client - converting to file-like object to allow buffered I/O

    Assumption: request/response messages ending with LF
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process
    # file-like obj in read/write binary mode  
    # Note: binary mode preserve the data (not convert encodings and line ending)
   #버퍼 2개 생성
    rfile = sock.makefile('rb')    # incoming stream
    wfile = sock.makefile('wb')   # outgoing stream
    sent_bytes = []
    recv_bytes = []
    for message in msg.msgs(20, length=2000):
        n_sent = wfile.write(message)# 지금 버퍼링만 되있는거(newline으로 끝난다. 경계가 있다.)
        wfile.flush()     # flush-out user buffer to send immediately ( 버퍼링 된거를 바로 내보내라는거 모아둔것을 send해서)(이거 안하면 밖으로 안나갈지도 모른다.)
        sent_bytes.append(n_sent) #(newline이 버퍼링해서 끄집어 내서 올 때까지 기다린다.)
        data = rfile.readline()     # incoming line message(newline까지 할 때는 revc가 안할지 몇번 할 수도 있다.)(보내고 stop and wait(new line을))
        #stop and wait가 아닌 pipeline을 하려면 outgoing 스트림과 incoming 스트림을 독립적으로 다뤄야 한다. 이걸 쉽게 구현하는 것이 thread이다.
        if not data:                 # check if server terminates abnormally
            print('Server abnormally terminated')
            break
        recv_bytes.append(len(data)) #보낸만큼 오게 될 것이다.
    sock.close()
    msg.report(sent_bytes, recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7))
