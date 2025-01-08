import socket


def echo_client(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print(f"Підключено до сервера {host}:{port}")

        while True:
            message = input("Введіть повідомлення (або 'exit' для завершення): ")
            if message.lower() == 'exit':
                print("Завершення роботи клієнта.")
                break

            client_socket.sendall(message.encode('utf-8'))  # Надсилання повідомлення
            data = client_socket.recv(1024)  # Отримання відповіді від сервера
            print(f"Відповідь сервера: {data.decode('utf-8')}")


if __name__ == "__main__":
    echo_client()
