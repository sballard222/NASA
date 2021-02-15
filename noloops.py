import sys
import math
import time
import numpy as np
from StringIO import StringIO

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Bad coding example 1
#
# Original Fortran version shamefully written by Ross Walker (SDSC, 2006)
#
# This code reads a series of coordinates and charges from the file
# specified as argument $1 on the command line.
#
# This file should have the format:
#  I9
# 4F10.4   (repeated I9 times representing x,y,z,q)
#
# It then calculates the following fictional function:
#
#             exp(rij*qi)*exp(rij*qj)   1
#    E = Sum( ----------------------- - - )  (rij <= cut)
#        j<i           r(ij)            a
#
# where cut is a cut off value specified on the command line ($2), 
# r(ij) is a function of the coordinates read in for each atom and 
# a is a constant.
#
# The code prints out the number of atoms, the cut off, total number of
# atom pairs which were less than or equal to the distance cutoff, the
# value of E, the time take to generate the coordinates and the time
# taken to perform the calculation of E.
#
# All calculations are done in double precision.
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

aval = 3.2

time0=time.clock()
print 'Value of system clock at start = %14.4f'%time0

# Step 1 - obtain the filename of the coord file and the value of
# cut from the command line.
#         Argument 1 should be the filename of the coord file (char).
#         Argument 2 should be the cut off (float).
argv=sys.argv
if len(argv) < 3:
   print "Too few arguments"
else:
   try:
      filename=argv[1]
      print "Coordinates will be read from file: %s"%filename
      cut=float(argv[2])
   except(TypeError,ValueError):
      print "Input error"

# Step 2 - Open the coordinate file and read the first line to
# obtain the number of atoms
fp=open(filename)
natom=int(fp.readline().strip())
     
print 'Natom = %d'% natom
print '  cut = %10.3e'% cut

# Step 3 - Set up the arrays to store the coordinate and charge data
#coords=np.zeros((natom*3,natom),dtype=float)
#q=[0]*natom
 
# Step 4 - read the coordinates and charges.
data=fp.read()
coords= np.genfromtxt(StringIO(data))

time1=time.clock()
print 'Value of system clock after coord read = %14.4f'%time1

a_ind=coords[:,0]
b_ind=coords[:,1]
c_ind=coords[:,2]
q_ind=coords[:,3]
a=np.zeros((natom,natom),dtype=float)
b=np.zeros((natom,natom),dtype=float)
c=np.zeros((natom,natom),dtype=float)
q=np.zeros((natom,natom),dtype=float)

for i in range(natom):
    a[:,i]=a_ind
    b[:,i]=b_ind
    c[:,i]=c_ind
    q[:,i]=q_ind

a_t=np.transpose(a)
b_t=np.transpose(b)
c_t=np.transpose(c)
q_t=np.transpose(q)

# Step 5 - calculate the number of pairs and E. - this is the
# majority of the work.
total_e = 0.0
cut_count = 0
vec2=np.zeros((natom,natom),dtype=float)
vec2=(a-a_t)**2+(b-b_t)**2+(c-c_t)**2
rij=np.sqrt(vec2)
e=np.zeros((natom,natom),dtype=float)
e=np.exp(rij*(q+q_t))/rij

cond_lists=np.zeros((natom,natom),dtype=bool)
cond_lists=[rij<=cut]
cond_lists2=[rij>0]

e_list=[e]
good_lists=np.select(cond_lists,e_list)
good_lists=[good_lists]
good_lists=np.select(cond_lists2,good_lists)

counts=np.sum(cond_lists)-natom

total_e = total_e + np.sum(good_lists) - counts*1.0/aval
total_e/=2
counts/=2
#time after reading of file and calculation
time2=time.clock()
print 'Value of system clock after coord read and E calc = %14.4f'%time2

# Step 6 - write out the results
print '                         Final Results' 
print '                         -------------'
print '                   Num Pairs = %14.4f ' %counts
print '                     Total E = %14.4f' %total_e
print '     Time to read coord file = %14.4f Seconds'% (time1-time0)
print '     Time to calculate E = %14.4f Seconds'% (time2-time1)
print '     Total Execution Time = %14.4f Seconds'% (time2-time0)

