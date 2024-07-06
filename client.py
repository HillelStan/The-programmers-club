import socket
import os

def open_file(file_name):
    directory = '/Users/hillelstanislas/Desktop/coding/python-ptoject/A_system_for_ploading _and_downloading_files/c_storage'
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
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('127.0.0.1', 8080))
    prefer = input("Tap 1 for downloading, Tap 2 for uploading: ")
    while True:
        if prefer == "1" or prefer == "2":
            break
        prefer = input("Invalid input. Tap 1 for downloading, Tap 2 for uploading: ")
    client_sock.send(prefer.encode())
    if prefer == "1":
        file_name = input("enter name of file with ect: ")
        client_sock.send(file_name.encode())
        file_path = open_file(file_name)
        data = b''
        while True:
            data2 = client_sock.recv(1024)
            if not data2:
                break
            data +=data2
        write_file(file_path, data)
    if prefer == "2":
        file_path = input("enter the path of the file: ").strip().strip("'")  # הסרת גרשיים מיותרות
        file_name = os.path.basename(file_path)
        client_sock.send(file_name.encode())
        print(client_sock.recv(1024).decode())
        with open(file_path, 'rb') as file:
            data = file.read()
            client_sock.send(data)
client_sock.close()