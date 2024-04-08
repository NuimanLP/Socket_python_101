import socket

def run_client():
    n= 0
    col = 0
    for i in range(10):
        # create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_ip = "203.150.243.76"  # replace with the server's IP address
        server_port = 6969  # replace with the server's port number
        # establish connection with server
        client.connect((server_ip, server_port))

        print(f"CONNECTED TO: {server_ip}:{str(server_port)}")
        Realname = '6610110066 Chavatik Thorarit'
        # name = input("Enter your name: ",Realname)
        print(F"Enter your name: {Realname}")
        client.send(Realname.encode("utf-8")[:1024])
        confirm = client.recv(1024).decode("utf-8")
        print(f"DATA: {confirm}")

        # Set initial guess range
        low = 1
        high = 100

        while True:
            # Calculate midpoint for the next guess
            guess = (low + high) // 2
            print(f"Guessing {guess}")
            client.send(str(guess).encode("utf-8")[:1024])

            # receive response from the server
            response = client.recv(1024).decode("utf-8")
            print(f"DATA: {response}")

            if response == "CORRECT":
                col+=1
                print(f"ANSWER = {guess}")
                break
            elif response == "LESS":
                n +=1
                high = guess - 1  # Adjust high end of the range
            elif response == "MORE":
                n+-1
                low = guess + 1  # Adjust low end of the range
            else:
                print("Unexpected response from server")
                break

        # close client socket (connection to the server)
        client.close()
        print("Connection closed")
        print(f"Try To Correct: {100/((col/n)*100)}")

run_client()
