import cv2
import pytesseract

def extract():
    # Read the image using OpenCV
    image = cv2.imread("/home/gabriel/Desktop/python/groceryListProject/GroceryListProj/data/captured_image.jpg")  # Replace "image.png" with the path to your image file
    #cv2.imshow('Loaded Image', image)

    # Convert the image to grayscale (optional but can help with text extraction)
    #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use pytesseract to extract text from the grayscale image
    extracted_text = pytesseract.image_to_string(image, lang='eng')

    # Print the extracted text
    print(extracted_text)

def main():
    extract()

if __name__ == '__main__':
    main()