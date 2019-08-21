
#A template for the ahnen

# Import everything from vpython 
#
import pandas as pan
import matplotlib

csv_path = "/home/grabmayr/samml-windows/privat/ahnen-test.csv"
data = pan.read_csv(csv_path, sep=';')

print  (csv_path)
print (' data read y')

print(' !!!!!!!!!!!!!!!!!!!!!!!!!!! ')
print (data[0:5])
print(' !!!!!!!!!!!!!!!!!!!!!!!!!!! ')
print(data.columns)
print(' !!!!!!!!!!!!!!!!!!!!!!!!!!! ')
print(type(data))
print(' !!!!!!!!!!!!!!!!!!!!!!!!!!! ')
print(data.info())
print(' !!!!!!!!!!!!!!!!!!!!!!!!!!! ')

# Set up display
#scene.width      = 840 #1680
#scene.height     = 512 #1024
#scene.background = color.white
#scene.center     = vector(0, -2, 0)

# Definition of parameters


# Initialize 
