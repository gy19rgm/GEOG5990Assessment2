# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 14:01:14 2020

@author: Perfe
"""
from tkinter import *

#def printSomething():
#
#    for x in range(9): # 0 is unnecessary
#        label = Label(root, text= ("test", str(x)))
#    # this creates x as a new label to the GUI
#        label.pack() 
#
#root = Tk()
#
#button = Button(root, text="Print Me", command=printSomething) 
#button.pack()
#
#root.mainloop()


#'''
#PACK METHOD
#'''
#def printoutput():
#    list = 4
#    list_tot_height = [1,2,5,6]
#    list_mass = [44,67,25,41]
#    
#    a = 0
#    while a < list:
##        label = Label(root, text = ("Iceberg", a+1, "is", list_tot_height[a], " m3, and, weighs", list_mass[a], "kg"))
#        label = Label(root, text = ("Iceberg {} is {} m3 and weighs {} kg".format(a+1, list_tot_height[a], list_mass[a])))
#        label.pack()
#        
#        #print('Iceberg', a+1, 'is', list_tot_height[a], 'm3 and weighs', list_mass[a], 'kg') # tot height + m3 are the same because counted up total 1m3 squares
#       
#        if list_mass[a] < 50:
#            label1 = Label(root, text = ("Iceberg", a+1, "is towable"))
#            label1.pack()
#            #print('Iceberg', a+1, 'is towable')
#            
#        else:
#            label2 = Label(root, text = ("Iceberg", a+1, "is NOT towable"))
#            label2.pack()
#            
#            #print('Iceberg', a+1, 'is NOT towable')
#        
#        a += 1
#    
#    # final statement concluding 
#    label3 = Label(root, text = "Finished searching ocean for icebergs!")
#    #print('Finished searching ocean for icebergs...')
#    
#
#def close():
#    root.destroy()
#    
#
#root = Tk()
#
#button = Button(root, text="Show", command=printoutput) 
#button.pack()
#
#button = Button(master=root, text="Exit", command=close)
#button.pack(side=BOTTOM)
#
#root.mainloop()










'''
GRID METHOD
'''
def printoutput():
    list = 4
    list_tot_height = [1,2,5,6]
    list_mass = [44,67,25,41]
    
    a = 0
    while a < list:
#        label = Label(root, text = ("Iceberg", a+1, "is", list_tot_height[a], " m3, and, weighs", list_mass[a], "kg"))
        label = Label(root, text = ("Iceberg {} is {} m3 and weighs {} kg".format(a+1, list_tot_height[a], list_mass[a])))
        label.pack(side = TOP)
        
        #print('Iceberg', a+1, 'is', list_tot_height[a], 'm3 and weighs', list_mass[a], 'kg') # tot height + m3 are the same because counted up total 1m3 squares
       
        if list_mass[a] < 50:
            label1 = Label(root, text = ("Iceberg", a+1, "is towable"))
            label1.pack()
            #print('Iceberg', a+1, 'is towable')
            
        else:
            label2 = Label(root, text = ("Iceberg", a+1, "is NOT towable"))
            label2.pack()
            
            #print('Iceberg', a+1, 'is NOT towable')
        
        a += 1
    
    # final statement concluding 
    label3 = Label(root, text = "Finished searching ocean for icebergs!")
    #print('Finished searching ocean for icebergs...')
    

def close():
    root.destroy()
    

root = Tk()

button = Button(root, text="Show", command=printoutput) 
button.pack()

button = Button(master=root, text="Exit", command=close)
button.pack(side=BOTTOM)

root.mainloop()