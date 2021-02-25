import socket
import queue

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(1)
q = []

while True:
    print("listening")
    conn, addr = sock.accept()
    print('connected:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        queue.push(q, data)
        print(q)
        conn.send("Done".encode())

