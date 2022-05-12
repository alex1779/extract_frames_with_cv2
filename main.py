# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 21:05:28 2021

@author: Ale
"""
import cv2
from utils import listFiles, getBaseName, create_folder


def main():
    files = listFiles('data')
    
    if files == []:
        print('Folder *data* is empty, please load video file first!')
        exit()
    else:
    
        for file in files:
            
            basename = getBaseName(file)
            print('Extracting frames of video:', basename)
            create_folder('out/' + basename)
            cap = cv2.VideoCapture('data/' + file)
            count = 0
            while True:
                ret, img = cap.read()
                if ret is True:
                    cv2.imwrite('out/' + basename + '/' + str(count)+".jpg", img)
                    count += 1
                else:
                    cap.release()
                    break
            print(str(count) + ' frames extracted in folder *data/' + basename + '*')
        print('Done.')
    

if __name__ == "__main__":
    main()