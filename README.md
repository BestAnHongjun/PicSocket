# PicSocket：轻量级局域网跨平台图传

<div align="center">
<img src="./attach/logo.jpg" width="500px">
</div>

### 1.特性
* 底层基于UDP协议，图传实时性强。
* 可用于高清数字图传（测试可支持1080P，100Mbps局域网下可达100+FPS）。
* 可用于局域网wifi无线图传。
* 跨平台，支持Windows，Linux，MacOS，Jetson，树莓派等。
* 跨语言，支持C/C++，Python。***跨平台使用时支持不同终端运行不同语言***。

### 2.快速开始

<details>
<summary>C/C++快速开始</summary>

#### (1)安装依赖项：
请确保您的机器已安装CMake及C/C++编译器工具链。

安装OpenCV库：
> Jetson平台
```sh
# Jetson平台JetPack已预装OpenCV库，无需操作。
```

> Ubuntu/树莓派/香橙派
```sh
sudo apt-get install libopencv-dev
```

> MacOS
```sh
brew install opencv
```
#### (2)编译安装
克隆本仓库。
```sh
cd ~
git clone https://github.com/BestAnHongjun/PicSocket.git
```

编译并安装。

```sh
cd ~/PicSocket
mkdir build
cd build
cmake ..
make -j4
make install # 不会安装到系统目录，安装到项目的install目录
```

编译安装结束后，项目目录项生成`install`目录。
```sh
|-install
    |- include  # C/C++头文件
    |- lib      # 链接库
    |- cpp      # 一个简易的demo
```

将`include`文件夹和`lib`文件夹拷贝到你自己的工程中即可使用。

#### (3)在自定义工程中使用`PicSocket`

为了演示使用方法，我们假设`cpp`就是您的工程目录。

在您的工程目录下创建源码文件，如[picsocket_sender.cpp](./example/cpp/picsocket_sender.cpp)、[picsocket_receiver.cpp](./example/cpp/picsocket_receiver.cpp)。创建CMake文件，如[CMakeLists.txt](./example/cpp/CMakeLists.txt)。

随后编译您的工程。

```sh
cd ~/PicSocket/install/cpp # 进入您的工程目录
mkdir build     # 创建编译目录
cd build
cmake ..
make -j4
```

随后，在您的编译目录下可以看到二进制文件`picsocket_sender`及`picsocket_receiver`。运行他们即可。

> **注意**：运行本demo时，请确保您的发送端设备安装有摄像头，并可由`cv::VideoCapture(0)`正常读取。

```sh
# 由8888端口接受图片流
./picsocket_receiver 8888

# 向127.0.0.0:8888发送图片流
./picsocket_sender 127.0.0.1 8888
```

</details>

<details>
<summary>Python快速开始</summary>

#### (1)安装依赖项：
请确保您的机器已安装CMake及C/C++编译器工具链。

安装OpenCV库：
> Jetson平台
```sh
# Jetson平台JetPack已预装OpenCV库，无需操作。
```

> Ubuntu/树莓派/香橙派
```sh
sudo apt-get install libopencv-dev
```

> MacOS
```sh
brew install opencv
```
#### (2)编译安装
克隆本仓库。
```sh
cd ~
git clone https://github.com/BestAnHongjun/PicSocket.git
```

编译并安装。

```sh
cd ~/PicSocket
mkdir build
cd build
cmake .. -DPYTHON_BUILD=TRUE
make -j4
```

安装Python模块。

```sh
cd ~/PicSocket
pip3 install -e .
```

#### (3)在自定义工程中使用`PicSocket`

作为一个简单示例，您可以复制并创建[picsocket_sender.py](./example/python/picsocket_sender.py)、[picsocket_receiver.py](./example/python/picsocket_receiver.py)，并运行他们。

> **注意**：运行本demo时，请确保您的发送端设备安装有摄像头，并可由`cv2.VideoCapture(0)`正常读取。

```sh
# 由8888端口接受图片流
python3 picsocket_receiver 8888

# 向127.0.0.0:8888发送图片流
python3 picsocket_sender 127.0.0.1 8888
```

</details>

### 3.简明教程

#### (1)C/C++简明教程
* 发送端
```cpp
// 0.引入头文件
#include "pic_socket.h" 

int main()
{
    // 1.OpenCV读取摄像头
    cv::VideoCapture capture(0);

    // 2.创建发送端实例，目标IP地址127.0.0.1，目标端口8888
    UDPImgSender img_sender("127.0.0.1", 8888);

    while (true)
    {
        // 3.读取OpenCV-Mat
        cv::Mat frame;
        capture >> frame;

        // 4.发送一帧
        img_sender.send(frame);

        // 5.可视化当前帧
        cv::imshow("sender", frame);
        cv::waitKey(30);
    }
    
    // 6.结束程序
    return 0;
}
```

* 接收端
```cpp
// 0.引入头文件
#include "pic_socket.h"

int main()
{
    // 1.创建接收端实例，接收端口8888
    UDPImgReceiver img_receiver(8888);

    while (true)
	{
		// 2.读取一帧
        cv::Mat frame = img_receiver.read();

        // 3.可视化当前帧
		cv::imshow("receiver", frame);
		cv::waitKey(30);
	}

    // 4.退出程序
	return 0;
 }
```

#### (1)Python简明教程
* 发送端

```py
import cv2
# 0.引入picsocket库
import picsocket


if __name__ == "__main__":
    # 1.创建发送端实例，目标IP地址127.0.0.1，目标端口8888
    img_sender = picsocket.ImgSender("127.0.0.1", 8888)

    cap = cv2.VideoCapture(0)
    while True:
        # 2.读取OpenCV-Mat
        ret, img = cap.read()
        
        # 3.发送一帧
        img_sender.send(img)
```

* 接收端

```py
import cv2
# 0.引入picsocket库
import picsocket


if __name__ == "__main__":
    # 1.创建接收端实例，监听端口8888
    img_receiver = picsocket.ImgReceiver(8888)

    while True:
        # 2.读取一帧
        img = img_receiver.read()

        # 3.可视化当前帧
        cv2.imshow("receiver", img)
        cv2.waitKey(5)

```
