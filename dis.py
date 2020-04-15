import math
import cv2
cap = cv2.VideoCapture(0)
face_model = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
font = cv2.FONT_HERSHEY_PLAIN
color_font = [0, 0, 0]
color_rectangle = [255, 255, 255]
org = (30, 35)
thickness = 1
fontScale = 2
line = cv2.LINE_AA
distance = 0


while True:
	status, img = cap.read()
	face_cord  = face_model.detectMultiScale(img)
	number_of_faces = len(face_cord)
	faces = f"Total: {number_of_faces}"
	cv2.putText(img,faces,org,font,fontScale,color_font,thickness,line)
	
	i=0
	if number_of_faces == 0 :
		pass
	else:
		while i < number_of_faces:
			x1 = face_cord[i][0]
			y1 = face_cord[i][1]
			x2 = x1 + face_cord[i][2]
			y2 = y1 + face_cord[i][3]
			cv2.rectangle(img,(x1,y1),(x2,y2),color_rectangle,3)
			i=i+1
		cv2.imshow('Image',img)
		if cv2.waitKey(10) == 27:
			break


cv2.imwrite(f"detected faces {number_of_faces}.jpg", img)
print(f"Number of faces detected: {number_of_faces}")
cv2.destroyAllWindows()
cap.release()




import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = f"Attendance for the session is (number of faces detected): {number_of_faces}"
#The mail addresses and password
sender_address = input("Enter Sender Mail Address: ")
sender_pass = input("Enter Sender Password: ")
receiver_address = input("Enter Receiver Mail Address: ")
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Attendance'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print(f'Mail Sent successfully to {receiver_address}')
