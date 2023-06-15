import cv2
import os
import time

inicio = time.time()
for img in os.listdir():
    
    path = r'Path to your Images'
    os.chdir(path)
    
    if "jpg" in img:
        #print(img)
        
        imagem = cv2.imread(img)
        
        #img = img[:-3] + 'png'
        print(img)
        
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = classificador.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        #cv2.imshow("Faces detectadas", imagem)
        
        path = r'Path to the Result folder'
        os.chdir(path)
        
        status = cv2.imwrite(img, imagem)
        
        print(path)
        
        if status:
            print("Image saved successfully.")
        else:
            print("The image saving failed.")
        cv2.waitKey(0)
        #time.sleep(5)
        
cv2.destroyAllWindows()

fim = time.time()       