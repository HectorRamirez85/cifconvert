import os
import cifconvert.main as cifconvert
import cifconvert.merge as cifmerge

datadir = os.getcwd() + "/"

cifconvert(datadir + "example.cif", datadir + "example.h5",46, 43)
cifconvert()

cifmerge