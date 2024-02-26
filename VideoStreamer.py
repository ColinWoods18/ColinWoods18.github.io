import cv2
from flask import Flask, render_template

app = Flask(__name__)


@app.route('index.html/')

def home():
    return render_template('index.html')

def vidCap():

    vid = cv2.VideoCapture(0)   # 0 is the default camera

    # Check if the camera is opened successfully
    if not vid.isOpened():
        print("Cannot open camera")
        exit()

    while(True): 
        
        # Capture the video frame by frame 
        ret, frame = vid.read() 
    
        # Display the resulting frame 
        cv2.imshow('frame', frame) 
        
        # Set it so you can to press q to quit the window 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    
    # After the loop release the cap object 
    vid.release() 
    # Destroy all the windows 
    cv2.destroyAllWindows() 

if __name__ == '__main__':
    app.run(debug=True)
    vidCap()