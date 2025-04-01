import socket
import os
import time

SERVER_IP = "192.168.1.100"  # Replace with server IP
PORT = 12345

def send_data():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, PORT))
    with open("attendance.txt", "r") as f:
        data = f.read()
    client.send(data.encode())
    client.close()

if __name__ == "__main__":
    while True:
        if os.path.exists("attendance.txt"):
            send_data()
            os.remove("attendance.txt")
        time.sleep(60)
