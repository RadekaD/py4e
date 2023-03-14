import socket


user_input = input("Enter URL: ")
count = 0

try:
    host = user_input.split("/")[2]
except:
    print("Please enter a valid URL")

print(host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = f"GET {user_input} HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512).decode()
    if len(data) < 1:
        break
    
    for line in data:
        words = line.split()
        count = count + 1            
        if count > 3000:
            break

print(count)   
mysock.close()