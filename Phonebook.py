import tkinter as tk
import pymongo

client = pymongo.MongoClient(mongodb://localhost:27017/"'
mydb n client[ phonebook"]
mycol = mydb["contacts"]
root =tk.TkO)
root.geometry("600x406+1200+500")
canvasl = tk.Canvas(root,width=400, height=300)
canvas1.pack()

labell = tk.Label(root_text='FirstName')
canvas1.create_window(100.60, window=_labell)
entry1 = tk.Entry(root)
canvas1.create_window(220.600_window=entry1)
labell = tk.Label(root, text=_'LastName")

label1 = tk. Label(root, text=_'LastName')
canvas1.create_window(100, 90, window=label1)
entry2 = tk.Entry(root)
canvas1.create_window(220, 90, window=entry2)
labell = tk.Label(root, text= 'PhoneNumber')
canvas1.create_window(100, 120, window=label1)
entry3 = tk.Entry(root)
canvas1.create_window(220, 120, window=entry3)
Line=canvas1.create_line(10.40300,40,fill='black'£width=3.
Labell = tk.Label(root, text='Search')
;anvas1.create_window(90, 20, window=label1)
entry4 = tk.Entry(root)
canvas1.create_window(220, 20, window=entry4)

def insert():
 xl= entry1.get()
x2=entry2.get()
x3=entry3.get()
newcontact = ({"firstName": x1,"lastName": x2."phoneNumber":x3})
X = mycol.insert_one(newcontact)



def search():
x4 = entry4.get()
result = mycol.find(("$text": ("$search":x4_)
for x in result:
print(x)



def clearBoxQ):
entry4.delete(0,"end")
entry3.delete(0_"end")
entry2.delete(0,"end")
entry1.delete(0."end")

entry2.delete(0z"end")
entryl.delete(0."end")

button1 =_tk.Button(text='ADD".command: insert)
canvas1.create_window(100,160 _indow=button1)
button2 = tk.Button(text='Search' command=search)
canvasl.create_window(150, 160, window-button2)
button3 = tk.Button(text='Clear'
command=clearBox)
canvas1.create_window(200, 160, window=button3)
root.mainloop()