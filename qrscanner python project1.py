import cv2
from pyzbar.pyzbar import decode
import time

##create a variable to ask the opencv module to make the video capture function works for us
cam = cv2.VideoCapture(0)

## now we will set the window this is the window that would be reflected when we just make our camera = True, that is camera always defaulted as False, we have to make it true to get it pop it on your windows screen for that we set the size

cam.set(5, 640) ## width, 640 is pixel
cam.set(6, 480) ## highet,480 is pixel

## we need to make the camera = True

camera = True

while camera == True: ## if it is true then we will read the QR code scanner we will show in our front camera, so that we will write the command when camera == true is when the camera is open
    suceess, frame = cam.read() ## it will read the frame that would be shown into our camera, suceess is it will return the boolean value that is one or zero and frame is it would read the frame as captured by a front camera and decode it 

## to decode it we will run a loop

    for i in decode(frame): ## that is the frame it will caputured by our camera
        print(i.type) ## type is which type it is that is QR code or barcode or any other code, so it just capture the frame and it will return or print it as which type it is
        print(i.data.decode('utf-8')) ## it will print what we will decode from the QR code, data will store the data in it, and we using the function decode() and the memory we would be using utf-8

## after we write the frame we recorded it to sleep for some time for that we just import the time module
        time.sleep(6) ## make this sleep for 6 seconds

## we want make or show the camera on a window it should be popped up and we should be able to see it, for that we use the opencv module
        cv2.imshow("OurQr_code_scanner",frame) ## we will name the camera window with our QR code scanner we can name it anything as you want and the pass Frame
        cv2.waitKey(3) ## this would be used to capture the frame after 3 seconds