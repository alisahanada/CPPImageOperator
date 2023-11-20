# TODO: you will need to install cv2
# Run "pip3 install opencv-python" in CLI
import cv2
import sys
# Kaleidoscope requires numpy. Uncomment this line and install it if you need to.
import numpy as np

# Store command line arguments in variables
# TODO: change the next line to store the filename
filename = sys.argv[1]
manip = sys.argv[2]

# Open the image file
img = cv2.imread(filename)
# Get the dimensions (in pixels) of the image
dimensions = img.shape
# Copy the original image into an image for manipulation
img_manip = cv2.resize(img, (dimensions[1], dimensions[0]))
# TODO: Store white in a list, where each of the three parts is on a scale of [0, 255]
white = [255,255,255]
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        if manip == 'flip':
            img_manip[x, y] = img[dimensions[0]-1-x, y]
        elif manip == 'mirror':
            # TODO: mirror the image and store in img_manip[x, y]
            img_manip[x,y] = img[x,dimensions[1] - 1 - y]
            pass

        elif manip == 'invert':
            # TODO: invert the image and store in img_manip[x, y]
            # Hint: img[x, y] returns the color of the pixel at that coordinate.
            # You can invert by subtracting that color from white.
            img_manip[x,y]=white-img[x,y]
            pass


# Display the kaleidoscope image for the "mirror" operation
if manip == 'mirror':
    # Displays the original image in the top left corner of the screen.
    image = 'Original image'
    cv2.namedWindow(image)
    cv2.moveWindow(image, 0, 0)
    cv2.imshow(image, img)

    img_mirror_x = img[::-1, :, :]

    # Display the mirrored image alongside the original and manipulated images.
    # image = 'Mirror X-axis'
    # cv2.namedWindow(image)
    # cv2.moveWindow(image, 2 * dimensions[0] + 2, 0)
    # cv2.imshow(image, img_mirror_x)

    # Concatenate horizontally
    horizontal_concat = np.concatenate((img, img_manip), axis=1)

    # Flip the horizontal concatenation vertically
    flipped_horizontal_concat = horizontal_concat[::-1, :, :]

    # Concatenate the flipped horizontal concatenation with itself vertically
    kaleidescope = np.concatenate((horizontal_concat, flipped_horizontal_concat), axis=0)

    # Display the vertically concatenated image
    image = 'Kaleidescope'
    cv2.namedWindow(image)
    cv2.moveWindow(image, 0, dimensions[1] + 1)
    cv2.imshow(image, kaleidescope)

    # Create a kaleidoscope image by mirroring on both X and Y axes
    # kaleidoscope = cv2.flip(cv2.flip(img, 1), 0)
    # cv2.imshow(image, kaleidoscope)
else:
    # Displays the original image in the top left corner of the screen.
    image = 'Original image'
    cv2.namedWindow(image)
    cv2.moveWindow(image, 0, 0)
    cv2.imshow(image, img)

    # TODO: Display the manipulated image alongside the original image.
    image = 'Manipulated image'
    cv2.namedWindow(image)
    cv2.moveWindow(image, dimensions[0] + 1, 0)
    cv2.imshow(image, img_manip)



# TODO: Create a kaleidoscope image, display it, and save it to a file.
# This line puts two images side-by-side in one window.
#horizontal_concat = np.concatenate((img, img_manip), axis=1)
# TODO: Save the image using the imwrite method from cv2
# TODO: Show the image
#cv2.imshow('Horizontal Concatenation!', horizontal_concat)
# for x in range(dimensions[0]):
#     for y in range(dimensions[1]):
#         # TODO: mirror the image and store in img_manip[x, y]
#         img_manip[x,y] = img[x,dimensions[1]-1-y]
#         pass
# horizontal_concat = np.concatenate((img, img_manip), axis=1)
# cv2.imshow('Horizontal Concatenation!', horizontal_concat)

# for x in range(dimensions[0]):
#     for y in range(dimensions[1]):
#         # TODO: mirror the image and store in img_manip[x, y]
#         img_manip[x, y] = horizontal_concat[dimensions[0]-1-x, y]
#         pass

# cv2.imshow('Horizontal Concatenation!', img_manip[x,y])

# Infinite loop to keep the windows open until the escape key is pressed.
while True:
    k = cv2.waitKey(1)
    if k == 27:
        cv2.destroyAllWindows()
        exit()

