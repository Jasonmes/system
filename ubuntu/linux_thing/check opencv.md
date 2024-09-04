如果要在 NVIDIA Jetson 设备上查看 OpenCV 的版本号，可以使用以下方法：

在终端中输入命令 pkg-config --modversion opencv，可以查看 OpenCV 的版本号。

在终端中输入命令 dpkg -l | grep opencv，可以查看 OpenCV 的安装信息，其中版本号也会显示出来。

在终端中输入命令 dpkg -s opencv，可以查看 OpenCV 软件包的详细信息，其中版本号也会显示出来。

需要注意的是，上述方法只适用于使用 dpkg 包管理器安装的 OpenCV，如果使用其他方式安装的 OpenCV，可能需要使用不同的方法来查看版本号。