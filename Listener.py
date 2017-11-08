import socket
import sys

#This function creates a socket, binds it to a port, and then receives data
def openSocket(): #Creates the socket and begins listening
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address =  ('localhost', 10000)

    # Simple try-catch block to make sure a port opens correctly
    try:
        sock.bind(server_address)
    except socket.error as msg:
        print('Bind failed, error code : ' + str(msg[0]) + ' Message: ' + str(msg[1]))
        sys.exit(1)

    # Listens for incoming connections, the number in parenthesis is how many connections can be in the backlog queue
    sock.listen(5)

    # Simple endless loop that holds
    print('Waiting for a connection')
    while True:
        connection, client_address = sock.accept()
        try:
            print('Connection from {0}'.format(client_address))
            while True:
                data = connection.recv(48).decode()
                print('Received: {0}'.format(data), file=sys.stderr)
                if data == "":
                    break

        # This closes and cleans up the connection, this is important
        finally:
            connection.close()
            print('Connection closed', file=sys.stderr)

openSocket()





