import time
import socket
from PIL import Image
client_ip = '127.0.0.1'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((client_ip, port))
filename=""
count=0

while True:
         count += 1
         filename = str(count)+".jpg"
         with open(filename, 'rb') as f:
            print('file opened', filename)
            print ("Start : %s" % time.ctime())
            time.sleep( 0.25 )
            print ("End : %s" % time.ctime())
        
            data = s.send(f.read())
            f.close()
            print('transfer complete!!!')
print('transfer complete!!!')
s.close()
