from datetime import datetime 
import cv2, time
import numpy as np
import simpleaudio as sa


# Code from https://software.intel.com/en-us/node/754940
def main():
    sdThresh = 10
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.namedWindow('frame')
    cv2.namedWindow('dist')
    cap = cv2.VideoCapture(0)
    _, frame1 = cap.read()
    _, frame2 = cap.read()
    facecount = 0

    wave_obj = sa.WaveObject.from_wave_file("audio/alarm.wav")
    play_obj = None

    while(True):
        _, frame3 = cap.read()
        rows, cols, _ = np.shape(frame3)
        cv2.imshow('dist', frame3)
        dist = distMap(frame1, frame3)

        frame1 = frame2
        frame2 = frame3

        mod = cv2.GaussianBlur(dist, (9, 9), 0)
        _, thresh = cv2.threshold(mod, 100, 255, 0)
        _, stDev = cv2.meanStdDev(mod)

        cv2.imshow('dist', mod)
        if stDev > sdThresh:
            print("Motion")
            if play_obj == None or not play_obj.is_playing():
                play_obj = wave_obj.play()

        cv2.imshow('frame', frame2)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

def distMap(frame1, frame2):
    """outputs pythagorean distance between two frames"""
    frame1_32 = np.float32(frame1)
    frame2_32 = np.float32(frame2)
    diff32 = frame1_32 - frame2_32
    norm32 = np.sqrt(diff32[:, :, 0]**2 + diff32[:, :, 1] **
                     2 + diff32[:, :, 2]**2)/np.sqrt(255**2 + 255**2 + 255**2)
    dist = np.uint8(norm32*255)
    return dist

