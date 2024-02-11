/*
 * Copyright (C) 2024 Coder.AN
 * Email: an.hongjun@foxmail.com
 * Page: www.anhongjun.top
 */

#include <pybind11/operators.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <iostream>

#include "pic_socket.h"
namespace py = pybind11;


class _UDPImgSender{
private:
    UDPImgSender img_sender;
public:
    _UDPImgSender(const char* ip, uint16_t port) : 
        img_sender(ip, port, MODE_JPGBUF){};
    void send(const std::vector<uint8_t> &jpg_buffer, size_t size);
};

class _UDPImgReceiver{
private:
    UDPImgReceiver img_receiver;
public:
    _UDPImgReceiver(uint16_t port) :
        img_receiver(port, MODE_JPGBUF){};
    std::vector<uint8_t> read();
};

void _UDPImgSender::send(const std::vector<uint8_t> &jpg_buffer, size_t size)
{
    uint8_t* buffer = (uint8_t*)&jpg_buffer[0];
    this->img_sender.sendjpg(buffer, size);
    return;
}

std::vector<uint8_t> _UDPImgReceiver::read()
{
    return this->img_receiver.readjpg();
}

PYBIND11_MODULE(_picsocket, m) 
{
    py::class_<_UDPImgSender>(m, "ImgSender")
        .def(py::init<const char*, uint16_t>())
        .def("send", &_UDPImgSender::send);
    
    py::class_<_UDPImgReceiver>(m, "ImgReceiver")
        .def(py::init<uint16_t>())
        .def("read", &_UDPImgReceiver::read);
}
