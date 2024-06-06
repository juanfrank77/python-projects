# Uncomment this to pass the first stage
import socket
import threading

def handle_client(connection):
    while True:
        data = connection.recv(1024)
        if 'ping' in data.decode('utf-8').lower():
            response = "+PONG\r\n"
            connection.send(response.encode('utf-8'))
        elif 'echo' in data.decode('utf-8').lower():
            # extract the message from the command
            msg = data.decode('utf-8')[6:].split('\\r\\n')[-2]
            response = f"${len(msg)}\r\n{msg}\r\n"
            connection.send(response.encode('utf-8'))
        else:
            print("Unknown command: ")

# echo '*2\r\n$4\r\nECHO\r\n$9\r\nblueberry\r\n' | nc localhost 6379

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)

    while True:
        connection, address = server_socket.accept()
        print(f"Accepted connection from {address}")
        client_thread = threading.Thread(target=handle_client, args=(connection,))
        client_thread.start()

if __name__ == "__main__":
    main()
