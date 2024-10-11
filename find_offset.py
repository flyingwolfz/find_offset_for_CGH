import cv2
import numpy as np
import keyboard


image_path = 'out/r.png'
image = cv2.imread(image_path)
if image is None:
    print("Failed to load image.")
    exit()
image = cv2.resize(image, (1280,720))  # important: integer scaling or no scaling


window_name = 'Image'

cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.moveWindow(window_name, 5, 5)
cv2.resizeWindow(window_name, 1280,720)

cv2.imshow('Image', image)
cv2.waitKey(1)

def adjust_image_brightness(image, value):

    adj_image=(image+value)%255
    #image = np.clip(image + value, 0, 255).astype(np.uint8)
    return adj_image


adjustment_step = 5

print("Press 'a' to decrease brightness, 'd' to increase brightness, 'q' to quit.")

brightness_value = 0

while True:
    if keyboard.is_pressed('a'):
        brightness_value -= adjustment_step
        adjusted_image = adjust_image_brightness(image, brightness_value)
        cv2.imshow('Image', adjusted_image)
        print(f"Current brightness adjustment: {brightness_value}")
        cv2.waitKey(200)
    elif keyboard.is_pressed('d'):
        brightness_value += adjustment_step
        adjusted_image = adjust_image_brightness(image, brightness_value)
        cv2.imshow('Image', adjusted_image)
        print(f"Current brightness adjustment: {brightness_value}")
        cv2.waitKey(200)
    elif keyboard.is_pressed('q'):
        break

cv2.destroyAllWindows()
