# Copyright (C) 2024 Coder.AN
# Email: an.hongjun@foxmail.com
# Page: www.anhongjun.top

import os
import sys
import cv2
import numpy as np

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "lib"))
import _picsocket


class ImgSender:
    def __init__(self, ip, port):
        self.sender = _picsocket.ImgSender(ip, port)
    
    def send(self, img):
        img_encode = cv2.imencode(".jpg", img)[1]
        img_list = img_encode.tolist()
        self.sender.send(img_list, len(img_list))


class ImgReceiver:
    def __init__(self, port):
        self.receiver = _picsocket.ImgReceiver(port)
    
    def read(self):
        img_list = self.receiver.read()
        image = np.asarray(bytearray(img_list))
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image
