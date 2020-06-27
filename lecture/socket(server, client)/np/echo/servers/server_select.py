from socket import socket, AF_INET, SOCK_STREAM
import selectors
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')
#DEBUG  INFO 다 프린팅하는 것
#INFO 하면 info 레벨 이상만 프린팅된다. error와
# default로 적힌것이 되는것
sel = selectors.DefaultSelector()

# call-back functions
def accept(sock, mask):
    conn, client_address = sock.accept()
    conn.setblocking(False) # non-blocking socket
    sel.register(conn, selectors.EVENT_READ, echo) #커넥티드 소켓 등록 )(callback function은 echo로)
    logging.info(f'Client enters: {client_address}') #몇 바이트마다 debug하는 것

def echo(conn, mask):
    data = conn.recv(1024)  # Should be ready, conection이 없는데 receive를 받으려고 해서 error가 생긴것이다
    #소켓이 없는데 읽으려고 해서 죽었다.(client하나떄문에 죽었다.)(exception handling을 잘 돌려야 겠다.)
    if data:
        conn.sendall(data)  # Hope it won't block 데이터를 다 보낼 때까지 loop를 돈다.
        logging.debug(f'echo({conn.fileno()}) {len(data)} bytes')
        #send는 일부만 넣어서 들어갈 수 있는데 
    else:
        client_address = conn.getpeername()
        sel.unregister(conn)
        conn.close()#select에서 관심대상이 아니다.
        print('Client closed {}'.format(client_address))
        """logging.info(f'Client closing: {conn.getpeername()}')
        shut_down(conn) """

def shut_down(conn):
    try:
        sel.unregister(conn)
        conn.close()
    except Exception as e:
        logging.error(e)#(warnign보다 더 높은 레벨 error)
        #logging은 log메세지를 프린하게 한다. 다른 모듈에서 실행가능 

def echo_server(my_port):

    sock = socket(AF_INET, SOCK_STREAM) #data가 도착할 떄까지 기다릴 것이다.
    sock.setblocking(False) # nonblocking
    sock.bind(('', my_port))
    sock.listen(5)
    sel.register(sock, selectors.EVENT_READ, accept)# 위에서 accept라는 함수가 정의 되어있다.
    print('Server started')
    logging.info(f'Server listens: {sock.getsockname()}')

    while True:
        events = sel.select(timeout=1) #기다리는 것을 n+1 소켓에서 기다린다.
        print(events)
        for key, mask in events:
            callback = key.data #callback 함수불러서 (coneected 면 echo )
            try:
                callback(key.fileobj, mask) #fileobj 가 소켓(arugument로 이걸 보냄)
            except OSError as e:
                logging.error(f'Error in{callback.__name__} callback: {e}')
                shut_down(key.fileobj)
                if(key.fileobj is sock):
                    import sys
                    sys.exit(1) # 0는 비정상 전송이라는 것을 알려준다. 
                    #listening 소켓에서 문제가 생기면 불가능

if __name__ == '__main__':
    echo_server(10007)
#client 돌릴 때 (python clients.py localhost 10007 500 5)
#500개의 메세지를 5개의 client가 돈다.
#keyboardexception이 일어나면서 열린 socket들을 close(ctrl+c)
#(ctrl+break)강제저긍로 중지시켜버리면 server에서 exception이 발생 data가 발생한 것이아니라.