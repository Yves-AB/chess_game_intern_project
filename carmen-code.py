import cv2
import numpy as np

# Read the image
image = cv2.imread("C:/Users/Carmen/Desktop/internship/002.png")

# Check if the image was successfully read
if image is not None:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply adaptive thresholding to obtain a binary image
    _, binary_image = cv2.threshold(grayscale_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Perform Harris corner detection
    corners = cv2.cornerHarris(binary_image, 2, 3, 0.04)

    # Refine corner locations by applying a dilation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    corners = cv2.dilate(corners, kernel)

    # Threshold the corner response
    threshold = 0.01 * corners.max()
    corner_mask = corners > threshold

    # Find centroids of the detected corners
    contours, _ = cv2.findContours(corner_mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    centroids = []
    for contour in contours:
        moments = cv2.moments(contour)
        centroid_x = int(moments["m10"] / moments["m00"])
        centroid_y = int(moments["m01"] / moments["m00"])
        centroids.append((centroid_x, centroid_y))

    # Sort centroids based on the y-coordinate (row) first, then the x-coordinate (column)
    centroids.sort(key=lambda c: (c[1], c[0]))

    # Define the matrix to store square color values
    matrix = np.zeros((len(centroids),), dtype=int)

    # Calculate the number of squares in each row and column
    num_squares_row = 933 // 157
    num_squares_col = 961 // 157

    # Iterate over the centroids and classify squares based on color
    for i, centroid in enumerate(centroids):
        # Calculate the row and column index of the square
        row_index = i // num_squares_col
        col_index = i % num_squares_col

        # Calculate the position of the square in the image
        x = col_index * 157
        y = row_index * 157

        # Extract the square region from the image
        square = image[y:y+157, x:x+157]

        # Calculate the average color of the square
        average_color = np.mean(square, axis=(0, 1))

        if average_color[2] > average_color[1] and average_color[2] > average_color[0]:  # Red square
            matrix[i] = 0
        elif average_color[1] > average_color[2] and average_color[1] > average_color[0]:  # Green square
            matrix[i] = 1

    for i in range(len(matrix)):
        print(matrix[i], end=" ")
        if (i + 1) % 6 == 0:
            print()
            if (i + 1) // 6 == 6:
                break

    # Display the original image with detected squares
    for centroid in centroids:
        cv2.circle(image, centroid, 5, (0, 255, 0), 2)
    cv2.imshow('Detected Squares', image)
    cv2.waitKey(0)  # Wait for a key press
    cv2.destroyAllWindows()  # Close the window
else:
    print('Failed to read the image.')