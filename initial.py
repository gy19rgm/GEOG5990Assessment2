# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:12:30 2019

Author: R Martin, The University of Leeds, 201369797

"""

# import libraries
import matplotlib.pyplot as mpl

# open radar file
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

# open lidar file
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
        
# create copies of the data which can be altered without damaging orginal files
templidar = lidarenv
tempradar = radarenv       

# set up lists for data which will be calculated for each iceberg
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
            
#            print('//// i, j:', i, j)
            if int(tempradar[i][j])<100: # means it isn't ice ''better to be i, j '''
                pass
                    
            else:
                num_of_bergs += 1
                
                print('ice found')
                
#                print('------ i, j:', i,j)
                berg_footprint(tempradar, templidar, i, j)

#                mpl.imshow(tempradar)
                
 
def berg_footprint(tempradar, templidar, i, j):
    
    '''
    Function to identify the length of a row of an icebergs, then, assuming
    all icebergs are square, calculate their mass
    
    Params: tempradar, templidar, i , j
    Returns: xxxx
    '''
 
    print('checking berg footprint...')
    
    global berg_tot_height
    global berg_mass
    global berg_dimension
    global berg_start_row
    global berg_start_col
    global num_of_bergs
    
    print('this is berg number', num_of_bergs)
    
    berg_start_row.append(i) # write row into row [] starting at berg 0 which is the 1st berg
    berg_start_col.append(j) # write row into col [] starting at berg 0 which is the 1st berg

    dimension = 1
    height = 0
    
    
    carry_on = True

    while carry_on == True:
        if j == 299: # if on last column
            if i == 299: # and if on last row
                carry_on = False # stop
#                print('carry on is false - bottom corner')
                
        elif radarenv[i][j+1] == 0: # if next area has no ice
#            if i == 299:
                carry_on = False # stop
#                print('carry on is false - no next door ice')
                
        elif radarenv[i][j+1] > 100: # if next m3 does have ice
            j += 1 # look to column to the right
            dimension += 1
#            print('added one to dimension. total:', dimension) 
         
    ii = berg_start_row[num_of_bergs-1] # because we append to the first item in a list
    
    while ii < (berg_start_row[num_of_bergs-1] + dimension):
        
        jj = berg_start_col[num_of_bergs-1] # because we append to the first item in a list
        
        while jj < (berg_start_col[num_of_bergs-1] + dimension):
            
#            print('ii:', ii, 'jj:', jj)
#            print('start height:', height)
#            print('value:', templidar[ii][jj])
            height = height + templidar[ii][jj]
#            print('end height:', height)

            tempradar[ii][jj] = 0 # set radar to 0 so we know we have looked at ice here
                       
            jj += 1
#            print('after jj, ii:', ii)
       
        ii = ii + 1 
#        print('added i value:', i)


    mass = (height*900) # mass kg

    print('appending values')
    berg_dimension.append(dimension)
    berg_tot_height.append(height)
    berg_mass.append(mass)
    
# Call the iceberg function - this calls the berg_footprint function itself
find_ice(tempradar, templidar)

# Return information about iceberg
a = 0
while a < num_of_bergs:
    print('Iceberg', a+1, 'is', berg_tot_height[a], 'm3 and weighs', berg_mass[a], 'kg') # tot height + m3 are the same because counted up total 1m3 squares
   
    if berg_mass[a] < 36000000:
        print('Iceberg', a+1, 'is towable')
        
    else:
        print('Iceberg', a+1, 'is NOT towable')
    
    a += 1


# Final statement concluding 
print('Ocean completely searched for icebergs!')


# make graph
mpl.imshow(lidarenv)
mpl.title('Icebergs')


# GUI - using label widgits   . Scrolled text widgit    
         
 

      
 
 
     






'''
# plot figures
fig,a = mpl.subplots(2, 2, sharex=True, sharey=True)
a[0][0].imshow(lidarenv)
a[0][0].set_title('lidar data')
a[0][1].imshow(radarenv)
a[0][1].set_title('radar data')
#a[1][0].imshow(tempradar)
#a[1][0].set_title('unanalysed data')
mpl.show()
'''