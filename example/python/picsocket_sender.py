# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top

import sys
import cv2
import picsocket


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: {} <target-ip> <target-port>".format(sys.argv[0]))
    img_sender = picsocket.ImgSender(sys.argv[1], int(sys.argv[2]))

    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if img is None:
            print("Read images error!")
            break
        img_sender.send(img)
