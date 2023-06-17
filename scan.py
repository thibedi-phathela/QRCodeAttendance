import cv2
import mysql.connector

cap = cv2.VideoCapture(0) 
detector = cv2.QRCodeDetector()

while True:

    _, img = cap.read()
    data, bbox, _ = detector.detectAndDecode(img)
    if (data):

        info = data
        break

    cv2.imshow("Scan QR", img)
    
    if (cv2.waitKey(1) == ord("q")): 
        break

decode = info.split("-")

#Accessing database
db = mysql.connector.connect(user ='root', password ='', host ='localhost', database ='attendance')
cursor = db.cursor()

query = 'INSERT INTO attendance_register (firstName,lastName,id) VALUES (%s, %s, %s)'
values = (decode[0],decode[1],decode[2])
cursor.execute(query,values)
db.commit()
db.close()

print("Attendance Recorded")

#release cam       
cap.release()
cv2.destroyAllWindows()

    
