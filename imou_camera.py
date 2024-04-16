import cv2

# Dirección IP de la cámara
ip_camera_address = "rtsp://admin:L2635768@192.168.1.92"

# Capturar el video desde la cámara
cap = cv2.VideoCapture(ip_camera_address)

# Ciclo para mostrar el video en vivo
while True:
    ret, frame = cap.read()
    cv2.imshow('Cámara IP', frame)
    
    # Presiona 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()