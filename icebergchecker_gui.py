# -*- coding: utf-8 -*-
"""
Created December 2019

Author: R Martin, The University of Leeds, 201369797

Application to identify icebergs from .radar and .lidar files, assess their
towability and display the outcomes, including iceberg metadata, onto a GUI

https://www.geog.leeds.ac.uk/courses/computing/study/core-python/assessment2/ice.html

"""

# import libraries
import matplotlib.colors
import matplotlib.pyplot as mpl
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg)
import tkinter


# open radar file - 300m x 300m grid of m3 values between 0 and 255 where 100 or above is ice
with open("white2.radar") as f:
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

# open lidar file - 300m x 300m grid of m3 value between 0 and 255 where one lidar unit equals 10cm in height
with open("white2.lidar") as f:
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

        
# create copies of the data which can be altered without having to alter the orginal files
templidar = lidarenv
tempradar = radarenv 

# set up blank lists and counters for data that will be calculated for each iceberg
berg_tot_height = []
berg_mass = []
berg_dimension = []
berg_start_row = []
berg_start_col = []
num_of_bergs = 0


def find_ice(tempradar, templidar):
    
    '''
    Function to identity the location of any icebergs present 
    
    Check every cell in the radar file to see if an iceberg is present (radar
    value will be greater than 100 if ice is present). Pass to next cell if no
    ice found. If ice is found, add one to total number of icebergs, print 
    iceberg found, and its number and call function berg_footprint
        
    Params:
        tempradar - copy of the radarenv 2D array file
        templidar - copy of the lidarenv 2D array file
    Returns: 
        print statement - iceberg found and its number
    '''
    
    global num_of_bergs
    
    for i in range(numrows):
        for j in range(numcols):
            
#            print('///i,j:', i, j)
            if int(tempradar[i][j])<100: # if texture shows no ice present
                pass
                    
            else: # if texture shows ice is present
                num_of_bergs += 1
                
                print('iceberg', num_of_bergs, 'found')
                
#                print('--- i, j:', i, j)
                berg_footprint(tempradar, templidar, i, j)

 
def berg_footprint(tempradar, templidar, i, j):
    
    '''
    Function to trace iceberg footprint and append iceberg values
    
    This function will only be called if the find_ice function has identified
    the presence of an iceberg. 
    
    Identify the length of one row of an iceberg then, assuming all icebergs
    are square, sum the height of the entire iceberg before multiplying by
    900 kg/m3 (the mass density of ice) to get iceberg mass in kg. Append the
    iceberg dimension, height and mass to the corresponding arrays.
    
    Params:
        tempradar - copy of the radarenv 2D array file
        templidar - copy of the lidarenv 2D array file
        i - identifier for the number of rows
        j - identifier for the number of columns
    Returns:
        print statement - appending berg values for a stated iceberg number
    '''
    
#    print('checking berg footprint...') # shows successfully entered the function
    
    global berg_tot_height
    global berg_mass
    global berg_dimension
    global berg_start_row
    global berg_start_col
    global num_of_bergs
  
    berg_start_row.append(i) # write row into row [] starting at berg 0 which is the 1st berg
    berg_start_col.append(j) # write col into col [] starting at berg 0 which is the 1st berg
    dimension = 1
    height = 0

    carry_on = True

    while carry_on == True:
        if j == 299: # if on last column
            if i == 299: # and if on last row
                carry_on = False # stop
#                print('carry on is false - bottom corner of grid')
                
        elif radarenv[i][j+1] == 0: # if next m3 cell has no ice
                carry_on = False # stop
#                print('carry on is false - no neighbouring ice')
               
        elif radarenv[i][j+1] > 100: # if next m3 cell has ice
            j += 1 # add one to column
            dimension += 1
#            print('added one to dimension, total:', dimension)
         
    ii = berg_start_row[num_of_bergs-1] # copy of the start row for the number iceberg being looked at  
    
    while ii < (berg_start_row[num_of_bergs-1] + dimension):
        
        jj = berg_start_col[num_of_bergs-1] # copy of the start col for the number iceberg being looked at  
        
        while jj < (berg_start_col[num_of_bergs-1] + dimension):
            
#            print('ii:', ii, 'jj:', jj)
#            print('start height:', height)
#            print('cell value:', templidar[ii][jj])
            height = height + templidar[ii][jj] # cumulatively add height
#            print('end height:', height)

            tempradar[ii][jj] = 0 # set tempradar value to 0 so we know we have dealt with the ice present here
                       
            jj += 1
#            print('added j value:', jj)
       
        ii = ii + 1
#        print('added i value:', ii)

    mass = (height*900) # mass kg
    
    print('appending berg', num_of_bergs, 'values...')
    berg_dimension.append(dimension)
    berg_tot_height.append(height)
    berg_mass.append(mass)
    
    
# call the find_ice function
find_ice(tempradar, templidar)


## Return information about iceberg and print onto console
#a = 0 # set counter to 0 ready for while loop
#while a < num_of_bergs:
#    # tot height + m3 are the same because counted up total 1m3 squares
#    print('Iceberg', a+1, 'is', berg_tot_height[a], 'm3 and weighs', berg_mass[a], 'kg')
#   
#    if berg_mass[a] < 36000000: # where 36 million kg is the maximum iceberg weight that can be tugged
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
    Function to print iceberg metadata onto the GUI
    
    For each identified iceberg, display its number, size and weight on the GUI
    
    Returns:
        textual information - iceberg number and its size (m3) and weight (kg),
        whether or not the iceberg is or is NOT towable and a concluding
        statement that all icebergs have been identified 
    '''
    
    global berg_mass
    global berg_tot_height
    global num_of_bergs
    
    a = 0 # set counter to 0 ready for while loop
    while a < num_of_bergs:
       
        # tot height + m3 are the same because counted up total 1m3 squares
        label = tkinter.Label(root, text = ("Iceberg {} is {} m3 and weighs {} kg".format(a+1, berg_tot_height[a], berg_mass[a])))
        label.pack()
       
        if berg_mass[a] < 36000000: # where 36 million kg is the maximum iceberg weight that can be tugged
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
a = 0 # set counter to 0 ready for while loop
#print('start a:', a)
while a < num_of_bergs:

    ii = berg_start_row[a] # copy of the start row of the number iceberg being looked at  
    
    while ii < (berg_start_row[a] + berg_dimension[a]):
    
        jj = berg_start_col[a] # copy of the start col for the number iceberg being looked at  
           
        while jj < (berg_start_col[a] + berg_dimension[a]):
            
#            print('ii:', ii, 'jj:', jj)

            if berg_mass[a] < 36000000:
#                print('towable ii:', ii, 'jj:', jj)
                bergtowability[ii][jj] = 2
#                print('added 2 as towable')
                     
            else:
                bergtowability[ii][jj] = 0
#                print('added 0 as NOT toable')
                       
            jj += 1
#            print('added 1 to j:', jj)
        
        ii = ii + 1
#        print('added 1 to i:', ii)
    
    a += 1
#    print('new a:', a)


# displaying berg towability if using backend 'inline' and image appears in console
#mpl.title('Icebergs locations and tow-ability')
#cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", ["#d73027","#92c5de","#33a02c"]) # red, blue, green
#mpl.imshow(bergtowability, cmap = cmap)


# write textual data to file
f = open("icebergmetadata.txt", "w")
a = 0 # set counter to 0 ready for while loop
while a < num_of_bergs:
   
    f.write('Iceberg number %d is %d m3 and weighs %d kg. ' % (a+1, berg_tot_height[a], berg_mass[a]))  
   
    if berg_mass[a] < 36000000: # where 36 million kg is the maximum iceberg weight that can be tugged
        f.write('This iceberg is towable. \n')
        
    else:
        f.write('This iceberg is NOT towable. \n')
    
    a += 1 # add one to counter

f.close()


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

button2 = tkinter.Button(master=root, text="Show tow-ability values", command=printoutputs)
button2.pack(side=tkinter.TOP)
    
menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="File", menu=model_menu)
model_menu.add_command(label="Show tow-ability values", command=printoutputs)
model_menu.add_command(label="Exit model", command=close)

tkinter.mainloop()