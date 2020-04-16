import mail_backend as mb
from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog

maillist = []

def addmail(event):
    mail = recievers_field.get()
    maillist.append(mail)
    recievers_field.delete(0,END)
    Label(insidecanv, text = mail, width = 95, anchor = "w").pack()

def loadfromfile():
    x = filedialog.askopenfilename(title = "Select your list file", filetypes = (("Txt FIle","*.txt"), ("All Files","*.*")))
    if x != ():
        try:
            with open(x,"r") as fi:
                y = fi.readlines()
                for mail in y:
                    maillist.append(mail)
                    Label(insidecanv, text = mail, width = 95, anchor = "w").pack()
        except:
            pass
def reset():
    global maillist
    maillist = []
    for child in insidecanv.winfo_children():
        child.destroy()

def showpas():
    if var.get():
        password_field.configure(show = "")
    else:
        password_field.configure(show = "*")
def sendmails():
    try:
        server = mb.Mail()
        server.sender(username_field.get(), password_field.get())
        server.reciever(maillist)
        server.login()
        msg = msghere.get("1.0", END)
        server.send(msg)
        status.configure(text = "Completed")
    except:
        status.configure(text = "Failed")

window = Tk()
window.title("Mail Sender")
window.geometry("900x600")
window.iconphoto(True,PhotoImage(file="icon.png"))
root = Frame(window, padx = 10)
root.pack()

header = Frame(root,width = 800, height = 40)
send = Frame(root,width = 800, height = 40)
reci = Frame(root,width = 800, height = 40)
dispmails = LabelFrame(root,text = "Added mails", width = 800)
messagesection = LabelFrame(root,text = "Type your message", pady = 5)
footer = Frame(root,width = 800, height = 40)

#Sender's Credentials
username = Label(send,text = "Sender's Gmail: ", anchor = "w", width = 20)
username.grid(row = 0, column = 0, sticky = EW)

username_field = Entry(send, width = 30)
username_field.grid(row = 0, column = 1)

password = Label(send,text = "Password: ", width = 20)
password.grid(row = 0, column = 2)

password_field = Entry(send, show = "*")
password_field.grid(row = 0, column = 3)

var = IntVar()
show = Checkbutton(send, variable = var, text = "Show Password", command = showpas)
show.grid(row = 0, column = 4)

#Recievers Address
recievers = Label(reci, text = "Reciever's Gmail:", anchor = "w", width = 20)
recievers.grid(row = 0, column = 0, sticky = EW)

recievers_field = Entry(reci, width = 30)
recievers_field.bind('<Return>', addmail)
recievers_field.grid(row = 0, column = 1, sticky = EW)

loadfile = Button(reci, text = "Open file", command = loadfromfile)
loadfile.grid(row = 0, column = 2, padx = 40)

res = Button(reci, text = "Reset", command = reset)
res.grid(row = 0, column = 3, padx = 40)

#Recievers List
canv = Canvas(dispmails, width = 700, height = 220)
scrollbar = ttk.Scrollbar(dispmails, orient = "vertical", command = canv.yview)
insidecanv = Frame(canv)
#IDK what the hell this part does found it on web for scroll window ._.
insidecanv.bind("<Configure>",lambda e: canv.configure(scrollregion=canv.bbox("all")))

canv.create_window((0,0), window = insidecanv, anchor = "nw")
canv.configure(yscrollcommand = scrollbar.set)

canv.pack(side = "left", fill = "both", expand = True)
scrollbar.pack(side = "right", fill = "y")

#Message Section
msghere  = ScrolledText(messagesection, width = 95, height = 9)
msghere.pack()

#Footer
status = Label(footer)
status.grid(row = 0, column = 1, padx = 20)
sendbtn = Button(footer, text = "Send Mails", command = sendmails)
sendbtn.grid(row = 0, column = 0)

header.grid(row = 0, column = 0)
send.grid(row = 1, column = 0, pady = 5, sticky = NSEW)
reci.grid(row = 2, column = 0, pady = 5, sticky = NSEW)
dispmails.grid(row = 3, column = 0, pady = 5, sticky = NSEW)
messagesection.grid(row = 4, column = 0, pady = 5, sticky = NSEW)
footer.grid(row = 5, column = 0, pady = 2)

root.mainloop()