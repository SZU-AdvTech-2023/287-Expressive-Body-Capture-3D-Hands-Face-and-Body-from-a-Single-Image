import json
import numpy as np
import cv2
 

for i in range(10,100):
 
    with open('data/keypoints/%s_img_keypoints.json'%(i), "r") as f:
        data = f.read()
 
    data = json.loads(data)
 
    points = data["shapes"][0]["points"]
    points = np.array(points, dtype=np.int32)
 
    image = cv2.imread('data/keypointsxxx/%s_img.jpg' %(i) ) 
 
    mask = np.zeros_like(image, dtype=np.uint8)
 
    cv2.fillPoly(mask, [points], (255, 255, 255))
 
    cv2.imwrite('output/results/%s.png' %(i), mask) 