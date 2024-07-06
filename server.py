import socket
import os   


def open_file(file_name):
    directory = '/Users/hillelstanislas/Desktop/coding/python-ptoject/A_system_for_ploading _and_downloading_files/s_storage'
#   if not os.path.exists(directory):
#       os.makedirs(directory)  # יצירת התיקייה אם היא לא קיימת
    file_path = os.path.join(directory, file_name)  # יצירת הנתיב המלא לקובץ
    with open(file_path, 'w') as file:
        file.write("")  # יצירת הקובץ הריק
    print(f"File '{file_name}' created successfully in directory.")
    return file_path
def write_file(file_path, data):
    with open(file_path, 'wb') as file:
        file.write(data)
    print("All data written to the file!")
if __name__ == "__main__":
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(('127.0.0.1', 8080))
    server_sock.listen(1)
    print("Server is listening for connections...")
    client_sock, client_address = server_sock.accept()
    prefer = client_sock.recv(1024).decode()
    if prefer == "1":
        file_name = client_sock.recv(1024).decode()
        file_name=f"/{file_name}"
        directory = '/Users/hillelstanislas/Desktop/coding/python-ptoject/A_system_for_ploading _and_downloading_files/s_storage'
        file_path=directory+file_name
        with open(file_path,'rb') as file:
            data = file.read()
            client_sock.send(data)
    if prefer == "2":
        file_name = client_sock.recv(1024).decode().strip()  # הסרת רווחים וגרשיים
        file_path = open_file(file_name)
        msg = "The file created successfully!"
        client_sock.send(msg.encode())
        data = b''
        while True:
            data2 = client_sock.recv(1024)
            if not data2:
                break
            data +=data2
        write_file(file_path, data)

    client_sock.close()
    server_sock.close()





