

```
==> Pouring sing-box--1.6.0.ventura.bottle.1.tar.gz
==> Caveats
To start sing-box now and restart at login:
  brew services start sing-box
Or, if you don't want/need a background service you can just run:
  /usr/local/opt/sing-box/bin/sing-box run --config /usr/local/etc/sing-box/config.json
==> Summary
🍺  /usr/local/Cellar/sing-box/1.6.0: 7 files, 25.6MB
==> Running `brew cleanup sing-box`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
(base) jasonmes@biw003deAir ~ %
(base) jasonmes@biw003deAir ~ % brew services start sing-box
==> Tapping homebrew/services
Cloning into '/usr/local/Homebrew/Library/Taps/homebrew/homebrew-services'...
remote: Enumerating objects: 2571, done.
remote: Counting objects: 100% (392/392), done.
remote: Compressing objects: 100% (182/182), done.
remote: Total 2571 (delta 248), reused 284 (delta 205), pack-reused 2179
Receiving objects: 100% (2571/2571), 711.45 KiB | 87.00 KiB/s, done.
Resolving deltas: 100% (1187/1187), done.
Tapped 1 command (45 files, 886KB).
==> Successfully started `sing-box` (label: homebrew.mxcl.sing-box)
(base) jasonmes@biw003deAir ~ % homebrew.mxcl.sing-box
zsh: command not found: homebrew.mxcl.sing-box
(base) jasonmes@biw003deAir ~ %
```

### 1. 验证服务状态

您可以使用以下命令来检查 Sing-box 服务的状态：

```
bashCopy code
brew services list
```

在服务列表中，应该可以看到 `sing-box`，并且状态应该是 `started`。

### 2. 配置文件

确保您的配置文件 `config.json`（或者是 YAML 格式的配置文件）正确放置在 `/usr/local/etc/sing-box/` 目录下，并且配置了正确的代理设置。您可以使用文本编辑器打开并编辑这个文件。

### 3. 使用 Sing-box

如果您使用 Homebrew 的服务来管理 Sing-box，它应该已经在后台运行了。不过，您也可以手动启动 Sing-box，使用以下命令：

```
bashCopy code
/usr/local/opt/sing-box/bin/sing-box run --config /usr/local/etc/sing-box/config.json
```

这条命令会让 Sing-box 根据您的配置文件来运行。

### 4. 测试代理

为了测试代理是否工作，您可以尝试访问一些通常无法访问的网站，或者使用命令行工具如 `curl` 来测试特定的代理端口。

### 5. 高级配置

Sing-box 支持更高级的配置，比如路由规则、策略组等。如果您需要，可以查看官方文档以获取更详细的配置方法。

## sing-box配置

# Tun

```
{
  "dns": {
    "servers": [
      {
        "tag": "google",
        "address": "tls://8.8.8.8"
      },
      {
        "tag": "local",
        "address": "223.5.5.5",
        "detour": "direct"
      },
      {
        "tag": "block",
        "address": "rcode://success"
      }
    ],
    "rules": [
      {
        "geosite": "category-ads-all",
        "server": "block",
        "disable_cache": true
      },
      {
        "outbound": "any",
        "server": "local"
      },
      {
        "geosite": "cn",
        "server": "local"
      }
    ],
    "strategy": "ipv4_only"
  },
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "auto_route": true,
      "strict_route": false,
      "sniff": true
    }
  ],
  "outbounds": [
    {
      "type": "shadowsocks",
      "tag": "proxy",
      "server": "mydomain.com",
      "server_port": 8080,
      "method": "2022-blake3-aes-128-gcm",
      "password": "8JCsPssfgS8tiRwiMlhARg=="
    },
    {
      "type": "direct",
      "tag": "direct"
    },
    {
      "type": "block",
      "tag": "block"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    }
  ],
  "route": {
    "rules": [
      {
        "protocol": "dns",
        "outbound": "dns-out"
      },
      {
        "geosite": "cn",
        "geoip": [
          "private",
          "cn"
        ],
        "outbound": "direct"
      },
      {
        "geosite": "category-ads-all",
        "outbound": "block"
      }
    ],
    "auto_detect_interface": true
  }
}
```

# Linux 服务器安装

#### 依赖

- Linux & Systemd
- Git
- C 编译器环境

#### 安装

```
git clone -b main https://github.com/SagerNet/sing-box
cd sing-box
./release/local/install_go.sh # 如果已安装 golang 则跳过
./release/local/install.sh
```

编辑配置文件 `/usr/local/etc/sing-box/config.json`

```
./release/local/enable.sh
```

#### 更新

```
./release/local/update.sh
```

#### 其他命令

| 操作     | 命令                                          |
| :------- | :-------------------------------------------- |
| 启动     | `sudo systemctl start sing-box`               |
| 停止     | `sudo systemctl stop sing-box`                |
| 强制停止 | `sudo systemctl kill sing-box`                |
| 重启     | `sudo systemctl restart sing-box`             |
| 查看日志 | `sudo journalctl -u sing-box --output cat -e` |
| 实时日志 | `sudo journalctl -u sing-box --output cat -f` |
| 卸载     | `./release/local/uninstall.sh`                |

# DNS 劫持

#### 探测模式

```
{
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "auto_route": true,
      "sniff": true // 必须
    }
  ],
  "outbounds": [
    {
      "type": "direct"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    }
  ],
  "route": {
    "rules": [
      {
        "protocol": "dns",
        "outbound": "dns-out"
      }
    ],
    "auto_detect_interface": true
  }
}
```

#### 端口模式

```
{
  "inbounds": [
    {
      "type": "tun",
      "inet4_address": "172.19.0.1/30",
      "auto_route": true,
      "sniff": true // 非必须
    }
  ],
  "outbounds": [
    {
      "type": "direct"
    },
    {
      "type": "dns",
      "tag": "dns-out"
    }
  ],
  "route": {
    "rules": [
      {
        "port": 53,
        "outbound": "dns-out"
      }
    ],
    "auto_detect_interface": true
  }
}
```

# DNS 规则

### 结构

```
{
  "dns": {
    "rules": [
      {
        "inbound": [
          "mixed-in"
        ],
        "ip_version": 6,
        "query_type": [
          "A",
          "HTTPS",
          32768
        ],
        "network": "tcp",
        "auth_user": [
          "usera",
          "userb"
        ],
        "protocol": [
          "tls",
          "http",
          "quic"
        ],
        "domain": [
          "test.com"
        ],
        "domain_suffix": [
          ".cn"
        ],
        "domain_keyword": [
          "test"
        ],
        "domain_regex": [
          "^stun\\..+"
        ],
        "geosite": [
          "cn"
        ],
        "source_geoip": [
          "private"
        ],
        "source_ip_cidr": [
          "10.0.0.0/24"
        ],
        "source_port": [
          12345
        ],
        "source_port_range": [
          "1000:2000",
          ":3000",
          "4000:"
        ],
        "port": [
          80,
          443
        ],
        "port_range": [
          "1000:2000",
          ":3000",
          "4000:"
        ],
        "process_name": [
          "curl"
        ],
        "process_path": [
          "/usr/bin/curl"
        ],
        "package_name": [
          "com.termux"
        ],
        "user": [
          "sekai"
        ],
        "user_id": [
          1000
        ],
        "clash_mode": "direct",
        "invert": false,
        "outbound": [
          "direct"
        ],
        "server": "local",
        "disable_cache": false
      },
      {
        "type": "logical",
        "mode": "and",
        "rules": [],
        "server": "local",
        "disable_cache": false
      }
    ]
  }
}
```

当内容只有一项时，可以忽略 JSON 数组 [] 标签

### 默认字段

默认规则使用以下匹配逻辑:
(`domain` || `domain_suffix` || `domain_keyword` || `domain_regex` || `geosite`) &&
(`port` || `port_range`) &&
(`source_geoip` || `source_ip_cidr`) &&
(`source_port` || `source_port_range`) &&
`other fields`

#### inbound

[入站](https://sing-box.sagernet.org/zh/configuration/inbound) 标签.

#### ip_version

4 (A DNS 查询) 或 6 (AAAA DNS 查询)。

默认不限制。

#### query_type

DNS 查询类型。值可以为整数或者类型名称字符串。

#### network

`tcp` 或 `udp`。

#### auth_user

认证用户名，参阅入站设置。

#### protocol

探测到的协议, 参阅 [协议探测](https://sing-box.sagernet.org/zh/configuration/route/sniff/)。

#### domain

匹配完整域名。

#### domain_suffix

匹配域名后缀。

#### domain_keyword

匹配域名关键字。

#### domain_regex

匹配域名正则表达式。

#### geosite

匹配 GeoSite。

#### source_geoip

匹配源 GeoIP。

#### source_ip_cidr

匹配源 IP CIDR。

#### source_port

匹配源端口。

#### source_port_range

匹配源端口范围。

#### port

匹配端口。

#### port_range

匹配端口范围。

#### process_name

仅支持 Linux、Windows 和 macOS.

匹配进程名称。

#### process_path

仅支持 Linux、Windows 和 macOS.

匹配进程路径。

#### package_name

匹配 Android 应用包名。

#### user

仅支持 Linux。

匹配用户名。

#### user_id

仅支持 Linux。

匹配用户 ID。

#### clash_mode

匹配 Clash 模式。

#### invert

反选匹配结果。

#### outbound

匹配出站。

`any` 可作为值用于匹配任意出站。

#### server

必填

目标 DNS 服务器的标签。

#### disable_cache

在此查询中禁用缓存。

#### rewrite_ttl

重写 DNS 回应中的 TTL。

### 逻辑字段

#### type

```
logical
```

#### mode

```
and` 或 `or
```

#### rules

包括的默认规则。



# 入站

### 结构

```
{
  "inbounds": [
    {
      "type": "",
      "tag": ""
    }
  ]
}
```

### 字段

| 类型          | 格式                                                         | 注入支持 |
| :------------ | :----------------------------------------------------------- | :------- |
| `direct`      | [Direct](https://sing-box.sagernet.org/zh/configuration/inbound/direct) | X        |
| `mixed`       | [Mixed](https://sing-box.sagernet.org/zh/configuration/inbound/mixed) | TCP      |
| `socks`       | [SOCKS](https://sing-box.sagernet.org/zh/configuration/inbound/socks) | TCP      |
| `http`        | [HTTP](https://sing-box.sagernet.org/zh/configuration/inbound/http) | TCP      |
| `shadowsocks` | [Shadowsocks](https://sing-box.sagernet.org/zh/configuration/inbound/shadowsocks) | TCP      |
| `vmess`       | [VMess](https://sing-box.sagernet.org/zh/configuration/inbound/vmess) | TCP      |
| `trojan`      | [Trojan](https://sing-box.sagernet.org/zh/configuration/inbound/trojan) | TCP      |
| `naive`       | [Naive](https://sing-box.sagernet.org/zh/configuration/inbound/naive) | X        |
| `hysteria`    | [Hysteria](https://sing-box.sagernet.org/zh/configuration/inbound/hysteria) | X        |
| `shadowtls`   | [ShadowTLS](https://sing-box.sagernet.org/zh/configuration/inbound/shadowtls) | TCP      |
| `tuic`        | [TUIC](https://sing-box.sagernet.org/zh/configuration/inbound/tuic) | X        |
| `hysteria2`   | [Hysteria2](https://sing-box.sagernet.org/zh/configuration/inbound/hysteria2) | X        |
| `vless`       | [VLESS](https://sing-box.sagernet.org/zh/configuration/inbound/vless) | TCP      |
| `tun`         | [Tun](https://sing-box.sagernet.org/zh/configuration/inbound/tun) | X        |
| `redirect`    | [Redirect](https://sing-box.sagernet.org/zh/configuration/inbound/redirect) | X        |
| `tproxy`      | [TProxy](https://sing-box.sagernet.org/zh/configuration/inbound/tproxy) | X        |

#### tag

入站的标签。



# SOCKS

`socks` 入站是一个 socks4, socks4a 和 socks5 服务器.

### 结构

```
{
  "type": "socks",
  "tag": "socks-in",

  ... // 监听字段

  "users": [
    {
      "username": "admin",
      "password": "admin"
    }
  ]
}
```

### 监听字段

参阅 [监听字段](https://sing-box.sagernet.org/zh/configuration/shared/listen/)。

### 字段

#### users

SOCKS 用户

如果为空则不需要验证。

### 1. DNS 配置

这部分配置定义了 DNS 服务器的设置和 DNS 请求的处理规则。它包括三个服务器配置（Google DNS、本地 DNS 和一个用于拦截广告的 DNS）和对应的处理规则。

### 2. 入站（Inbounds）配置

这里配置了网络代理的入站连接。例如，`tun` 类型的入站配置通常用于虚拟网络接口，用于处理通过 TUN 设备的数据。

### 3. 出站（Outbounds）配置

出站配置定义了数据包的发送方式。在您的配置中，包括了 Shadowsocks 代理、直连、拦截和 DNS 出站处理。

### 4. 路由（Route）配置

路由规则定义了如何根据不同的条件（如协议、地理位置、IP 地址等）来处理网络流量，指定流量应该通过哪个出站代理发送。

### 5. Linux 服务器安装指南

提供了在 Linux 系统上安装 Sing-box 的步骤，包括安装依赖、克隆仓库、安装 Go 语言环境、以及启动和更新 Sing-box 的命令。

### 6. DNS 劫持配置

DNS 劫持部分包含了两种模式：探测模式和端口模式。这两种模式都涉及到 DNS 请求的处理方式。

### 7. DNS 规则结构

详细说明了 DNS 规则的结构，包括各种匹配条件和字段的使用方式。

### 8. 入站类型

列出了 Sing-box 支持的各种入站协议类型，例如 SOCKS、HTTP、Shadowsocks、VMess 等。

### 9. SOCKS 入站配置

具体说明了如何配置 SOCKS 代理服务器，包括用户验证设置。

这些配置项使 Sing-box 成为一个强大的网络工具，能够处理复杂的网络代理需求。配置时，请确保正确理解每个配置项的含义，并根据您的网络环境和需求进行调整。如果您对某些配置项或其作用有疑问，我可以提供进一步的解释。





要暂时停止 Sing-box 服务，您可以使用 Homebrew 提供的服务管理命令。在终端中执行以下命令即可停止 Sing-box：

```
brew services stop sing-box
```

这个命令会停止当前运行的 Sing-box 服务。当您需要重新启动服务时，可以使用相似的命令来启动它：

```
brew services start sing-box
```