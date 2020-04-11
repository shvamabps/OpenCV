import cv2
import numpy as np
import requests


url = "http://100.90.28.66:8080/shot.jpg"

while True:
    img_resp = requests.get(url)

    img_array = np.array(bytearray(img_resp.content), dtype=np.uint8)

    img = cv2.imdecode(img_array, -1)

    cv2.imshow("IP Camera", img)

    if cv2.waitKey(1) == 27:
        break

