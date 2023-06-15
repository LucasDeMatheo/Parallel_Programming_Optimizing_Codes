import cv2
import os
import time
from joblib import Parallel, delayed

def reconhecer_face(img):    
    if "jpg" in img:
        
        path = r'Path to your Images'
        os.chdir(path)
               
        imagem = cv2.imread(img)
        
        img = img[:-3] + 'png'
        print(img)
        
        cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
        classificador = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = classificador.detectMultiScale(cinza, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        for (x, y, w, h) in faces:
            cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        path = r'Path to the Result folder'
        os.chdir(path)

        status = cv2.imwrite(img, imagem)

        print(path)

        if status:
            print("Image saved successfully.")
        else:
            print(""The image saving failed.")
    
    return 
	

tempo_inicial = time.time()

path = r'C:\Users\lucas\OneDrive\Documents\UVA\11º Período\Programacao Paralela\A1\Algoritmo\Imagens'
os.chdir(path)
arquivos = os.listdir()
arquivos.pop()

Parallel(n_jobs=4)(delayed(reconhecer_face)(arquivo) for arquivo in arquivos)

print(f"Demorou: {time.time() - tempo_inicial}")