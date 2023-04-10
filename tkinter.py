import cv2
import tkinter as tk

# Initialize the video capturing device
cap = cv2.VideoCapture(0)

# Create a Tkinter window and add a slider widget to it
root = tk.Tk()
root.geometry("300x100")
root.title("Exposure Slider")
slider = tk.Scale(root, from_=0, to=500, orient=tk.HORIZONTAL)
slider.set(50)
slider.pack()

# Define a function to update the exposure time based on the slider value
def update_exposure(val):
    exposure_time = int(slider.get())
    cap.set(cv2.CAP_PROP_EXPOSURE, exposure_time)
    print(cap.get(cv2.CAP_PROP_EXPOSURE))

# Attach the update_exposure function to the slider's 'command' event
slider.config(command=update_exposure)

# Define a function to show the current frame in the window
def show_frame():
    # Read a frame from the camera
    ret, frame = cap.read()
    
    # Check if the frame was successfully read
    if not ret:
        return
    
    # Display the frame in a window
    cv2.imshow('Frame', frame)
    
    # Call this function again after a delay to create a loop
    root.after(1, show_frame)

# Call the show_frame function to start the loop
root.after(1, show_frame)

# Start the mainloop of the window
root.mainloop()

# Release the video capturing device and destroy the window
cap.release()
cv2.destroyAllWindows()
