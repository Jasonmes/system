# ubuntu Nvidia显卡安装失败的问题

step 1 ，禁用nouveau，没有gedit的安装一下；

> sudo gedit /etc/modprobe.d/blacklist.conf

将下面内容加入其中，保存关闭；

> blacklist nouveau
> options nouveau modeset=0

然后输入下面命令，重启系统；

> sudo update-initramfs -u
> sudo reboot

重启后，使用下面命令，确保没有输出信息；

> lsmod | grep nouveau

step 2，完全卸载之前安装的显卡驱动；

> sudo apt-get remove --purge nvidia*

然后到nvidia官网或者软件更新驱动那里查到你的显卡适应的版本号；如470，495..



> sudo add-apt-repository ppa:graphics-drivers/ppa
> sudo apt-get update
>
> sudo ubuntu-drivers devices
>
> sudo apt-get install nvidia-driver-470 #此处数字要对应上版本号
> sudo apt-get install mesa-common-dev

# 注意，接下来要重启了，但是重点来了，

如果前面没有禁用secure boot，则在安装过程中会提示设置一个密码，在重启时需要输入密码验证以禁用secure boot，重启后会出现蓝屏，**这时候不能直接选择continue,而应该按下按键，选择Enroll MOK,** **确认后在下一个选项中选择continue,**

接着输入安装驱动时设置的密码，开机；

> sudo reboot

来吧，小宝贝!

> nvidia-smi



1. **验证安装**： 一旦你的系统重新启动，你可以使用以下命令验证NVIDIA驱动程序是否正确安装：

   ```
   nvidia-smi
   ```

这些步骤应该帮助你在Ubuntu 20.04上成功安装NVIDIA驱动程序。但请注意，不同的硬件和系统配置可能需要不同的处理方式，因此始终建议在更改系统配置之前进行备份。



## 查看pci接口

```
lspci

lspci |grep NVIDIA



sudo ubuntu-drivers devices
```

