#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import*
root= Tk()
root.title= "p151"
root.geometry= "500x500"

month=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits=(20000, 45000,78000,97000,12000,456000, 65000, 54000,10000,30000,70000,90000)

max_profit= max(profits)
max_profit_index= profits.index(max_profit)
print(max_profit_index)
max_profit_month= month[max_profit_index]
print("The maximum profit of "+ str(max_profit)+ " was recorded in the month of "+str(max_profit_month))

def maximum():
    label_max["text"]= "The most profitable month was " + str(max_profit_month) +" with a profit of "+ str(max_profit)

label_max= Label(root)
btn_max=Button(root, text="Most profitable month", command= maximum)

def minimum():
   label_min["text"]= "The least profitable month was " + str(min_profit_month) +" with a profit of "+ str(min_profit) 

min_profit= min(profits)
min_profit_index= profits.index(min_profit)
print(min_profit_index)
min_profit_month= month[min_profit_index]
print("The minimum profit of "+ str(min_profit)+ " was recorded in the month of "+str(min_profit_month))
label_min= Label(root)
btn_min= Button(root, text="Least profitable month", command= minimum)


label_max.place(relx= 0.5, rely= 0.3, anchor= CENTER)
btn_max.place(relx= 0.5, rely= 0.4, anchor= CENTER)
label_min.place(relx= 0.5, rely= 0.6, anchor = CENTER)
btn_min.place(relx= 0.5, rely= 0.7, anchor = CENTER)
root.mainloop()