# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top

import sys
import cv2
import picsocket


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <listen-port>".format(sys.argv[0]))
    img_receiver = picsocket.ImgReceiver(int(sys.argv[1]))

    while True:
        img = img_receiver.read()
        cv2.imshow("receiver", img)
        cv2.waitKey(5)
