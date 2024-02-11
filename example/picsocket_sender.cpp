/*
 * Copyright (C) 2024 Coder.AN
 * Email: an.hongjun@foxmail.com
 * Page: www.anhongjun.top
 */
 #include <cstdlib>
 #include <cstdio>
 #include "pic_socket.h"

 int main(int argc, char* argv[])
 {
    if (argc != 3){
        printf("Usage: %s <target-ip> <target-port>\n", argv[0]);
        return -1;
    }
    
    cv::VideoCapture capture(0);
    UDPImgSender img_sender(argv[1], atoi(argv[2]));

    while (true)
	{
		cv::Mat frame;
		capture >> frame;
        img_sender.send(frame);
		cv::imshow("sender", frame);
		cv::waitKey(30);
	}
	return 0;
 }