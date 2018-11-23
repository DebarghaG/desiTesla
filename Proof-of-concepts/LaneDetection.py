def draw_lane_lines(image):
imshape = image.shape

    # Greyscale image
    greyscaled_image = grayscale(image)

    # Gaussian Blur
    blurred_grey_image = gaussian_blur(greyscaled_image, 5)

    # Canny edge detection
    edges_image = canny(blurred_grey_image, 50, 150)

    # Mask edges image
    border = 0
    vertices = np.array([[(0,imshape[0]),(465, 320), (475, 320),
    (imshape[1],imshape[0])]], dtype=np.int32)
    edges_image_with_mask = region_of_interest(edges_image,
    vertices)

    # Hough lines
    rho = 2
    theta = np.pi/180
    threshold = 45
    min_line_len = 40
    max_line_gap = 100
    lines_image = hough_lines(edges_image_with_mask, rho, theta,
    threshold, min_line_len, max_line_gap)

    # Convert Hough from single channel to RGB to prep for weighted
    hough_rgb_image = cv2.cvtColor(lines_image, cv2.COLOR_GRAY2BGR)

    # Combine lines image with original image
    final_image = weighted_img(hough_rgb_image, image)

    return final_image
