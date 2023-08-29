from PIL import Image
import time
import os
import cv2


ASCII_CHARS = "@B%8WM#*oahkbdpwmZO0QCJYXzcvnxrjft/\|()1{}[]-_+~<>i!lI;:, "


# Image resizing
def resize(image, new_width=412):
    (width, height) = image.size
    radio = height / width
    new_height = int(radio * new_width * 0.35)
    new_image = image.resize((new_width, new_height))
    return new_image

# Conversion to grayscale
def grayify(image):
    return image.convert("L")
    

# Mapping pixels to ASCII characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    char ="".join([ASCII_CHARS[pixel//5] for pixel in pixels])
    return char
  

# Creating a frame in Ascii
def convert_to_ascii(image, new_width=412):
    new_image_data = pixels_to_ascii(grayify(resize(image)))
    pixel_count = len(new_image_data)
    result = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixel_count, new_width))
    return result

# Checking if the path to the image is correct
def convert_img_to_ascii(image_path):
    try:
        image = Image.open(image_path) 
        image = convert_to_ascii(image)
        print(image)
    except: 
        return "Invalid path"

def play_ascii_animation(frames, delay=0.1):
    for frame in frames:
        print(frame)
        time.sleep(delay)   

# Creating video in ascii
def generate_ascii_video(video_path):
    cap = cv2.VideoCapture(video_path)
    ascii_frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        pil_frame = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        ascii_frame = convert_to_ascii(pil_frame, new_width=412)
        ascii_frames.append(ascii_frame)

    play_ascii_animation(ascii_frames) 
    cap.release()


print("1: Image to Ascii \n2: Video to Ascii")
choice = input("Enter your choice: ")
path = input("\nEnter the file: ")

if choice == '1':
    convert_img_to_ascii(path)
elif choice == '2': 
    generate_ascii_video(path)
else: 
    print("Bad choice!")