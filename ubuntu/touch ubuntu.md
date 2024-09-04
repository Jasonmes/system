## 小米Ubuntu Touch

1.开机后链接电脑，使用adb shell，登陆
2.执行 sudo su ,切换到root
3.mount -o remount,  rw /  重新挂载根文件系统
4.修改 etc/ssh/sshd_config 配置
5./etc/init.d/ssh start 
6.使用ssh 登陆

密码：0000