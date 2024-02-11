# PicSocket：轻量级局域网跨平台图传

### 1.特性
* 底层基于UDP协议，图传实时性强。
* 可用于高清数字图传（测试可支持1080P）。
* 可用于局域网wifi无线图传。
* 跨平台，支持Windows，Linux及MacOS。
* 跨语言，支持C/C++，Python。

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
```sh
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
    |- example  # 一个简易的demo
```

将`include`文件夹和`lib`文件夹拷贝到你自己的工程中即可使用。为了演示使用方法，我们假设`example`就是您的工程目录。

在您的工程目录下创建源码文件，如[picsocket_sender.cpp](./example/picsocket_sender.cpp)、[picsocket_receiver.cpp](./example/picsocket_receiver.cpp)。创建CMake文件，如[CMakeLists.txt](./example/CMakeLists.txt)。

随后编译您的工程。

```sh
cd install/example # 进入您的工程目录
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

