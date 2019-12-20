# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 12:12:30 2019

Author: gy19rgm, The University of Leeds 201369797

"""

# import libraries
import matplotlib.pyplot as mpl

# open radar file
with open("white1.radar") as f:
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
with open("white1.lidar") as f:
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

berg_tot_height = []
berg_mass = []
berg_dimension = []
berg_start_row = []
berg_start_col = []
num_of_bergs = 0


# define functions
def find_ice(tempradar, templidar):
    
    '''
    Function to identity the location of any icebergs present, and return its mass
    
    Params: tempradar, templidar
    Returns: iceberg number and its total mass (kg)
    '''
#    mpl.imshow(tempradar) 

    
    global berg_tot_height
    global berg_mass
    global berg_dimension
    global berg_start_row
    global berg_start_col
    global num_of_bergs
    
    for i in range(numrows):
        for j in range(numcols):
            if int(tempradar[j][i])<100: # means it isn't ice ''better to be i, j '''
                pass

#            else: # when is ice
#                tot_mass,templidar,tempradar = calc_mass(tempradar, templidar, j, i) # start point as point as grid
#               
#                if tot_mass != 0: 
#                    ''' issue here '''
#               #     num_of_bergs += 1
#                    ''' set up array? '''
#                    print("Iceberg", num_of_bergs, "is", tot_mass, 'kg. j=', j, 'i=', i)
                    
            else:
                num_of_bergs += 1
                
                berg_footprint(tempradar, templidar, j, i)

#    mpl.imshow(tempradar) 
    
def berg_footprint(tempradar, templidar, j, i):
    
    global berg_tot_height
    global berg_mass
    global berg_dimension
    global berg_start_row
    global berg_start_col
    global num_of_bergs

## appends!
''' list index out of range, update specific xxx in list'''
    berg_start_row[num_of_bergs].append(i)
        
    berg_start_row[num_of_bergs] = i # write row into row [] starting at berg 1
    berg_start_col[num_of_bergs] = j # write col into row [] starting at berg 1
    berg_dimension[num_of_bergs] = 1
    
    carry_on = True

    while carry_on == True:
        if j == 299:
            if i == 299 :
                carry_on = False
                
        elif radarenv[j+1][i] == 0: # if next area has no ice
            if i == 299 :
                carry_on = False
                
        elif radarenv[j+1][i]>100: # if next m3 does have ice
            berg_dimension[num_of_bergs] += 1
          
    ii = berg_start_row[num_of_bergs]
    jj = berg_start_col[num_of_bergs]
    
    while ii <= (berg_start_row[num_of_bergs] + berg_dimension[num_of_bergs]):
        while jj <= (berg_start_col[num_of_bergs] + berg_dimension[num_of_bergs]):
            
            berg_tot_height[num_of_bergs] = (berg_tot_height[num_of_bergs] + templidar[ii][jj])
            tempradar[ii][jj] = 0 # set radar to 0 so we know we have looked at ice here
            
            jj += 1
        ii += 1 
        ''' if error, check indentations here '''

    berg_mass[num_of_bergs] = (berg_tot_height[num_of_bergs]*900) # mass kg
    


    
          
            
    
    
            

def calc_mass(tempradar, templidar, j, i):
    ''' 
    Function to calculate the mass of an iceberg from total height values
    
    Params: tempradar, templidar, j, i
    Returns: tot_mass, templidar, tempradar
    '''
    
    results = berg_sum(tempradar, templidar, j, i)
    
    tot_mass=results[0]
    size = results[1]
    templidar = results[2]
    tempradar = results[3]
    
#    tot_mass = (tot_mass/10) # divide my ten to convert units to metres
#    tot_mass = (tot_mass*10) # to get full height, not just height asl
###    tot_mass = (tot_mass*size) 
#    tot_mass = (tot_mass*900) #kgm3 of ice
    
    tot_mass = (tot_mass*900)
    
    return (tot_mass, templidar, tempradar)
  
    

def berg_sum(tempradar, templidar, j, i): 

    '''
    Function to calculate the cumulative height of an iceberg for a whole iceberg, one row at a time
    
    Params: tempradar, templidar, j, i
    Returns: tot_height, m3, templidar, tempradar
    '''

    starting_j=j    

    tot_height = templidar[j][i] # set total height as the height of the square we identified as ice 
    m3 = 1 # start counting the size of this iceberg in m3

    carry_on = True
    
    while carry_on == True:
        #print (starting_j,j,i)
        if j == 299:
            templidar[j][i] = 0
            tempradar[j][i] = 0
            if i == 299 :
                carry_on=False
            elif templidar[starting_j][i+1] == 0:
                carry_on=False
            else:
                j=starting_j    
                i+=1   
                tot_height = tot_height + templidar[j][i]
            
        elif radarenv[j+1][i] == 0: # if next area has no ice
            templidar[j+1][i] = 0
            tempradar[j+1][i] = 0
            if i == 299 :
                carry_on=False
            elif templidar[starting_j][i+1] == 0:
                carry_on=False
            else:
                j=starting_j    
                i+=1
                tot_height = tot_height + templidar[j][i]
        
            
        elif radarenv[j+1][i]>100: # if next m3 does have ice
            tot_height = tot_height + templidar[j+1][i] # add it's height to first m3
            m3 += 1 # add 1 to m3 so we know how big the berg is for later maths
            templidar[j+1][i] = 0
            tempradar[j+1][i] = 0
            j += 1
        
    return (tot_height, m3, templidar, tempradar)








''' call functions (from agent called Icebergs?) '''

'''
# plot figures
fig,a = mpl.subplots(2, 2, sharex=True, sharey=True)
a[0][0].imshow(lidarenv)
a[0][0].set_title('lidar')
a[0][1].imshow(radarenv)
a[0][1].set_title('radar')
#a[1][0].imshow(icebergs)
#a[1][0].set_title('icebergs')
mpl.show()
'''