# -*- coding: utf-8 -*-
"""
Created December 2019

Author: R Martin, The University of Leeds, 201369797

Application to identify icebergs from .lidar and .radar files, assess their
towability and present the outcomes, including iceberg metadata, on a GUI

https://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/ice.html

"""

# import libraries
import matplotlib.colors
import matplotlib.pyplot as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import tkinter


#  open files
with open("white2.radar") as f: # open radar file
    radarenv = []
    for line in f:
        parsed_line = str.split(line, ",")
        rowlist = []
        for value in parsed_line:
            rowlist.append(int(value))
        radarenv.append(rowlist)

numrows = len(radarenv)
numcols = len(radarenv[0])
#print('number of rows:', numrows)
#print('number of columns:', numcols)

## check has correctly read radar data
#mpl.title("Radar data")        
#mpl.imshow(radarenv)

with open("white2.lidar") as f: # open lidar file
    lidarenv = []
    for line in f:
        parsed_line = str.split(line, ",")
        rowlist = []
        for value in parsed_line:
            rowlist.append(int(value))
        lidarenv.append(rowlist)

## check has correctly read lidar data
#mpl.title("Lidar data")  
#mpl.imshow(lidarenv)

        
# create copies of the data which can be altered without damaging orginal files
templidar = lidarenv
tempradar = radarenv 

# set up lists for data that will be calculated for each iceberg
berg_tot_height = []
berg_mass = []
berg_dimension = []
berg_start_row = []
berg_start_col = []
num_of_bergs = 0


def find_ice(tempradar, templidar):
    
    '''
    Function to identity the location of any icebergs present, and return its 
    mass
    
    Params: tempradar, templidar
    Returns: iceberg number and its total mass (kg)
    '''
    
    global num_of_bergs
    
    for i in range(numrows):
        for j in range(numcols):
            
#            print('///i,j:', i, j)
            if int(tempradar[i][j])<100: # means it isn't ice
                pass
                    
            else:
                num_of_bergs += 1
                
                print('iceberg', num_of_bergs, 'found')
                
#                print('--- i, j:', i, j)
                berg_footprint(tempradar, templidar, i, j)

 
def berg_footprint(tempradar, templidar, i, j):
    
    '''
    Function to identify the length of a row of an icebergs, then, assuming
    all icebergs are square, calculate their mass
    
    Params: tempradar, templidar, i , j
    Returns: xxxx
    '''
    
#    print('checking berg footprint...') # successfully started the berg_footprint function
    
    global berg_tot_height
    global berg_mass
    global berg_dimension
    global berg_start_row
    global berg_start_col
    global num_of_bergs
  
    berg_start_row.append(i) # write row into row [] starting at berg 0 which is the 1st berg
    berg_start_col.append(j) # write row into col [] starting at berg 0 which is the 1st berg
    dimension = 1
    height = 0

    carry_on = True

    while carry_on == True:
        if j == 299: # if on last column
            if i == 299: # and if on last row
                carry_on = False # stop
                print('carry on is false - bottom corner')
                
        elif radarenv[i][j+1] == 0: # if next area has no ice
                carry_on = False # stop
#                print('carry on is false - no neighbouring ice')
               
        elif radarenv[i][j+1] > 100: # if next m3 does have ice
            j += 1 # look to column to the right
            dimension += 1
#            print('added one to dimension, total:', dimension)
         
    ii = berg_start_row[num_of_bergs-1] # because we append to the first item in a list
    
    while ii < (berg_start_row[num_of_bergs-1] + dimension):
        
        jj = berg_start_col[num_of_bergs-1] # because we append to the first item in a list
        
        while jj < (berg_start_col[num_of_bergs-1] + dimension):
            
#            print('ii:', ii, 'jj', jj)
#            print('start height:', height)
#            print('cell value:', templidar[ii][jj])
            height = height + templidar[ii][jj]
#            print('end height:', height)

            tempradar[ii][jj] = 0 # set radar to 0 so we know we have looked at ice here
                       
            jj += 1
#            print('after jj, ii:', ii)
       
        ii = ii + 1
#        print('added i value:', i)

    mass = (height*900) # mass kg
    
    print('appending berg', num_of_bergs, 'values...')
    berg_dimension.append(dimension)
    berg_tot_height.append(height)
    berg_mass.append(mass)
    
    
# Call the iceberg function - this calls the berg_footprint function itself
find_ice(tempradar, templidar)


## Return information about iceberg and print into console
#a = 0 # set counter to 0 ready for while loop
#while a < num_of_bergs:
#    print('Iceberg', a+1, 'is', berg_tot_height[a], 'm3 and weighs', berg_mass[a], 'kg') # tot height + m3 are the same because counted up total 1m3 squares
#   
#    if berg_mass[a] < 36000000:
#        print('Iceberg', a+1, 'is towable')
#        
#    else:
#        print('Iceberg', a+1, 'is NOT towable')
#    
#    a += 1 # add one to counter
#
## final statement concluding 
#print('Finished searching ocean for icebergs!')


def printoutputs():
    '''
    Function to display the size and weight for each identified iceberg on
    the GUI interface
    
    Returns: Textual information:
        Iceberg x, is y m3 and weighs z kg
        Iceberg is or is NOT towable
        A concluding statement that all icebergs have been identified
    
    '''
    
    global berg_mass
    global berg_tot_height
    global num_of_bergs
    
    a = 0 # set counter to 0 ready for while loop
    while a < num_of_bergs:
        
        label = tkinter.Label(root, text = ("Iceberg {} is {} m3 and weighs {} kg".format(a+1, berg_tot_height[a], berg_mass[a]))) # tot height + m3 are the same because counted up total 1m3 squares
        label.pack()
       
        if berg_mass[a] < 36000000:
            label1 = tkinter.Label(root, text = ("Iceberg {} is towable".format(a+1)))
            label1.pack()
            
        else:
             label2 = tkinter.Label(root, text = ("Iceberg {} is NOT towable".format(a+1)))
             label2.pack()
        
        a += 1 # add one to counter
    
    label3 = tkinter.Label(root, text = "Finished searching ocean for icebergs!")
    label3.pack()


# set up data grid ready for displaying figure of towability
bergtowability = [[1] * numrows for n in range(numcols)]

# assign towability values (ready for figure presentation)
a = 0  # set counter to 0 ready for while loop
#print('start a:', a)
while a < num_of_bergs:

    ii = berg_start_row[a] # because we append to the first item in a list
    
    while ii < (berg_start_row[a] + berg_dimension[a]):
    
        jj = berg_start_col[a] # because we append to the first item in a list
           
        while jj < (berg_start_col[a] + berg_dimension[a]):
            
#            print('ii:', ii, 'jj:', jj)
                
            if berg_mass[a] < 36000000:
                
#                print('towable ii:', ii, 'jj:', jj)
                bergtowability[ii][jj] = 2
#                print('added 1 to towable')
                     
            else:
                bergtowability[ii][jj] = 0
#                print('added 2 to NOT toable')
           
            
#            print('end jj:', jj)
            jj += 1
#            print('added 1 to j:', jj)
        
#        print('end ii:', ii)
        ii = ii + 1
#        print('added 1 to i:', ii)
    
    a += 1
#    print('new a:', a)


# displaying berg towability if using backend 'inline' and image appears in console
#mpl.title('Icebergs locations and tow-ability')
#cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["#d73027","#92c5de","#33a02c"]) # red, blue, green
#mpl.imshow(bergtowability, cmap = cmap)


# set up GUI
root = tkinter.Tk()
root.wm_title("White Star Line Iceberg Checker")

fig = mpl.figure(1)
mpl.title('Icebergs locations and their tow-ability')
mpl.xlabel('Distance (m)')
mpl.ylabel('Distance (m)')
 
cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["#d73027","#92c5de","#33a02c"]) # red, blue, green
mpl.imshow(bergtowability, cmap = cmap)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

def close():
    root.destroy()

button1 = tkinter.Button(master=root, text="Exit", command=close)
button1.pack(side=tkinter.BOTTOM)

button2 = tkinter.Button(master=root, text="Show towability values", command=printoutputs)
button2.pack(side=tkinter.TOP)
    
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="File", menu=model_menu)
model_menu.add_command(label="Exit model", command=close)

tkinter.mainloop()