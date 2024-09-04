# FRP + Proxyfix



要实现通过 FRP（Fast Reverse Proxy）将外部访问转发到你本机上的 Postfix 邮件服务器，你可以按照以下步骤操作：

1. **安装并配置 Postfix**：

   - 确保 Postfix 已经正确安装和配置好，并且能够在本地正常接收邮件。

   - 例如，你可以使用以下命令安装 Postfix：

     ```
     bash
     复制代码
     sudo apt-get update
     sudo apt-get install postfix
     ```

   - 在安装过程中选择 “Internet Site” 配置，并设置邮件域名。

2. **安装 FRP**：

   - 从 [FRP 官方 GitHub](https://github.com/fatedier/frp/releases) 下载最新的 FRP 客户端和服务器。

   - 解压下载的文件，例如：

     ```
     bash
     复制代码
     tar -zxvf frp_0.37.0_linux_amd64.tar.gz
     ```

   - 将解压后的文件移动到合适的目录，比如 `/usr/local/bin`。

3. **配置 FRP 服务端**：

   - 在外部服务器上，创建 

     ```
     frps.ini
     ```

      文件，并添加以下配置：

     ```
     ini
     复制代码
     [common]
     bind_port = 7000
     ```

   - 启动 FRP 服务端：

     ```
     bash
     复制代码
     ./frps -c frps.ini
     ```

4. **配置 FRP 客户端**：

   - 在本地安装了 Postfix 的机器上，创建 `frpc.ini` 文件，并添加以下配置：

     ```
     ini
     复制代码
     [common]
     server_addr = <外部服务器IP>
     server_port = 7000
     
     [smtp]
     type = tcp
     local_ip = 127.0.0.1
     local_port = 25
     remote_port = 2525
     ```

     在这里，`server_addr` 为你的外部服务器的 IP 地址，`local_ip` 是本地 Postfix 监听的 IP 地址，`local_port` 是 Postfix 监听的端口（通常是 25），`remote_port` 是外部用户访问的端口（你可以自定义，这里示例为 2525）。

   - 启动 FRP 客户端：

     ```
     bash
     复制代码
     ./frpc -c frpc.ini
     ```

5. **开放防火墙端口**：

   - 确保在外部服务器上开放 `7000` 端口（FRP 服务端）和 `2525` 端口（FRP 客户端转发的端口），以便能够接受外部连接。

   - 例如，使用 

     ```
     ufw
     ```

      管理防火墙规则：

     ```
     bash
     复制代码
     sudo ufw allow 7000
     sudo ufw allow 2525
     ```

6. **测试外部访问**：

   - 从外部机器，尝试通过 

     ```
     telnet
     ```

      或其他邮件客户端连接到你的邮件服务器：

     ```
     bash
     复制代码
     telnet <外部服务器IP> 2525
     ```

   - 尝试发送邮件，确认本地 Postfix 可以接收到。

以上步骤完成后，外部用户可以通过外部服务器的 `2525` 端口访问你本地的 Postfix 邮件服务器，实现邮件的收发功能。确保你的外部服务器和本地服务器配置安全，以防止未授权的访问和邮件滥用。