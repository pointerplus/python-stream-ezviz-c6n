
import cv2

#open up the video stream
cap = cv2.VideoCapture('rtsp:/admin:VERIFICATIONCODE@IPADDRESS/h264_stream')

#Loop to capture frames
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
