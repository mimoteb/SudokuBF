from base64 import b16decode
import numpy as np
sgrid = np.array([[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]])
l0 = np.array(sgrid[0])
l1 = np.array(sgrid[1])
l2 = np.array(sgrid[2])
l3 = np.array(sgrid[3])
l4 = np.array(sgrid[4])
l5 = np.array(sgrid[5])
l6 = np.array(sgrid[6])
l7 = np.array(sgrid[7])
l8 = np.array(sgrid[8])
lines = [l0,l1,l2,l3,l4,l5,l6,l7,l8]

c0 = np.array([l0[0], l1[0],l2[0],l3[0],l4[0],l5[0],l6[0],l7[0],l8[0]])
c1 = np.array([l0[1],l1[1],l2[1],l3[1],l4[1],l5[1],l6[1],l7[1],l8[1]])
c2 = np.array([l0[2],l1[2],l2[2],l3[2],l4[2],l5[2],l6[2],l7[2],l8[2]])
c3 = np.array([l0[3],l1[3],l2[3],l3[3],l4[3],l5[3],l6[3],l7[3],l8[3]])
c4 = np.array([l0[4],l1[4],l2[4],l3[4],l4[4],l5[4],l6[4],l7[4],l8[4]])
c5 = np.array([l0[5],l1[5],l2[5],l3[5],l4[5],l5[5],l6[5],l7[5],l8[5]])
c6 = np.array([l0[6],l1[6],l2[6],l3[6],l4[6],l5[6],l6[6],l7[6],l8[6]])
c7 = np.array([l0[7],l1[7],l2[7],l3[7],l4[7],l5[7],l6[7],l7[7],l8[7]])
c8 = np.array([l0[8],l1[8],l2[8],l3[8],l4[8],l5[8],l6[8],l7[8],l8[8]])
columns =[c0,c1,c2,c3,c4,c5,c6,c7,c8]

