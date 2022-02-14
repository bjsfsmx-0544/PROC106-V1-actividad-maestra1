# Importar la biblioteca OpenCV
import cv2

# Cargar el archivo Clasificador en cascadas
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

# Definir un objeto de captura de video
vid = cv2.VideoCapture(0)

while(True):
   
    # Capturar el video cuadro por cuadro
    ret, frame = vid.read()

    # Convertir a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detectar las caras
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    # Dibujar los rectángulos al rededor de cada cara
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
    # Mostrar el cuadro resultante 
    cv2.imshow('Fotograma', frame)
      
    # Salir de la ventana a través de la barra espaciadora
    if cv2.waitKey(25) == 32:
        break
  
# Después del bucle, liberar el objeto capturado
vid.release()

# Destruir todas las ventanas
cv2.destroyAllWindows()