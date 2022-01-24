import socket
import re
import PyQt5

def start_server(list_view):
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
            try:
                matches = re.findall(
                    r'[0-9][0-9][0-9][0-9]\s[a-zA-Z0-9][a-zA-Z0-9]\s[0-9][0-9]:[0-9][0-9]:[0-9][0-9]\.[0-9][0-9][0-9]\s[0-9][0-9]',
                    data.__str__())
                print(matches)
                for match in matches:
                    member_number = match[0:4]
                    chanel_id = data.decode('ascii')[5:7]
                    hours = data.decode('ascii')[8:10]
                    minutes = data.decode('ascii')[11:13]
                    seconds = data.decode('ascii')[14:16]
                    zhq = data.decode('ascii')[17:20]
                    group_number = data.decode('ascii')[21:23]
                    print(f'member_number {member_number}')
                    print(f'chanel_id {chanel_id}')
                    print(f'hours {hours}')
                    print(f'minutes {minutes}')
                    print(f'seconds {seconds}')
                    print(f'zhq {zhq}')
                    print(f'group_number {group_number}')
                    time = data.decode('ascii')[8:18]
                    print(f'спортсмен, нагрудный номер {member_number} прошёл отсечку {chanel_id} в «{time}»')
                    if group_number == "00":
                        item = PyQt5.QtGui.QStandardItem(f'спортсмен, нагрудный номер {member_number} прошёл отсечку {chanel_id} в «{time}»')
                        list_view.appendRow(item)
                    # list_view.addItem(f'спортсмен, нагрудный номер {member_number} прошёл отсечку {chanel_id} в «{time}»')

                print(data.__str__())
            except UnicodeDecodeError:
                pass
            conn.send("Done".encode())



