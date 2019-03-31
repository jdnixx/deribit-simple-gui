import tkinter as tk


# set up RestClient
from deribit_api import RestClient
client = RestClient("AHoDez9QDVyM", "UQT5ZLCGE4WTF6XYSKTJZSJKOCXQES35", "https://test.deribit.com") # key, secret, URL
client.index()
client.account()
#print(client.positions())

HEIGHT = 700
WIDTH = 800



root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="lightblue")
frame.place(relwidth=0.5, relheight=0.8, relx=0.1, rely=0.1)


text = tk.Text(frame)

def displayPositions():
	text.insert(tk.INSERT, client.positions())
	button.place(relx=0, rely=0.1, relwidth=0.25, relheight=0.25)

text.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.4)


button = tk.Button(frame, text="Test button lol", command=displayPositions)
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)

#label = tk.Label(frame, text=client.positions())
#label.place(relx=0, rely=0.5, relwidth=0.9, relheight=0.1)

entry = tk.Entry(frame)
entry.place(relx=0.8, rely=0)










root.mainloop()