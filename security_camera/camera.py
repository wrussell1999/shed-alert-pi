import cv2

def main():
    camera = cv2.VideoCapture(0)

    while True:
        ret, frame = camera.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) % 0xFF == ord('q'):
            break
    
    camera.release()
    cv2.destroyAllWindows()
