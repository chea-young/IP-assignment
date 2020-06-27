'''
Threading TCP server with request handlers
'''
import socket
import threading, logging, selectors

logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s')
# default log level
# logging.basicConfig(level=logging.WARNING, format='%(threadName)s: %(message)s')

class BaseRequestHandler:
    def __init__(self, request, client_address, server):
        self.request = request
        self.cli_addr = client_address
        self.server = server    # can access server attributes
        self.setup()
        try:
            self.handle()
        finally:
            self.finish()

    def setup(self):
        pass

    def handle(self): #얘만 overrriding 해서 쓸 수 있다.
        pass

    def finish(self):
        pass

# 상속받아서 쓸수있다.
class StreamRequestHandler(BaseRequestHandler):
    def setup(self):
        self.rfile = self.request.makefile('rb')# string으로 만들어준다. 
        self.wfile = self.request.makefile('wb', buffering=0) # no buffering,  써달라고 하면 그냥 send해서 flush 가 필요가 없다.

    def finish(self):
        if not self.wfile.closed:
            self.wfile.flush()
        self.wfile.close()
        self.rfile.close()


class ThreadingTCPServer:# 멀티스레딩하는 TCP 서버를 만든다.
    def __init__(self, server_address, HandlerClass):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Reuse port number if used
        sock.bind(server_address)
        sock.listen(5)
        self.sock = sock
        self.HandlerClass = HandlerClass

    def serve_forever(self):# 메인 스레드안에서 핸들링
        logging.info(f'Server started: {self.sock.getsockname()}')
        try:
            while True:                     # do forever (until process killed)
                request, client_address = self.sock.accept()
                logging.info(f'Connection from {client_address}')
                t = threading.Thread(target=self.process_request,
                                        args=(request, client_address)) #이렇게 넘겨준다
                t.setDaemon(True)  # as daemon thread 데몬으로 start
                t.start()
        except:
            self.server_close()
            raise# 다시 동일한 exception을 일으켜서 끝내라

    def process_request(self, request, client_address):# 새로운 스레드로 돌아감 (request는 리퀘스트 소켓) #스레드 내에서 핸들링
        """Invoke the handler to process the request"""
        try:
            handler = self.HandlerClass(request, client_address, self) #자체에서 exptception 핸들링함 (핸들러를 다른 클래스로 독립시킴)
            #self는 서버자체를 access함.
            # 얘가 끝나는 거는 finish()가 된거고 client 가 끝내자고 해서 끝낸 것이다.
        except Exception as e:
            logging.exception(f'Exception in processing request from {client_address}: {e}')
        finally:
            request.close()

    def server_close(self):
        self.sock.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.server_close()


if __name__ == '__main__':
    # Echo server implemented by extending request handler
    class EchoRequestHandler(StreamRequestHandler): #내 에코하기 위한다.
        def handle(self):
            while True:
                line = self.rfile.readline() #읽어와서 하면 된다.
                if not line:
                    break
                logging.debug(f'Rcvd from {self.cli_addr}: {len(line)} bytes')
                self.wfile.write(line)         # send a reply to the client
            logging.info(f'Client {self.cli_addr} closing')


    # server = ThreadingTCPServer(('', 10007), EchoRequestHandler)
    # server.serve_forever()
    # __enter__ __exit으로 이렇게 쓰는거
    with ThreadingTCPServer(('', 10007), EchoRequestHandler) as server:
        server.serve_forever()#이렇게 하면 서버만 만들어진다. (비정상적으로 종료될 때만 빠져나간다.)
       

