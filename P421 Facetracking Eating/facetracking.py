import cv2

#amount of neighbors integer
nose_neighbors = 40
mouth_neighbors = 70
nose_size = 40
mouth_size = 50

#load face recognition model
nose_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_nose.xml")
mouth_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_mcs_mouth.xml")

#ask user what video file they want to use
##video_input = ""
##video_played = False
##while video_played != True:
##        video_input = input("Please type what video file you want to track: \n")
##        if video_input == "quit":
##            exit(0) #successful
##        video_capture = cv2.VideoCapture(video_input)
##        video_played = True

video_capture = cv2.VideoCapture('face_video.mp4')
#identify faces in video and draw box
def detect_bounding_box(vid, neighbors, classifier, size):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = classifier.detectMultiScale(gray_image, 1.1, neighbors, minSize=(size, size)) #size of the min face detection
    for (x,y,w,h) in faces:
        cv2.rectangle(vid,(x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
frame = 0
while True:
    
    #try:
    
    #read a frame of the video
    nose_y, mouth_y = 0, 0
    frame += 1
    result, img = video_capture.read()
    try:
        nose_y = detect_bounding_box(img, nose_neighbors, nose_classifier, nose_size)[0][1]
        mouth_y = detect_bounding_box(img, mouth_neighbors, mouth_classifier, mouth_size)[0][1]
    except:
        print("Lost sight of face features")
    point_distance = str(mouth_y - nose_y)
    print("Distance between = ", point_distance)
    f = open("output.txt", "a")
    file_write_string = "(" + str(frame) + "," + point_distance + ")\n"
    f.write(file_write_string)
    f.close()
        
    #except:
    #    print("An error occured, please make sure that the video name and format is correct eg; \'face_video.mp4\'\n")
    #    video_input = input("Please type what video file you want to track: \n")
    #    if video_input == "quit":
    #        exit(0) #successful
    #    video_capture = cv2.VideoCapture(video_input)
    
    #display frames
    cv2.imshow('img', img)
    #terminate if q is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    
#display video in new screen
video_capture.release()
cv2.destroyAllWindows()
