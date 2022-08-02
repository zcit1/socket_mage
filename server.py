import socket
from PIL import Image
import os
import threading
count=0
port = 8000
host = '127.0.0.1'
ext = ".jpg"
max_size = 50000

def main():
        global count
        print("[STARTING] Server is starting")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((host, port))
        s.listen()

        while True:
            print("Waiting to connect...\n")
            conn, addr = s.accept()
            count += 1

            thread = threading.Thread(target=handle_client, args=(conn, addr))
            print("thread id = ",conn)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

def handle_client(conn, addr):
        lcount=1
        print(f"[NEW CONNECTION] {addr} connected.")
        print('Connected to addr{}'.format(addr))
        
   
        while True:
            filename = str(addr[0]) +"_"+str(lcount)+"r.jpg"
        
            with open(filename, 'wb') as f:
                print("Displaying {} recieved from {}".format( filename, addr[0]))
                data = conn.recv(max_size)
                f.write(data)
                f.close()
                
            with open(filename, 'rb') as f:
                im = Image.open(filename)
                im.show()
                lcount += 1
                
            if os.path.exists(filename):
                os.remove(filename)
                print('Deleting {}...\n' .format(filename))

        print('Done')


if __name__ == "__main__":
    main()
