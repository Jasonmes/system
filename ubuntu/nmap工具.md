在Mac下，你可以使用类似的步骤来搜索连接了WiFi的设备的IP地址。以下是具体步骤：

1. **安装nmap工具**： 如果你还没有安装`nmap`，可以使用Homebrew进行安装。首先，确保你已经安装了Homebrew。如果没有安装，可以参考[Homebrew的安装指南](https://brew.sh/)。

   安装Homebrew后，使用以下命令安装`nmap`：

   ```
   brew install nmap
   ```

2. **获取你的网络子网**： 你需要知道你的网络子网地址。可以使用以下命令查看：

   ```
   ifconfig
   ```

   找到与你的无线网络接口（通常是`en0`）相关的IP地址。例如，如果你的IP地址是`192.168.1.5`，子网通常是`192.168.1.0/24`。

3. **扫描网络中的设备**： 使用`nmap`扫描网络中的设备。假设你的子网是`192.168.1.0/24`，你可以运行以下命令：

   ```
   sudo nmap -sn 192.168.1.0/24
   ```

   你可能需要输入你的密码来授权`sudo`命令。

4. **查看结果**： 扫描完成后，你将看到类似于以下的输出：

   ```
   Starting Nmap 7.80 ( https://nmap.org ) at 2024-06-17 14:00 UTC
   Nmap scan report for 192.168.1.1
   Host is up (0.0040s latency).
   Nmap scan report for 192.168.1.2
   Host is up (0.0030s latency).
   Nmap scan report for 192.168.1.5
   Host is up (0.00050s latency).
   Nmap scan report for 192.168.1.10
   Host is up (0.0050s latency).
   ```

   这些IP地址就是当前连接到你的WiFi网络的设备。