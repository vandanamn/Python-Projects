# PYTHON PROJECT TO CONVERT JPG FILE TO PNG FILE #
# Arguments provided are two folder names. 
# One folder which contains all the jpg files and the other one to which the converted files are stored.
import sys
import os
from PIL import Image
Destn = (sys.argv[2])
if not os.path.exists(Destn):    # If folder doesn't exist, then create it.
	os.makedirs(Destn)
	print("New folder created: ", Destn)
for filename in os.listdir(sys.argv[1]):
	if filename.endswith(".jpg"):
		im = Image.open(f'{sys.argv[1]}{filename}')
		name=filename.replace('.jpg','.png')
		im.save(f'{Destn}{name}')
		c+=1
	print('IMAGE SUCCESSFULLY CONVERTED!')   