import cv2


img = cv2.imread("solar-system.jpg")


font = cv2.FONT_HERSHEY_COMPLEX
font_scale = 0.5


cv2.putText(img, "Sun", (30, 300), font, font_scale, (255, 255, 255))        
cv2.putText(img, "Mercury", (130, 300), font, font_scale, (183, 184, 185))  
cv2.putText(img, "Venus", (230, 300), font, font_scale, (57, 52, 56))       
cv2.putText(img, "Earth", (340, 300), font, font_scale, (64, 40, 24))       
cv2.putText(img, "Mars", (450, 300), font, font_scale, (246, 241, 213))    
cv2.putText(img, "Jupiter", (580, 300), font, font_scale, (186, 172, 177))  
cv2.putText(img, "Saturn", (740, 300), font, font_scale, (206, 184, 184))  
cv2.putText(img, "Uranus", (860, 300), font, font_scale, (172, 229, 238))   
cv2.putText(img, "Neptune", (980, 300), font, font_scale, (120, 192, 168)) 


cv2.imwrite("Solar_systemwithname.jpg", img)


cv2.imshow("output", img)
cv2.waitKey(0)  

