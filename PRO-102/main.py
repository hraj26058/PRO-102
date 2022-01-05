import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
	number=random.randint(0,1000)
	videoCaptureObject = cv2.VideoCapture(0)
	result=True
	while (result):
		ret, frame=videoCaptureObject.read()
		image_name="img"+str(number)+".png"
		cv2.imwrite(image_name,frame)
		start_time=time.time()
		result=False
	return image_name
	print("Snapshot Taken")

	videoCaptureObject.release()
	cv2.destroyAllWindows()

def upload_file(image_name):
	access_token='bssSOBkyHBwAAAAAAAAAASpb3GFxjNCNrfYkPOC5Qnu0U6cylN7sFa74XyKPsUdd'
	file=image_name
	file_from=file
	file_to="/PRO-102/" + image_name
	dbx=dropbox.Dropbox(access_token)

	with open(file_from,'rb') as f:
		dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
		print("File Uploaded")

def main():
	while(True):
		if((time.time()-start_time) >= 3):
			name = take_snapshot()
			upload_file(name)

main()

