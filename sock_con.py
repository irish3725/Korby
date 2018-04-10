import time
import socket
import sys

class sock_con:

    def __init__(self, gui=None):
        # gui object for accessing things for the robot
        self.gui = gui
        # get hostname for listening for connection
        self.host = "10.200.5.223"
        #self.host = socket.gethostname() 
        #self.host = "127.0.0.1"
        # get port for listening for new connections
        self.port = 5000
        # create new socket on port and bind
        self.sock = socket.socket()

        self.send = True
        self.message = 'reply from server'

    ## tell client to listen
    def tell_listen(self):
        self.sock.sendall('listen\n'.encode())

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
#        data = conn.recv(1024).decode()
        data = ''

        while data != 'end':    
            conn, addr = self.sock.accept()
            print('New connection from:', addr)
            # get message contents
            data = conn.recv(1024).decode()

            if self.send:
                conn.send(self.message.encode())
                self.send = False

            if data != '':
                #data = conn.recv(1024).decode()
                #print('received message:', data)
                print(addr, 'says:\n', data, '\n')
                words = data.split()
            
                part = ''
                direction = ''
                time = ''
                # speech syntax
                # start (run go function)
                # move forward for three seconds (move wheels forward for 3 seconds)
                # move back for three seconds (move wheels forward for 3 seconds)
                # turn head left for three seconds (turn head for three seconds)
                # turn body left for three seconds
                while len(words) > 0:

                    word = words.pop(0)
                    print('word:', word)

                    time = self.get_number(word)

                    if self.gui:
                        if word == 'start':
                            self.gui.go()
                        elif word == 'forward':
                            direction = 'go forward'

                        # if for moving robot back
                        elif word == 'back' or word == 'backward':
                            direction = 'go back'

                        # if for turning head/body
                        elif word == 'left' or word == 'right' or word == 'up' or word == 'down':
                            direction = word

                        elif word == 'head' or word == 'body' or word == 'wheels':
                            part = word

                        elif word == 'move' or word == 'go' or word == 'turn':
                            part = 'wheels'
                        else:
                            print('didn\'t recognize word', word)

                        if part != '' and direction != '' and time != '':
                            self.gui.add(part, direction, time)
                            part = ''
                            direction = ''
                            time = ''

        print("closing connection")
        # safely shutdown and close sockets
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()

    ## turn word number to number
    def get_number(self, number):
        if number == 'one':
            number = 1
        elif number == 'two' or number == '2':
            number = 2 
        elif number == 'three' or number == '3':
            number = 3 
        elif number == 'four' or number == '4':
            number = 4
        elif number == 'five' or number == '5':
            number = 5
        elif number == 'six' or number == '6':
            number = 6
        else:
            return ''

        return number

    ## connect to host 
    ## @param addr - ip address of new host
    ## @param c_port - port of new host
    def connect(self, host, c_port=5000):
        self.port = 5002
        print('binding to host:', self.host, 'on port', self.port)
        self.sock.bind((socket.gethostname(), self.port))
        print(self.host)
        # create new socket and connect to host on that socket
        sock = socket.socket()
        sock.connect((host, c_port))

        # send on message to that host
#        message = 'I smell like beef...'
        message = ' move head down for two second'
        sock.send(message.encode())
        message = ' move head up for one second'
        sock.send(message.encode())
        message = ' move body left for one second'
        time.sleep(5)
        sock.send(message.encode())
        message = ' move body right for one second'
        sock.send(message.encode())
        message = ' start'
        sock.send(message.encode())

        # safely shutdown and close sockets
        #sock.shutdown(socket.SHUT_RDWR)
        #sock.close()

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
