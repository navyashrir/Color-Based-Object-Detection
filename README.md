# Color-Based Object Detection and Counting

## Project Description

This project focuses on detecting and counting objects based on their color using digital image processing techniques.

The system uses Python and OpenCV to convert an input image from BGR color space to HSV color space. HSV color space is used because it makes color-based segmentation easier. A color threshold is applied to identify the required color region and generate a binary mask.

Morphological operations are then applied to remove small noise and improve the detected regions. Contours are detected from the cleaned mask, and valid regions are selected based on their area. Finally, bounding boxes and object numbers are displayed on the detected objects.

## Technologies Used

- Python
- OpenCV
- NumPy
- Matplotlib
- Visual Studio Code

## Methodology

The project follows these steps:

1. Input Image
2. BGR to HSV Conversion
3. Color Thresholding
4. Binary Mask Generation
5. Morphological Operations
6. Contour Detection
7. Area Filtering
8. Bounding Box Detection
9. Object Counting

## Dataset

The dataset used for this project is:

**Fruits Images Dataset - Object Detection**

Kaggle:
https://www.kaggle.com/datasets/afsananadia/fruits-images-dataset-object-detection

The dataset contains fruit images along with annotation files. Selected fruit images were used to test the color-based object detection approach.

## Project Implementation

The current implementation demonstrates orange-colored object detection using an HSV color range.

The system generates:

- Original input image
- Orange color mask
- Cleaned binary mask
- Final detection image with bounding boxes and object count

## Output

The final output shows the detected orange-colored regions with bounding boxes and labels.

The output images are available in this repository.

## Limitations

The accuracy of color-based detection depends on lighting conditions, background colors, and the similarity between the object and its surroundings.

When objects touch or overlap, they may sometimes be detected as a single region.

## Future Enhancement

The project can be improved by using advanced segmentation techniques to separate touching objects and by supporting multiple target colors with better color calibration.

## Author

Navyashri
CSEAIML
2023003780
