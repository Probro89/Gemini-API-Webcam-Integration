import cv2
import time
import threading
import google.generativeai as genai 
from IPython.display import display
import PIL.Image
import os




GOOGLE_API_KEY = "AIzaSyB1afaJnWzMNbw-3adnLAEpDMNuAkpUYY4"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro-vision")


def show_and_capture_webcam(save_path, capture_interval=5):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Webcam Feed', frame)

        if int(time.time()) % capture_interval == 0:
            screenshot_path = f"{save_path}/screenshot.png"
            cv2.imwrite(screenshot_path, frame)
            
            global img
            img = PIL.Image.open("C:\python projects\gemini project\webcam\screenshot.png")
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def user_input_function():
    while True:
        question = input("Enter your Prompt.")
        response = model.generate_content([ question, img])
        resp = response.text 
        print(resp)

if __name__ == '__main__':
    file_path = "C:\python projects\gemini project\webcam"

    # Create a thread for the webcam function
    webcam_thread = threading.Thread(target=show_and_capture_webcam, args=(file_path,))
    webcam_thread.start()

    # Run the user input function in the main thread
    user_input_function()
