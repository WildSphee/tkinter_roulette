import tkinter as tk
import random

money = 10000

def spin():

    global money

    print(f"{e1.get()=} {e2.get()=}")
    if e1.get() == "" or e1.get() == "0":
        labelwin["text"] = "some numbers are missing"
        return


    betamount = float(e1.get())
    betnumber = float(e2.get())

    if money == 0:
        labelwin["text"] = "You broke, GG :("
        return

    if money < betamount:
        labelwin["text"] = "Not enough money, please lower bet amount :("
        return
    else:
        money -= betamount

    spinnum = random.randint(0, 36)

    if spinnum == betnumber:
        labelwin["text"] = f"Roulette landed on {spinnum}, you win an amount of ${betamount * 36}!"
        money += betamount*36
        labelmoney["text"] = money.__str__()
    else:
        labelwin["text"] = f"Roulette landed on {spinnum}, you lost :("
        labelmoney["text"] = money.__str__()

root = tk.Tk()
root.title("Bet The Roulette")
root.geometry('{}x{}'.format(300, 200))


label0 = tk.Label(root, text="Welcome to the Roulette Simulator", borderwidth=5)
label0.grid(row=0, columnspan=2)

labelmoney = tk.Label(root, text=money.__str__())
labelmoney.grid(row=1)

label1 = tk.Label(root, text="Bet amount:", borderwidth=5)
label1.grid(row=2, columnspan=1, column=0)
label2 = tk.Label(root, text="Bet number:", borderwidth=10)
label2.grid(row=3, column=0)
e1 = tk.Entry(root, borderwidth=5)
e1.grid(row=2, column=1)
e2 = tk.Scale(root, borderwidth=5, from_=0, to=36, orient=tk.HORIZONTAL)
e2.grid(row=3, column=1)

labelwin = tk.Label(root, text=f"", borderwidth=10)
labelwin.grid(row=4, column=0, columnspan=2)


spinb = tk.Button(root, text="Spin!!", command=spin)
spinb.grid(row=5, columnspan=2)


root.mainloop()