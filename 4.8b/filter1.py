######################################
#   Eliminating Digital Noise Code   #
#                                    #
#             UTeach CSP             #
#             Brian Ford             #
#                                    #
#              9/13/19               #
#                                    #
######################################



#I MODIFIED THIS TO WORK ON LINUX OUTSIDE OF REPL.IT JUST LOOK AT THE CODE IT WONT RUN ON REPEL.IT

# importing PIL.Image library and os library
from PIL import Image 
import os

#Get the current working directory
cwd = os.getcwd() + "/4.8b"
print(cwd)

# Deletes old created images if they exist
if os.path.exists(cwd + "/newImage.jpg"):
  os.remove(cwd + "/newImage.jpg")

# Prints two blank lines to start our program output
print("\n\n")

# Opens image - Local File in repl.it
img = Image.open(cwd + '/image.jpg')

# Rescale image size down, if needed
width = img.width
height = img.height
mwidth = width // 1000
mheight = height // 1000
if mwidth > mheight:
  scale = mwidth
else:
  scale = mheight
if scale != 0:
  img = img.resize( (width // scale, height // scale) )

########################
#        Filter        #
########################
def newFilter(value):
  # Starts at the first pixel in the image
  location = 0
  # Continues until it has looped through all pixels
  while location < len(new_pixels):
    # Gets the current color of the pixel at location
    p = new_pixels[location]
    # Splits color into red, green and blue components
    r = p[0]
    g = p[1]
    b = p[2]
    # Perform pixel manipulation and stores results
    # to a new red, green and blue components
    newr = r + value
    newg = g + value
    newb = b + value
    # Assign new red, green and blue components to pixel
    # at that specific location
    new_pixels[location] = (newr, newg, newb)
    # Changes the location to the next pixel in array
    location = location + 1
  # Creates a new image, the same size as the original 
  # using RGB value format
  newImage = Image.new("RGB", img.size)
  # Assigns the pixel values to newImage
  newImage.putdata(new_pixels)
  # Saves the new image file
  newImage.save(cwd + "/newImage.jpg")

# Creates an ImageCore Object from original image
pixels = img.getdata()
# Creates empty array to hold new pixel values
new_pixels = []
# For every pixel from our original image, it saves
# a copy of that pixel to our new_pixels array
for p in pixels:
  new_pixels.append(p)

# Calls the newFilter function to create the image
value = int(input("Enter an integer from 0 - 255: "))
newFilter(value)
