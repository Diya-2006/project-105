import cv2

vid=cv2.VideoCapture(0)

if(vid.isOpened()==False):
    print("Unable to read the feed")

vid.get()

height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(height)
width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
print(width)
fps=int(vid.get(cv2.CAP_PROP_FPS))
print(fps)

while(True):

    # Capture the video frame 
    # By Frame
    ret,frame=vid.read()
    cv2.destroyAllWindows
    
