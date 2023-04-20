import socket
import rsa_helper

def main():
    private_key, public_key = rsa_helper.generate_key_pair()
    message = input("Enter a message to sign: ")
    signature = rsa_helper.sign_message(message, private_key)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 12345))
        print("Public key:", public_key)
        s.sendall(str(len(public_key)).encode().zfill(4))
        s.sendall(public_key)
        s.sendall(str(len(message)).encode().zfill(4))
        s.sendall(message.encode())
        s.sendall(str(len(signature)).encode().zfill(4))
        s.sendall(signature)

if __name__ == "__main__":
    main()
