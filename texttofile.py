# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 14:36:29 2020

@author: Perfe
"""

# write a file



#f= open("guru99.txt","w+")
#for i in range(11):
#     f.write("This is line %d\r\n" % (i+1))
#f.close() 

#a = [4,5,6]
#b = [12, 15, 16]
#
#f= open("guru99.txt","w+")
#for i in range(3):
#     f.write('Iceberg number %d is %d m3 and weighs %d kg \n' % ((i+1), (a[i]), (b[i])))
#f.close() 


a = [4,5,6]
b = [12, 15, 16]

f= open("guru99.txt","w")
c = 0
while c < 3:
     f.write('Iceberg number %d is %d m3 and weighs %d kg. \n' % ((c), (a[c]), (b[c])))
     
     if b[c] < 15:
         f.write('Iceberg %d is towable. \n' % (c))
     
     else:
         f.write('Iceberg %d is NOT towable! \n' % (c))
    
     c += 1
f.close() 
    
    

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