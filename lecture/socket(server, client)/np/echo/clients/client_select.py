import socket
import msg
import selectors


def client(server_addr):
    """Client - read more date after shut-down
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_addr)       # connect to server process
    sock.setblocking(False)         # non-blocking socket 

    sel = selectors.DefaultSelector()
    sel.register(sock, selectors.EVENT_READ | selectors.EVENT_WRITE)
    it = msg.msgs(100, length=2000)  # generator is iterable(for문을 계속 돌릴 수가 없어서 generator 만든거)
    sent_bytes = []
    recv_bytes = []
    keep_running = True

    while keep_running:
        events = sel.select(timeout=1)   # wake up every 1 sec even though no events

        if not events:  # timeout event occurs
            print('timeout')
            continue

        for key, mask in events:
            conn = key.fileobj

            # recv if socket becomes readable
            if mask & selectors.EVENT_READ:
                data = conn.recv(2048)#이런 버퍼 사이즈는 2의 n승으로 하는 것이 좋다 커널이 2의 n승으로 메모리를 할당하는 것이 빠르기 때문이다.
                if not data:
                    print('Server closing')
                    sel.unregister(conn)
                    keep_running = False
                    break
                recv_bytes.append(len(data))
                print('recv:', len(data))

            # sendall if socket becomes writable
            if mask & selectors.EVENT_WRITE:
                try:
                    message = next(it)
                except StopIteration:  # no more messages
                    # Do not check writable.
                    sel.modify(conn, selectors.EVENT_READ)
                    conn.shutdown(socket.SHUT_WR)
                    break
                conn.sendall(message)   # send the entire message even though non-blocking mode(sendall은 실제로 있는게 아니라 파이썬으로 만들어놓은것)
                sent_bytes.append(len(message))
                print('send:', len(message))

        # end for
    # end while

    sock.close()
    msg.report(sent_bytes, recv_bytes)

if __name__ == '__main__':
    client(('np.hufs.ac.kr', 7))
