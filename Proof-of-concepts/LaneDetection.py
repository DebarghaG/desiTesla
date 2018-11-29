"""

The following algorithms come to us courtesy of the assignment on Udacity's Self Driving Car Nanodegreeself.

They're being re-incorporated into our code to better understand lanes and extract them.

"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
import math
import os
from moviepy.editor import VideoFileClip
from IPython.display import HTML

"""Applies a transform to convert the image into grayscale"""
def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

"""Applies the Canny transform"""
def canny(img, low_threshold, high_threshold):
    return cv2.Canny(img, low_threshold, high_threshold)

"""Applies a Gaussian Noise kernel"""
def gaussian_blur(img, kernel_size):

    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

"""
Applies an image mask.

Only keeps the region of the image defined by the polygon
formed from `vertices`. The rest of the image is set to black.
"""
def region_of_interest(img, vertices):
    #defining a blank mask to start with
    mask = np.zeros_like(img)

    #defining a 3 channel or 1 channel color to fill the mask with depending on the input image
    if len(img.shape) > 2:
        channel_count = img.shape[2]  # i.e. 3 or 4 depending on your image
        ignore_mask_color = (255,) * channel_count
    else:
        ignore_mask_color = 255

    #filling pixels inside the polygon defined by "vertices" with the fill color
    cv2.fillPoly(mask, vertices, ignore_mask_color)

    #returning the image only where mask pixels are nonzero
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    """
    NOTE: this is the function you might want to use as a starting point once you want to
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).

    Think about things like separating line segments by their
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of
    the lines and extrapolate to the top and bottom of the lane.

    This function draws `lines` with `color` and `thickness`.
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    """
    `img` should be the output of a Canny transform.

    Returns an image with hough lines drawn.
    """
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((*img.shape, 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

# Python 3 has support for cool math symbols.

def weighted_img(img, initial_img, α=0.8, β=1., λ=0.):
    """
    `img` is the output of the hough_lines(), An image with lines drawn on it.
    Should be a blank image (all black) with lines drawn on it.

    `initial_img` should be the image before any processing.

    The result image is computed as follows:

    initial_img * α + img * β + λ
    NOTE: initial_img and img must be the same shape!
    """
    return cv2.addWeighted(initial_img, α, img, β, λ)


def polygon_from_shape(imshape, delta=0.5, d=25):
    """
    `poligon_from_shape` identifies a symmetric poligon (isosceles trapezoid)
    from the bottom of the image
    First, you imagine a triangle where:
    - the base is at the bottom of the picture, with length imshape[1]
    - the heigth "delta" is set (by default=0.5) in the middle of the picture
      but can be moved at the top (delta=0)
      or actually at the bottom (delta=1)
    Second, you want to cut a little triangle
    at the top of the just made bigger one
    - where the length of its heigth is of "d" pixels (default d=25)
    Once cut, you get your centered polygon

    NOTE: Be careful, current version needs a lot of coherence checks
    """

    H = imshape[0] # vertical length
    B = imshape[1] # horizontal length

    # to build a triangle with a vertex in the middle of the picture
    h = H * delta
    myRatio = float(B) / float(h)

    # s, the small half-base of the small tringle
    s = int (d * myRatio / 2.)

    # now, you can draw your four sided polygon to mask
    vertices = np.array([[(0,H),(B/2-s, h+d), (B/2+s, h+d), (B,H)]], dtype=np.int32)
    h_d = h+d
    return vertices, h_d

def lane_from_lines(img,lines2,h_d,h_max):
    """
    `lane_from_lines` return left and rigth lanes
    from red lanes drawn over a black picture (lanes2).
    Also, it needs "h_d" the heigth of the trapezoid
    and "h_max" the total height of the picture.(see the "polygon_from_shape" function)

    NOTE: Be careful, current version needs a coherent polygon_from_shape function

    """
    #creating a blank to draw lines on
    line_image = np.copy(img)*0

    # Extract point
    x1=np.reshape(np.hstack(lines2),[len(lines2),4])[:,0]
    y1=np.reshape(np.hstack(lines2),[len(lines2),4])[:,1]
    x2=np.reshape(np.hstack(lines2),[len(lines2),4])[:,2]
    y2=np.reshape(np.hstack(lines2),[len(lines2),4])[:,3]

    # y = mx + q
    # NOTE: henceforth we work with y axis rolled up-down (x is ok)

    # Check for vertical lines
    m_inf = (x2-x1) == 0

    # Check for horizontal lines
    # m_0 = (y2-y1) == 0

    # set m and q to 0.
    m = x1 * 0.
    q = y1 * 0.

    # m and q will assume a decent value or stay zero
    m[~m_inf] = (y2[~m_inf] - y1[~m_inf]) / (x2[~m_inf] - x1[~m_inf])
    q[~m_inf] =  y2[~m_inf] -  m[~m_inf]  *  x2[~m_inf]

    top_x    = x1 * 0. # if rare and still 0 median should exclude it
    bottom_x = x1 * 0. # if rare and still 0 median should exclude it
    top_x[~m_inf]    = (h_d   - q[~m_inf]) / m[~m_inf]
    bottom_x[~m_inf] = (h_max - q[~m_inf]) / m[~m_inf]

    rigth = m > 0 # the image is rolled up-down!

    # Draw left line
    x1 = int(np.median(bottom_x[~rigth])+0.5) # median is more robust than any mean
    y1 = int(h_max)
    x2 = int(np.median(top_x   [~rigth])+0.5)
    y2 = int(h_d)
    cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

    # Draw rigth line
    x1 = int(np.median(bottom_x[rigth])+0.5)
    y1 = int(h_max)
    x2 = int(np.median(top_x   [rigth])+0.5)
    y2 = int(h_d)
    cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),10)

    return line_image


def image_pipeline(image, display=False):
    """
    `image_pipeline` is the mainstream program for testing
    lines detection on single images

    "image" will be / must be a picture

    For displaying (all) intermediate images, set "display" to True

    This function could be improved:
    - automating "triangle cut" dimension "d" to have an intelligent trapezoid
    - weighting segments (with the length of each segment) when calculating medians
    """

    if display:
        # Print out some stats
        print('This image is: ',type(image),'with dimensions:',image.shape)

    # Pull out the x and y sizes and make a copy of the image
    ysize = image.shape[0]
    # xsize = image.shape[1]

    # Grayscale the image
    gray = grayscale(image)

    # Define a kernel size and apply Gaussian smoothing
    kernel_size = 5
    blur_gray = gaussian_blur(gray, kernel_size)

    # Define parameters for Canny and apply
    low_threshold = 80
    high_threshold = 200
    edges = canny (blur_gray, low_threshold, high_threshold)

    # Define the Hough transform parameters
    rho = 1
    theta = np.pi/180
    threshold = 20 # was 20
    min_line_len = 10 #was 10
    max_line_gap = 20 # was 16

    # Run Hough on edge detected image
    line_img = hough_lines(edges, rho, theta, threshold, min_line_len, max_line_gap)

    # Define four sided polygon to mask
    vertices,h_d = polygon_from_shape(line_img.shape, delta=0.5, d=60)

    # Apply the image mask.
    masked_edges = region_of_interest(line_img, vertices)

    # Redo Canny & Hough on the selected line_img
    edges2 = canny (masked_edges, low_threshold, high_threshold)
    lines2 = cv2.HoughLinesP(edges2, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)

    # Find the two lines (outputs from polygon_from_shape are needed!)
    line_image = lane_from_lines(masked_edges,lines2,h_d,ysize)

    # Draw the lines on the edge image
    combo = cv2.addWeighted(image, 0.8, line_image, 1, 0)

    # Display all the (modified) images
    if display:
        plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
        plt.imshow(image);plt.show()
        plt.xticks([]), plt.yticks([]);plt.imshow(gray, cmap='gray');plt.show()
        plt.xticks([]), plt.yticks([]);plt.imshow(blur_gray, cmap='gray');plt.show()
        plt.xticks([]), plt.yticks([]);plt.imshow(edges, cmap='Greys_r');plt.show()
        plt.imshow(line_img);plt.show()
        plt.imshow(masked_edges);plt.show()
        plt.imshow(edges2, cmap='Greys_r');plt.show()
        plt.imshow(line_image);plt.show()
        plt.xticks([]), plt.yticks([]);plt.imshow(combo);plt.show()

    return combo


for myImg in my_image_list:

    # Read in the image
    file_in = "".join(["input/test_images/",myImg])
    image = mpimg.imread(file_in)

    # Run mainstream program for testing lines detection
    result = image_pipeline(image, display=False)

    # Save the result array as image file
    file_out = "_".join(["output/my_images/my",myImg])
    mpimg.imsave(file_out,result)

def process_image(image):
    # NOTE: The output you return should be a color image (3 channel) for processing video below
    # TODO: put your pipeline here,
    # you should return the final output (image with lines are drawn on lanes)
    result = image_pipeline(image)
    return result

"""

Driving main part comes here ...


"""
