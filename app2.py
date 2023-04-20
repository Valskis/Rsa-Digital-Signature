import socket
import threading
import rsa_helper

def handle_connection(conn, addr):
    print(f"Connected by: {addr}")
    
    public_key_size = int(conn.recv(4).decode())
    public_key = conn.recv(public_key_size).strip()
    print("Received public key:", public_key)
    
    message_size = int(conn.recv(4).decode())
    message = conn.recv(message_size).decode()
    
    signature_size = int(conn.recv(4).decode())
    signature = conn.recv(signature_size)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12346))
        s.sendall(str(len(public_key)).encode().zfill(4))
        s.sendall(public_key)
        s.sendall(str(len(message)).encode().zfill(4))
        s.sendall(message.encode())
        s.sendall(str(len(signature)).encode().zfill(4))
        s.sendall(signature)

    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 12345))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            t = threading.Thread(target=handle_connection, args=(conn, addr))
            t.start()

if __name__ == "__main__":
    main()
