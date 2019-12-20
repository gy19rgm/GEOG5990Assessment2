# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 20:33:27 2019

Author: R Martin, The University of Leeds, 201369797
"""
    
def find_ice(tempradar, templidar):

 
#    Function to identity the location of any icebergs present, and return its 
#    mass
#    
#    Params: tempradar, templidar
#    Returns: iceberg number and its total mass (kg)


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
    
    print('this is berg', num_of_bergs)
    
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
#            if i == 299:
                carry_on = False # stop
                print('carry on is false - no next door ice')
                
        elif radarenv[i][j+1] > 100: # if next m3 does have ice
            j += 1 # look to column to the right
            dimension += 1
#            print('added one to dimension. total:', dimension) 
         
    ii = berg_start_row[num_of_bergs-1] # because we append to the first item in a list
    
    while ii < (berg_start_row[num_of_bergs-1] + dimension):
        
        jj = berg_start_col[num_of_bergs-1] # because we append to the first item in a list
        
        while jj < (berg_start_col[num_of_bergs-1] + dimension):
            
            print('ii:', ii, 'jj:', jj)
#            print('start height:', height)
#            print('value:', templidar[ii][jj])
            height = height + templidar[ii][jj]
            print('end height:', height)

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