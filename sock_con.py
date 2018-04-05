
import socket
import sys

class sock_con:

    def __init__(self, gui=None):
        # gui object for accessing things for the robot
        self.gui = gui
        # get hostname for listening for connection
        #self.host = "10.200.5.223"
        self.host = socket.gethostname() 
        #self.host = "127.0.0.1"
        # get port for listening for new connections
        self.port = 5000
        # create new socket on port and bind
        self.sock = socket.socket()

    ## listen to (3) new connections
    ## @param port - port number for listening connection
    def listen(self, port=5000):
        print('binding to host:', self.host, 'on port', self.port)
        self.sock.bind((self.host, self.port))
        print(self.host)

        self.sock.listen(3)
   
        # if given a new port, change it 
        self.port = port
    
        # get connection and address of sender
        conn, addr = self.sock.accept()
        print('New connection from:', addr)
#        data = conn.recv(1024).decode()
        data = ''

        while data != 'end' and data != 'start':    
            # get message contents
            data = conn.recv(1024).decode()
            if data != '':
                #data = conn.recv(1024).decode()
                #print('received message:', data)
                print(addr, 'says:\n', data, '\n')
                words = data.split()
            
                for word in words:
                    print('word:', word)

                    
                # speech syntax
                # start (run go function)
                # move forward for three seconds (move wheels forward for 3 seconds)
                # move back for three seconds (move wheels forward for 3 seconds)
                # turn head left for three seconds (turn head for three seconds)
                # turn body left for three seconds
                if len(words) > 0:
                    if words[0] == 'start':
                        gui.go()
                        done = True
                    # if for moving robot forward
                    elif words[0] == 'move' and words[1] == 'forward':
                        time = self.get_number(words[3])
                        gui.add('wheels', 'go forward', time)
                    # if for moving robot back
                    elif words[0] == 'move' and (words[1] == 'back' or words[1] == 'backward'):
                        time = self.get_number(words[3])
                        gui.add('wheels', 'go back', time)
                    # if for turning head/body
                    elif words[0] == 'turn':
                        time = self.get_number(word[3])
                        gui.add(words[1], words[2], time)


    ## turn word number to number
    def get_number(number):
        if number == 'one':
            number = 1
        elif number == 'two':
            number = 2 
        elif number == 'three':
            number = 3 
        elif number == 'four':
            number = 4
        elif number == 'five':
            number = 5
        elif number == 'six':
            number = 6

    ## connect to host 
    ## @param addr - ip address of new host
    ## @param c_port - port of new host
    def connect(self, host, c_port=5000):
        self.port = 5001
        print('binding to host:', self.host, 'on port', self.port)
        self.sock.bind((self.host, self.port))
        print(self.host)
        # create new socket and connect to host on that socket
        sock = socket.socket()
        sock.connect((host, c_port))

        # send on message to that host
        message = 'I smell like beef...'
        sock.send(message.encode())

        # safely shutdown and close sockets
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

if __name__ == '__main__':
    con = sock_con()

    if len(sys.argv) > 1 and sys.argv[1] == 'client':
        if len(sys.argv) > 2:
            con.connect(sys.argv[2])
        else:
            print('enter hostname')
    elif len(sys.argv) > 1 and sys.argv[1] == 'server':
        con.listen()       

    print('client or server?')
