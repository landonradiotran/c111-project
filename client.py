import socket
from threading import Thread
from tkinter import *

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI(Tk):
    def __init__(self):

        super().__init__()
        self.title("Login")

        self.resizable(width=False, height=False)
        self.configure(width=400, height=300,
							bg="#CD5C08")
        
        self.pls = Label(
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold",
					bg="#CD5C08",
					fg="#ffffff")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        self.label_name = Label(
							text = "Name: ",
							font = "Helvetica 12",
							bg="#CD5C08",
							fg="#ffffff")
        self.label_name.place(   relheight = 0.2,
							    relx = 0.1,
							    rely = 0.2)
        
        # Create a textbox named entry_name and set font, bg (#F5E8B7) and fg (#444444)
        
        # Place entry_name 
        
        # Set focus of cursor by default on the entry_name
        

        self.go = Button(text = "CONTINUE",
						font = "Helvetica 14 bold",
						bg="#FFA259",
						fg="#333333",
                        # Call  login() method and pass the name from self.entry_name
                        command = lambda: self.login(self.name_entry.get()) 
                        )
        self.go.place(  relx = 0.4,
					    rely = 0.55)

    def go_ahead(self, name):
        self.name = name
        rcv = Thread(target=self.receive)
        rcv.start()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                print(message)
            except:
                print("An error occured!")
                client.close()
                break

    # define login() method
    def login(self, name):
        # self.login.destroy()
        self.name = name
        # Move code pf receive_thread here that runs receive() method
        receive_thread = Thread(target=self.receive)
        receive_thread.start()


app = GUI()
app.mainloop()


# Move this code in login() method and add self with receiver
# receive_thread = Thread(target=receive)
# receive_thread.start()

def write():
    while True:
        message = '{}: {}'.format("nickname", input(''))
        client.send(message.encode('utf-8'))

write_thread = Thread(target=write)
write_thread.start()
