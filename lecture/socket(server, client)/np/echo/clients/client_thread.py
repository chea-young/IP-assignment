import socket, threading
import msg
import sys
sent_bytes = []
recv_bytes = []

def recv_loop(sock):#스레드를 쓰는것 os가 만들어줘서 독립적으로 돌아가는 얘(새로운 thread로 돌아감)
    print('recv thread started')
    while True:
        data = sock.recv(2048)     # receive response() (이걸 키우면은 성능이 좋아진다.)
        if not data:# 데이터가 끝날 떄까지 받는다.
            print('Server closing')
            break
        recv_bytes.append(len(data))
        #print('recv:', len(data))
    print("recv_loop terminated")# return되며 끝난다.

def client(server_addr): #(메인 thread로 돌아가고)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)         # connect to server process

    receiver = threading.Thread(target=recv_loop, args=(sock,)) #recv_loop 함수에 튜플로 보냄, Thread의 서브 클래스로 만드는 것
    receiver.start()    # start recv_loop thread(start메소드를 부름)

    # main thread continues hereafter
    #for message in msg.msgs(20, length=2000):
        #n_sent = sock.send(message)
    while(True):
        #message = sys.stdin.readline()
        #n_sent = sock.send(message)
        message = sys.stdin.readline()
        if not message:     # reading 0 bytes means EoF
            break
        sock.send(message.encode('utf-8'))      # send message to server
        data = sock.recv(1024).decode('utf-8')
        #sent_bytes.append(n_sent)
        print(data)
    print("sending loop terminated")
    sock.shutdown(socket.SHUT_WR)     # send FIN. This will stop receiver thread
    receiver.join()                   # wait for receiver exit(메인 thread가 reiver가 끝날 때 까지 기다리는 것)(이거 없으면 더 받아야하는데 그냥 끝나버린다.)(이거 이후 child thread 도 끝나는 거)
    sock.close()
    print('Client terminated')
    #msg.report(sent_bytes, recv_bytes)

if __name__ == '__main__':
    #client(('np.hufs.ac.kr', 7))
    client(('localhost', 10007))
