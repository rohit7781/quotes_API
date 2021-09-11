from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Rohit Quotes")
window.config(padx=50, pady=50)

canvas = Canvas(width=400, height=350 )
background_img = PhotoImage(file="ab.png")
canvas.create_image(200, 190, image=background_img )
quote_text = canvas.create_text(200, 190, text="Click on below button to start quotes ", width=250, font=("Arial", 10, "bold"), fill="black")
canvas.grid(row=0, column=0)

myimg = PhotoImage(file="bb.png")
btn1 = Button(image=myimg, highlightthickness=10, command=get_quote)
btn1.grid(row=1, column=0)

window.mainloop()