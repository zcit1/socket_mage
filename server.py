import socket
from PIL import Image
import os
import threading
count=0
port = 8000
host = '127.0.0.1'
ext = ".jpg"
filename1 = ""

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
            print("printing count ", count)
            filename1 = str(count)+'r.jpg'
            print(filename1)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            print("thread id = ",conn)
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() -1}")

def handle_client(conn, addr):
        lcount=1
        print(f"[NEW CONNECTION] {addr} connected.")
        #while True:
            #conn, addr = s.accept()
        print('Connected to addr{}'.format(addr))
        
   
        while True:
            filename = str(addr[0]) +"_"+str(lcount)+"r.jpg"
            #filename = str(lcount) +"r.jpg"
            with open(filename, 'wb') as f:
                print("opening ", filename)
                data = conn.recv(50000)
                f.write(data)
                #print(data)
                f.close()
            with open(filename, 'rb') as f:
                
                im = Image.open(filename)
                im.show()
                lcount += 1

print('Done')


if __name__ == "__main__":
    main()
