### Ubuntu下配置自定义ip，一波三折，终于搞定了

- **TUN模式才能做到真正全局代理**

- **下载clash pro, 这个版本才有TUN**

  - https://github.com/Dreamacro/clash 打开这个连接，找到支持tun的链接再打开新的页面，然后下载amd64版本(Ubuntu)

    

- **编写yaml文件**

  ```
  # 指定配置文件的版本
  version: "1"
  
  # 指定代理服务器设置
  proxies:
    - name: "MyProxy"
      type: socks5
      server: 45.149.154.255
      port: 50101
      username: wow3360YHbo
      password: whGN9UEzRf
  
  proxy-groups:
    - name: "Proxy"
      type: select
      proxies:
        - MyProxy
  
  rule-providers: {}
  
  rules:
    - MATCH,Proxy
  
  # TUN模式设置
  tun:
    enable: true
    stack: system
    device-url: dev://tun0
    macOS-auto-route: true
    macOS-auto-detect-interface: true
  ```

  

- **Ubuntu本身没有支持TUN的模式**

  - ```
    sudo apt-get install uml-utilities
    
    # 创建tun0的新设备
    sudo tunctl -t tun0
    # --- 这个是删除
    sudo ip link delete tun0
    
    # 激活
    sudo ip link set tun0 up
    ```
    
  - ```
    ip addr show
    此命令可以查看tun有没有存在
    ```

​        

- **手动设置DNS服务器**

  - ```
    sudo nano /etc/resolv.conf
    ```

  - ```
    nameserver 8.8.8.8
    nameserver 8.8.4.4
    谷歌公共 DNS IP 地址：
    
    Google 公共 DNS IP 地址 (IPv4) 如下：8.8.8.8 和 8.8.4.4
    Google 公共 DNS IPv6 地址如下：2001:4860:4860::8888 和 2001:4860:4860::8844
    
    ```



- **运行clash**

  - ```
    sudo ./clash-linux-amd64 -d . -f proxy_sale_config.yaml
    ```
  
  - ```
    sudo ./clash-linux-amd64 -d . -f config.yaml
    ```

​        

- **kill**

  ```
  sudo kill $(ps aux | grep '[c]lash-linux-amd64' | awk '{print $2}')
  ```

  

