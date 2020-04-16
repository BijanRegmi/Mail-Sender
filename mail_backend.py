from smtplib import SMTP
class Mail:
    def __init__(self):
        self.server = "smtp.gmail.com"
        self.port = 587
        self.process = SMTP(self.server,self.port)
        self.process.starttls()

    def sender(self,my_address,password):
        self.my = my_address
        self.password = password
        
    def reciever(self,their_address: list):
        if type(their_address) == str:
            their_address = their_address.splitlines()
        self.their = their_address

    def login(self):
        self.process.login(self.my,self.password)

    def send(self,message):
        for x in self.their:
            self.process.sendmail(from_addr=self.my,to_addrs=x,msg=message)

    def __str__(self):
        return "\nSender: " + self.my + "\nReciever: " + str(self.their)