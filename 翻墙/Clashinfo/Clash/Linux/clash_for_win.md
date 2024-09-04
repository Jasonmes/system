



## 暂时是失败不可用的





https://docs.cfw.lbyczf.com/contents/configfile.html#%E6%A0%BC%E5%BC%8F

格式
Clash 配置文件格式为YAML，具体写法参考：https://github.com/Dreamacro/clash/wiki/configuration

CFW 启动的过程会使用到两个配置文件，分别是：

Home Directory/config.yaml
Home Directory/profiles/xxxx.yaml

https://github.com/Fndroid/clash_for_windows_pkg/releases/tag/0.20.22
https://github.com/Dreamacro/clash/wiki/configuration

Clash 使用YAML，YAML Ain't Markup Language，作为配置文件。YAML 被设计为易于计算机阅读、编写和解释，通常用于精确的配置文件。在本章中，我们将介绍 Clash 的常见功能以及如何使用和配置它们。

Clash的工作原理是在本端开启HTTP、SOCKS5或透明代理服务器。当请求或数据包传入时，Clash使用 VMess、Shadowsocks、Snell、Trojan、SOCKS5 或 HTTP 协议将数据包路由到不同的远程服务器（“节点”）。

proxies:
  - name: Shadowsocks
    type: socks5
    server: 127.0.0.1
    port: 1080
    proxy-groups:
  - name: Proxy
    type: select
    proxies:
      - Shadowsocks
    rules:
  - "MATCH,DIRECT"