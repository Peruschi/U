import cv2

# 載入分類器
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascade_eye.xml')

# 從視訊鏡頭擷取影片. 
#cap = cv2.VideoCapture(0)
# 使用現有影片
cap = cv2.VideoCapture('test.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # 轉成灰階
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 偵測臉部
    faces = face_cascade.detectMultiScale(gray, 2, 5)

    # 繪製人臉部份的方框
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    cv2.imshow('img', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
