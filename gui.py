def Evil_insult():
    import requests
    data=requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')
    data=data.json()
    return data['insult']

from tkinter import *
app=Tk()
app.title("EVIL INSULT GENERATOR ")
app.geometry("800x100")
app.resizable(False,False)


def generate_insult():
    insult=Evil_insult()
    entry_box.delete(0,END)
    entry_box.insert(0,insult)
    return None

entry_box=Entry(app,width=50,borderwidth=5,font=("Helvetica",20),fg="black",bg="white",justify="center")
entry_box.pack()

Button(app,text="Generate Insult",command=generate_insult,width=15,borderwidth=3,font=("EkMukta Medium",10)).pack()

app.mainloop()

