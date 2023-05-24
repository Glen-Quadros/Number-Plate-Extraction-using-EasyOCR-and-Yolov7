# Number-Plate-Extraction-using-EasyOCR

In this computer vision project, I focus on detecting and printing the number plate of a car from images provided by the user. I use various python libraries such as OpenCV for image processing, easyOCR for text recognition, and imutils for contour detection.

To begin, I convert the image to greyscale since the Canny algorithm, which is used for edge detection, requires a grayscale image as the input. I then apply fundamental image processing techniques like noise reduction using a bilateral filter and edge detection using the Canny algorithm. By detecting and sorting the contours in descending order, I can pinpoint the relevant areas of the image.

In order to identify the number plate, I employ the Douglas-Peucker algorithm in a loop to find a polygon with four edges. This algorithm helps me approximate the shape of the number plate accurately. By applying a mask, I can isolate the number plate region, discarding any unnecessary information from the rest of the image.

Once the number plate is extracted, I utilize easyOCR to read the text on the plate. This library makes it easy to recognize characters and convert them into readable text. Finally, I display the output, which includes the detected text from the number plate, to the user.

I have built the web application for this project using Streamlit Python library. The user uploads an image as the input and in the backend, image processing is done and then the number plate of the car in text format is given as the output.

<img width="1440" alt="Screenshot 2023-05-24 at 14 18 28" src="https://github.com/Glen-Quadros/Number-Plate-Recognition-using-EasyOCR/assets/106950467/e7d64599-aea0-4bfa-8360-26a0da993f68">

<img width="1440" alt="Screenshot 2023-05-24 at 14 20 53" src="https://github.com/Glen-Quadros/Number-Plate-Recognition-using-EasyOCR/assets/106950467/b172d597-cb28-40a4-83cf-e1dc88a3f026">
