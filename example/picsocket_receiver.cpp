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
    if (argc != 2){
        printf("Usage: %s <listen-port>\n", argv[0]);
        return -1;
    }

    UDPImgReceiver img_receiver(atoi(argv[1]));

    while (true)
	{
		cv::Mat frame = img_receiver.read();
		cv::imshow("receiver", frame);
		cv::waitKey(30);
	}
	return 0;
 }