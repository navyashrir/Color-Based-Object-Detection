# Import OpenCV for image processing.
import cv2

# Import NumPy for creating arrays and kernels.
import numpy as np

# Import os for handling file paths.
import os


# Specify the input fruit image.
image_path = "dataset/fruits/38_Orange.jpg"

# Specify the folder for saving output images.
output_folder = "outputs"

# Create the output folder if it does not exist.
os.makedirs(output_folder, exist_ok=True)


# Read the input image.
image = cv2.imread(image_path)

# Check whether the image was loaded correctly.
if image is None:
    print("ERROR: Image could not be loaded.")
    exit()

# Convert the image from BGR to HSV color space.
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


# Define the lower HSV limit for orange.
lower_orange = np.array([5, 100, 80])

# Define the upper HSV limit for orange.
upper_orange = np.array([25, 255, 255])


# Create a binary mask for orange-colored regions.
orange_mask = cv2.inRange(
    hsv_image,
    lower_orange,
    upper_orange
)


# Create a 5 x 5 morphological kernel.
kernel = np.ones((5, 5), np.uint8)


# Remove small noise from the mask.
cleaned_mask = cv2.morphologyEx(
    orange_mask,
    cv2.MORPH_OPEN,
    kernel
)

# Fill small gaps inside detected regions.
cleaned_mask = cv2.morphologyEx(
    cleaned_mask,
    cv2.MORPH_CLOSE,
    kernel
)


# Find external contours in the cleaned mask.
contours, hierarchy = cv2.findContours(
    cleaned_mask,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)


# Define the minimum area for a valid fruit region.
MIN_AREA = 800


# Create a list for storing valid contours.
valid_contours = []


# Examine every detected contour.
for contour in contours:

    # Calculate the contour area.
    area = cv2.contourArea(contour)

    # Keep only sufficiently large regions.
    if area >= MIN_AREA:

        # Add the contour to the valid contour list.
        valid_contours.append(contour)


# Count the detected objects.
object_count = len(valid_contours)


# Create a copy of the original image.
result = image.copy()


# Draw bounding boxes around detected objects.
for index, contour in enumerate(valid_contours, start=1):

    # Calculate the bounding rectangle.
    x, y, width, height = cv2.boundingRect(contour)

    # Draw a green bounding rectangle.
    cv2.rectangle(
        result,
        (x, y),
        (x + width, y + height),
        (0, 255, 0),
        2
    )

    # Create a number for the detected object.
    object_label = "Object " + str(index)

    # Write the object number near the bounding box.
    cv2.putText(
        result,
        object_label,
        (x, max(y - 8, 20)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.55,
        (0, 255, 0),
        2
    )


# Create the final object-count text.
count_text = "Orange Objects Detected: " + str(object_count)


# Display the object count on the image.
cv2.putText(
    result,
    count_text,
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2
)


# Save the original image.
cv2.imwrite(
    os.path.join(output_folder, "step10_original.jpg"),
    image
)

# Save the initial orange mask.
cv2.imwrite(
    os.path.join(output_folder, "step10_color_mask.jpg"),
    orange_mask
)

# Save the cleaned mask.
cv2.imwrite(
    os.path.join(output_folder, "step10_cleaned_mask.jpg"),
    cleaned_mask
)

# Save the final detection result.
cv2.imwrite(
    os.path.join(output_folder, "step10_final_result.jpg"),
    result
)


# Print the number of detected contours.
print("Total contours detected:", len(contours))

# Print the number of valid objects.
print("Orange objects detected:", object_count)

# Print a confirmation message.
print("Step 10 completed successfully.")


# Display the final result.
cv2.imshow(
    "Color-Based Object Detection and Counting",
    result
)

# Wait until a key is pressed.
cv2.waitKey(0)

# Close all OpenCV windows.
cv2.destroyAllWindows()