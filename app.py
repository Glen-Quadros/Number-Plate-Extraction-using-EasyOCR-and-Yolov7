import streamlit as st
import numpy as np
import cv2
import easyocr
from PIL import Image
import imutils

# Load EasyOCR reader
reader = easyocr.Reader(['en'])

def process_image(image):
    # Convert to grayscale
    greyscale_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply bilateral filter
    bfilter = cv2.bilateralFilter(greyscale_img, 11, 17, 17)
    
    # Apply Canny edge detection
    edged = cv2.Canny(bfilter, 30, 30)
    
    # Find contours
    keypoints = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(keypoints)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    
    location = None
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 10, True)
        if len(approx) == 4:
            location = approx
            break
    
    # Create mask
    mask = np.zeros(greyscale_img.shape, np.uint8)
    new_image = cv2.drawContours(mask, [location], 0, 255, -1)
    new_image = cv2.bitwise_and(image, image, mask=mask)
    
    # Crop image
    (x, y) = np.where(mask == 255)
    (x1, y1) = (np.min(x), np.min(y))
    (x2, y2) = (np.max(x), np.max(y))
    cropped_image = greyscale_img[x1:x2+1, y1:y2+1]
    
    return cropped_image

def main():
    st.title("Number Plate Extraction using EasyOCR")
    
    # File upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Read the image file
        image = np.array(Image.open(uploaded_file))
        
        # Process the image
        cropped_image = process_image(image)
        
        # Display the cropped image
        st.write('Uploaded Image: ')
        st.image(uploaded_file, caption="Cropped Image", use_column_width=True)
        
        # Read the text using EasyOCR
        result = reader.readtext(cropped_image)
        
        if result:
            number_plate = result[0][1]
            st.header("Number Plate:")
            st.write(number_plate)
        else:
            st.warning("No number plate detected in the image.")

if __name__ == "__main__":
    main()
