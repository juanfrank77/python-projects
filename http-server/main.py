import os
import socket
import threading
import argparse

def handle_request(connection, address, directory):
    request = connection.recv(1024).decode()
    headers = request.split("\r\n")
    method, path, version = headers[0].split(" ")

    agent_header = headers[2].split(" ")[-1]
    random_string = path.partition("/echo/")[-1]

    if path == "/":
        response = "HTTP/1.1 200 OK\r\n\r\n"
    elif "/echo/" in path:
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(random_string)}\r\n\r\n{random_string}"
    elif path == "/user-agent":
        response = f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {len(agent_header)}\r\n\r\n{agent_header}"
    elif "/files/" in path:
        filename = path.split("/")[-1]
        response = handleFiles(filename, directory)
        if method == "POST":
            file_content = request.split("\r\n")[-1]
            response = save_file(filename, directory, file_content)
    else:
        response = "HTTP/1.1 404 Not Found\r\n\r\n"

    connection.sendall(response.encode())   
    connection.close()

def handleFiles(filename, directory):
    file_path = os.path.join(directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        return f"HTTP/1.1 200 OK\r\nContent-Type: application/octet-stream\r\nContent-Length: {len(content)}\r\n\r\n{content}"
    else:
        return "HTTP/1.1 404 Not Found\r\n\r\n"
    
def save_file(filename, directory, content):
    file_path = os.path.join(directory, filename)
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"HTTP/1.1 201 Created\r\n\Content-Type: application/x-www-form-urlencoded\r\n\r\n"
    except:
        return f"HTTP/1.1 500 Internal Server Error\r\n\r\n"

def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    server_socket = socket.create_server(("localhost", 4221), reuse_port=True)

    server_socket.listen()
    print("Listening on localhost:4221")

    while True:
        # Wait for client connection
        connection, address = server_socket.accept()

        # Parses command line arguments
        parser = argparse.ArgumentParser()
        parser.add_argument("--directory", help="The directory to check for files")
        args = parser.parse_args()

        # Creates a thread to handle concurrent requests
        client_thread = threading.Thread(target=handle_request, args=(connection, address, args.directory))
        client_thread.start()

if __name__ == "__main__":
    main()
