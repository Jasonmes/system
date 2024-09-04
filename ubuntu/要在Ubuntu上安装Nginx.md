要在Ubuntu上安装Nginx，你可以使用`apt`包管理器。下面是详细的步骤：

1. **更新软件包列表**

   首先，确保你的Ubuntu系统的软件包列表是最新的。

   ```
   sudo apt update
   ```

2. **安装Nginx**

   使用以下命令来安装Nginx。

   ```
   sudo apt install nginx
   ```

3. **启动Nginx**

   安装完成后，你可以使用以下命令来启动Nginx。

   ```
   sudo systemctl start nginx
   ```

4. **开启启动时自动运行**

   要确保每次系统启动时Nginx都会自动运行，使用以下命令：

   ```
   sudo systemctl enable nginx
   ```

5. **验证Nginx安装**

   打开你的Web浏览器，然后输入你的服务器的IP地址或域名。你应该会看到Nginx的默认欢迎页面，这表明Nginx已经成功安装并正在运行。

6. **防火墙配置**

   如果你启用了`ufw`防火墙，你可能需要允许HTTP和HTTPS流量。可以使用以下命令来完成：

   ```
   sudo ufw allow 'Nginx Full'
   ```

7. **停止、启动或重启Nginx**

   如果你需要停止、启动或重启Nginx，你可以使用以下命令：

   ```
   sudo systemctl stop nginx      # 停止Nginx
   sudo systemctl start nginx     # 启动Nginx
   
   # 重启Nginx
   ```

8. **查看Nginx状态**

   要查看Nginx的运行状态，可以使用：

   ```
   sudo systemctl status nginx
   ```

这些是安装和管理Ubuntu上Nginx的基本步骤。之后，你可能还需要进一步配置Nginx，例如设置虚拟主机、安装SSL证书等，但上述步骤应该为你提供了一个正在运行的Nginx实例。