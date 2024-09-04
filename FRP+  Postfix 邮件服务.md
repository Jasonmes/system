# FRP+  Postfix 邮件服务

1. **安装并配置 Postfix**：

2. postfix默认监听的是25的端口，本地25端口可以对应任何服务器对外的端口，包括25

   所以frpc.ini的内容为：

   ```
   [common]
   server_addr = 95.179.211.147
   server_port = 7000
   
   [my_ssh]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 22
   remote_port = 24
   
   [smtp_non_ssl]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 25
   remote_port = 25
   
   [smtp_ssl]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 25
   remote_port = 465
   
   [smtp_submission]
   type = tcp
   local_ip = 127.0.0.1
   local_port = 25
   remote_port = 587
   ```

   

   - 确保 Postfix 已经正确安装和配置好，并且能够在本地正常接收邮件。

   - 例如，你可以使用以下命令安装 Postfix：

     ```
     sudo apt-get update
     sudo apt-get install postfix
     ```

   - 在安装过程中选择 “Internet Site” 配置，并设置邮件域名。

3. 域名要添加服务器ip，例如腾讯购买的域名要添加服务器的ip

4. **安装 FRP**：

   - 从 [FRP 官方 GitHub](https://github.com/fatedier/frp/releases) 下载最新的 FRP 客户端和服务器。

   - 解压下载的文件，例如：

     ```
     tar -zxvf frp_0.37.0_linux_amd64.tar.gz
     ```

   - 将解压后的文件移动到合适的目录，比如 `/usr/local/bin`。

5. **配置 FRP 服务端**：

   - 在外部服务器上，创建 

     ```
     frps.ini
     ```

      文件，并添加以下配置：

     ```
     [common]
     bind_port = 7000
     ```

   - 启动 FRP 服务端：

     ```
     ./frps -c frps.ini
     ```

6. **配置 FRP 客户端**：

   - 在本地安装了 Postfix 的机器上，创建 `frpc.ini` 文件，并添加以下配置：

     ```
     [common]
     server_addr = 95.179.211.147
     server_port = 7000
     
     [my_ssh]
     type = tcp
     local_ip = 127.0.0.1
     local_port = 22
     remote_port = 24
     
     [smtp_non_ssl]
     type = tcp
     local_ip = 127.0.0.1
     local_port = 25
     remote_port = 25
     
     [smtp_ssl]
     type = tcp
     local_ip = 127.0.0.1
     local_port = 25
     remote_port = 465
     
     [smtp_submission]
     type = tcp
     local_ip = 127.0.0.1
     local_port = 25
     remote_port = 587
     ```

     在这里，`server_addr` 为你的外部服务器的 IP 地址，`local_ip` 是本地 Postfix 监听的 IP 地址，`local_port` 是 Postfix 监听的端口（通常是 25），`remote_port` 是外部用户访问的端口（你可以自定义，这里示例为 25）。

   - 启动 FRP 客户端：

     ```
     ./frpc -c frpc.ini
     ```

7. **开放防火墙端口**：

   - 确保在外部服务器上开放 `7000` 端口（FRP 服务端）和 `2525` 端口（FRP 客户端转发的端口），以便能够接受外部连接。

   - 例如，使用 

     ```
     ufw
     ```

      管理防火墙规则：

     ```
     sudo ufw allow 7000
     sudo ufw allow 25
     ```

8. **测试外部访问**：

   - 从外部机器，尝试通过 

     ```
     telnet
     ```

      或其他邮件客户端连接到你的邮件服务器：

     ```
     telnet <外部服务器IP> 2525
     ```

   - 尝试发送邮件，确认本地 Postfix 可以接收到。

以上步骤完成后，外部用户可以通过外部服务器的 `2525` 端口访问你本地的 Postfix 邮件服务器，实现邮件的收发功能。确保你的外部服务器和本地服务器配置安全，以防止未授权的访问和邮件滥用

邮件服务器安装在本机 `biw002` 上，而你希望通过 FRP 实现内网穿透，使外部用户能够访问你本机的 Postfix 服务器。

那么，`main.cf` 中的配置可以保持不变，只需要确保它能正确地配置 Postfix 以便在本地运行，并能够接受到转发来的邮件。

### 配置 `main.cf`

```
myhostname = biw002.bionicwalking.cc
mydomain = bionicwalking.cc
myorigin = $mydomain
mydestination = $myhostname, localhost.$mydomain, $mydomain, localhost
home_mailbox = Maildir/
inet_interfaces = all
```

### 安装并配置 FRP

#### 在外部服务器上配置 FRP 服务端

创建并编辑 `frps.ini`：

```
[common]
bind_port = 7000
```

启动 FRP 服务端：

```
./frps -c frps.ini
```

#### 在本机（biw002）上配置 FRP 客户端

创建并编辑 `frpc.ini`：

```
[common]
server_addr = <外部服务器IP>
server_port = 7000

[smtp]
type = tcp
local_ip = 127.0.0.1
local_port = 25
remote_port = 2525
```

启动 FRP 客户端：

```
./frpc -c frpc.ini
```

### 确保防火墙配置

确保外部服务器上防火墙允许 `7000` 和 `2525` 端口的访问：

```
sudo ufw allow 7000
sudo ufw allow 2525
```

在本地机器上，确保防火墙允许 Postfix 监听的 `25` 端口的访问：

```
sudo ufw allow 25
```

### 测试连接

从外部机器使用 telnet 或邮件客户端测试连接：

```
telnet <外部服务器IP> 2525
```

尝试发送邮件并确认邮件能够成功接收。

## 使用 `swaks` 从外部服务器测试发送邮件

Mac:brew install swaks

```
swaks --to kathleenhendrix5142@bionicwalking.cc --from wow336@163.com --server 95.179.211.147 --port 2525
```

```
swaks --to kathleenhendrix5142@bionicwalking.cc --from wow336@163.com --server 127.0.0.1 --port 25

swaks --to kathleenhendrix5142@bionicwalking.cc --from wow336@163.com --server 95.179.211.147 --port 25

swaks --to kathleenhendrix5142@bionicwalking.cc --from wow336@163.com --server 95.179.211.147 --port 587 --tls

swaks --to kathleenhendrix5142@bionicwalking.cc --from wow336@163.com --server 95.179.211.147 --port 465 --tls

```

### 检查 DNS 记录和 MX 记录

确保您的域名 `bionicwalking.cc` 的 MX 记录正确指向您的邮件服务器。如果 MX 记录不正确，外部邮件服务器将无法将邮件发送到您的服务器。

可以使用以下命令检查 MX 记录：

```
dig mx bionicwalking.cc
```

```
sudo ufw allow 25/tcp
sudo ufw allow 587/tcp
sudo ufw allow 465/tcp
```

