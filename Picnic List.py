# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 17:28:20 2022

@author: PC_RC
"""

from tkinter import *
import random

root = Tk()
root.title("List")
root.geometry("400x400")
root.configure(background="yellow")

display_item_list = Label(root)
display_random_item_list = Label(root)
list_food = ["carpet", "bottle", "napkin", "chocolate", "chips", "handkerchief", "park id card", "cutlery", "muffin"]

display_item_list["text"] = "Picnic Items: " + str(list_food)

def randomlist():
    randomlist = random.sample(range(1,9),1)
    display_random_item_list["text"] = "Put item " + str(randomlist)
    
btn = Button(root, text = "What should I pack for picnic?", command=randomlist)
btn.place(relx = 0.5, rely= 0.4, anchor=CENTER)

display_item_list.place(relx = 0.5, rely= 0.5, anchor=CENTER)
display_random_item_list.place(relx = 0.5, rely= 0.6, anchor=CENTER)

root.mainloop()