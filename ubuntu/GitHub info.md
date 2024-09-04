# 推送本地代码到 GitHub

## 1. 如果是使用各个不同的盘来push和pull代码

永远要记得，在做修改文件之前，先**git pull,** 

先同步文件



### 初始化本地仓库

1. **定位到项目目录**:

   ```
   cd ~/lianxian
   ```

2. **初始化 Git 仓库** (如果项目尚未初始化):

   ```
   git init
   ```

### 2. 添加和提交更改

1. **添加特定文件夹到暂存区**:

   ```
   git add src weights
   ```

2. **提交更改到本地仓库**:

   ```
   git commit -m "Add src and weights folders"
   ```

### 连接远程仓库

1. **添加远程仓库**:

   ```
   git remote add origin https://github.com/Jasonmes/lianxian.git
   ```

2. **首次推送到 GitHub**:

   ```
   git push -u origin master
   ```

   或者使用 `main` 分支 (取决于你的默认分支名称):

   ```
   git push -u origin main
   ```

### 遇到的问题及解决方案

#### 问题描述

- 在尝试使用 HTTPS 方式推送时，GitHub 要求输入用户名和密码。但自 2021 年 8 月起，GitHub 不再支持使用密码进行 HTTPS 认证。

#### 解决方案

- **切换到 SSH 方式**:

  1. **确保 SSH 密钥已添加到 GitHub 账户**。

  2. **更改远程仓库 URL 为 SSH 形式**:

     ```
     git remote set-url origin git@github.com:Jasonmes/lianxian.git
     ```

  3. **再次推送代码**:

     ```
     git push -u origin master
     ```

     或使用 `main` 分支：

     ```
     git push -u origin main
     ```

使用 SSH 方式，将自动通过 SSH 密钥验证身份，无需输入用户名和密码。



## 5. 处理 Git 上传大文件

当尝试上传大于 GitHub 允许的最大文件大小限制（100 MB）的文件时，可以使用以下方法：

### 使用 Git Large File Storage (LFS)

Git LFS 是一个用于有效处理大文件的 Git 扩展。

#### 安装 Git LFS

1. **更新包管理器**:

   ```
   sudo apt-get update
   ```
   
2. **安装 Git LFS**:

   ```
   sudo apt-get install git-lfs
   ```
   
3. **初始化 Git LFS**:

   ```
   git lfs install
   ```

#### 配置 Git LFS 追踪大文件

1. **追踪特定的大文件**:

   ```
   git lfs track "weights/*.pt"
   ```
   
2. **添加 `.gitattributes` 文件**:

   ```
   git add .gitattributes
   ```
   
3. **重新添加追踪的文件**:

   ```
   git add weights/*.pt
   ```
   
4. **提交更改**:

   ```
   git commit -m "Track large files with Git LFS"
   ```
   
5. **推送到 GitHub**:

   ```
   git push -u origin master
   ```

### 8. 移除或减小文件大小

如果不使用 Git LFS，可以选择移除或减小大文件的大小。

1. **从仓库中移除大文件**:

   ```
   git rm --cached weights/s0808split.pt
   ```

2. **提交更改**:

   ```
   git commit -m "Remove large file"
   ```

3. **推送到 GitHub**:

   ```
   git push -u origin master
   ```

4. **检查 SSH 密钥**：首先，确保你的系统上已经生成了 SSH 密钥。

   - 可以通过运行 `ls -al ~/.ssh` 来检查 `.ssh` 目录中是否有密钥文件（如 `id_rsa`, `id_rsa.pub`）。

     ```
     ls -al ~/.ssh
     ```

   - 运行以下命令来查看你的公钥内容：

   ```
   cat ~/.ssh/id_rsa.pub
   ```

5. **生成新的 SSH 密钥（如果需要）**：如果你没有 SSH 密钥，

   ```
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ssh-keygen -t rsa -b 4096 -C "wow336@163.com-0829"
   ```

   - "your_email@example.com" 来创建一个新的。这里应该替换为你的电子邮箱地址。

6. **将 SSH 公钥添加到 GitHub**：一旦你有了 SSH 密钥，需要将公钥添加到你的 GitHub 账户。可以通过 GitHub 网站的设置页面来完成这一步。

   ```
   cat ~/.ssh/id_rsa.pub
   SSH 密钥对包括私钥（id_rsa）和公钥（id_rsa.pub）两部分，其中私钥存储在您的计算机上，而公钥则被添加到您要访问的远程服务器或服务的授权列表中
   ```

   

7. **测试 SSH 连接**：通过运行 `ssh -T git@github.com` 来测试你的 SSH 连接。如果一切设置正确，你将看到一条欢迎信息。

8. **确认 Git 仓库的 SSH 地址**：确保你的本地 Git 仓库使用的是 SSH 地址而非 HTTPS 地址。可以通过运行 `git remote -v` 来检查。

9. **重新尝试推送**：完成以上步骤后，再次尝试推送你的代码。

# Please make sure you have the correct access rights

# **SSH Agent 和身份验证**

### 1. `ssh-add -l`

- 作用：列出当前 SSH 代理中已加载的身份验证密钥
- 结果：`Could not open a connection to your authentication agent.`，表示 SSH 代理没有运行

### 2. `eval $(ssh-agent)`

- 作用：启动 SSH 代理并设置环境变量
- 结果：`Agent pid 23043`，表示 SSH 代理已经启动，PID 为 23043

### 3. `ssh-add ~/.ssh/id_rsa`

- 作用：将私钥 `~/.ssh/id_rsa` 添加到当前 SSH 代理中
- 结果：`Identity added: /home/biw002/.ssh/id_rsa (wow336@163.com)`，表示私钥已经添加到代理中，身份验证信息为 `wow336@163.com`

## 提前操作了git add . ， 如何取消

```
可以使用 git reset 
可以手动删除这个 .git/index.lock
```

## 不小心git push了不完整的文件

```
使用 git revert 命令
```



## 能否自动拿到大文件之后添加到.gitattributes



自动检测大文件并将其添加到 `.gitattributes` 文件中以供 Git LFS 跟踪是一个稍微复杂的任务，但可以通过编写一个脚本来实现。这个脚本将会搜索你的仓库中所有大于特定大小的文件，并自动更新 `.gitattributes` 文件。

以下是一个简单的脚本示例，你可以根据自己的需求进行修改。这个脚本将会查找所有大于10MB（10240KB）的文件，并把它们添加到 `.gitattributes` 以供 Git LFS 跟踪。

```
#!/bin/bash

# 设置文件大小阈值（以KB为单位），这里设置为10240KB
SIZE_THRESHOLD=10240

# 寻找大于设定阈值的文件
# -size +10M 表示查找大于10MB的文件
# awk '{print $2}' 用于提取文件路径
find . -size +${SIZE_THRESHOLD}k -type f | while read -r file; do
    # 仅当文件不在.gitattributes中时才处理
    if ! grep -q "$file filter=lfs" ".gitattributes"; then
        echo "Adding $file to LFS tracking"
        git lfs track "$file"
    fi
done

# 添加并提交 .gitattributes 文件的更改
git add .gitattributes
git commit -m "Updated .gitattributes with large files"
```

使用这个脚本之前，请确保：

- 你已经安装了 Git LFS 并在仓库中初始化了它。
- 你已经将这个脚本保存为一个文件，比如 `track_large_files.sh`。
- 你已经给了这个脚本执行权限，可以通过运行 `chmod +x track_large_files.sh` 命令来实现。

然后，你可以通过运行这个脚本自动添加大文件到 `.gitattributes`。这个脚本可以根据你的具体需要进行修改，比如改变文件大小阈值或者添加额外的逻辑来处理特定类型的文件。



## **检查当前分支**：

运行 `git branch` 查看当前的分支列表，确认是否有 `master` 分支。



### Git 错误

错误消息 `remote: fatal: pack exceeds maximum allowed size (2.00 GiB)` 表明您尝试推送到远程仓库的数据包超过了GitHub允许的最大文件大小限制。GitHub 对于单个文件和推送的总大小都有限制，目前这个限制是2GB。当您尝试推送一个超过这个大小的数据包时，就会遇到这个错误



##  解决“ssh:connect to host github.com port 22: Connection timed out”

换个端口，操作方法：

1.进入~/.ssh下

```shell
cd ~/.ssh
1
```

2.创建一个config文件(这里我用的[vim编辑器](https://so.csdn.net/so/search?q=vim编辑器&spm=1001.2101.3001.7020))

```shell
vim config
1
```

3.编辑文件内容：

```shell
Host github.com
User git
Hostname ssh.github.com
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
Port 443

Host gitlab.com
Hostname altssh.gitlab.com
User git
Port 443
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa
```

### git commit 要求告知你是谁

```
Github:
git config --global user.email "wow336@163.com"
git config --global user.name "Jasonmes"

```

## fatal: unable to access 

## 修改hosts文件

Ubuntu系统：sudo vim /etc/hosts

```
# 13.250.177.223 github.com
20.205.243.166 github.com
# 75.126.164.178 github.global.ssl.fastly.net
103.42.176.244 github.global.ssl.fastly.net
100.67.155.102 gitlab.alibaba-inc.com
```

主要修改：github的ip和github.global.ssl.fastly.net的ip

使用下面的网址来查看

```
https://ip.tool.chinaz.com/github.global.ssl.fastly.net
```

## 强制推送

```
git push -f origin main
```



## 问题：pushkex_exchange_identification: Connection closed by remote host
Connection closed by 127.0.0.1 port 7890
fatal: Could not read from remote repository.Please make sure you have the correct access rights
and the repository exists.
```
nano ~/.ssh/config
```

```
Host 192.168.100.2
  HostName 192.168.100.2
  User biw002

Host 39.108.92.207
  HostName 39.108.92.207
  User root

Host github
  HostName github.com
  User git
  IdentityFile "~/.ssh/id_rsa"

Host github.com
  Hostname ssh.github.com
  Port 443
```

将端口改为Port 443





# OpenSSL version mismatch. Built against 30000020, you have 30200010

两个原因造成，conda会安装另外一个版本的openssl，于是系统有两个版本的openssl

下面两个部分，一个在系统安装最新的git

于是我全部卸载了这两个版本的openssl，git push就没有问题了，尚且没有了解openssl的作用是什么

```
OpenSSL 是一个广泛使用的开源加密库和工具集，用于实现加密和安全通信的功能。它在各种系统和应用程序中提供了多种加密相关的功能。以下是 OpenSSL 的主要用途和功能：

加密与解密：
OpenSSL 提供了多种加密算法，包括对称加密和非对称加密。它支持 AES、DES、3DES、RSA、DSA、ECDSA 等多种算法。
哈希与消息摘要：
OpenSSL 支持计算各种哈希函数，如 SHA-256、SHA-3、MD5 等，用于生成消息摘要，以验证数据的完整性。
数字证书和公钥基础设施 (PKI)：
OpenSSL 用于生成和管理数字证书，包括证书签名请求 (CSR)、证书颁发、证书撤销列表 (CRL) 等。它在 PKI 环境中是一个核心组件。
安全套接字层 (SSL) 和传输层安全 (TLS)：
OpenSSL 实现了 SSL/TLS 协议，用于建立加密的网络连接。它广泛用于 Web 服务器、邮件服务器、VPN、远程登录等领域，确保数据在传输过程中是加密和安全的。
生成和管理密钥：
OpenSSL 可用于生成密钥对（如 RSA 或 ECDSA），以及管理公钥和私钥。
加密协议的工具：
OpenSSL 提供了一组命令行工具，供开发人员和管理员用于各种加密任务，如加密文件、生成证书、调试 SSL/TLS 连接等。
数字签名与验证：
OpenSSL 支持生成和验证数字签名，确保数据或证书的真实性和完整性。
随机数生成：
OpenSSL 包含一个强大的随机数生成器（RNG），用于加密密钥和其他需要随机性的操作。
```

# git@github.com: Permission denied (publickey). fatal: Could not read from remote repository. Please make sure you have the correct access rights and the repository exists.

你遇到的问题可能是由于以下几个原因导致的。我们可以逐一排查并解决：

### 1. 确保SSH代理正在运行并添加了你的密钥

首先，确保你的SSH代理正在运行，并且已经添加了你的SSH密钥：

```
sh
复制代码
# 启动SSH代理
eval "$(ssh-agent -s)"

# 添加SSH密钥
ssh-add ~/.ssh/id_rsa
```

### 2. 检查SSH配置文件

检查你的`~/.ssh/config`文件，确保包含以下内容：

```
sh
复制代码
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_rsa
```

如果没有这个文件，可以创建并添加上述内容。

### 3. 测试SSH连接

测试你是否能够通过SSH连接到GitHub：

```
sh
复制代码
ssh -T git@github.com
```

你应该看到类似以下的消息：

```
sh
复制代码
Hi username! You've successfully authenticated, but GitHub does not provide shell access.
```

如果看到其他错误信息，可能是你的密钥配置有问题。

### 4. 检查GitHub上的SSH密钥

确保你已经正确地将SSH公钥添加到GitHub的设置中。可以登录GitHub，进入`Settings` -> `SSH and GPG keys`，确认你的公钥已在列表中。

### 5. 确认目录权限

`fatal: could not create work tree dir 'my_frp_client': Permission denied` 提示权限问题，确保你有权限在当前目录下创建文件夹。尝试在另一个目录下克隆仓库，或者更改当前目录的权限：

```
sh
复制代码
# 更改目录权限为当前用户
sudo chown -R $(whoami):$(whoami) /workspace
```

### 6. 不要使用sudo运行git命令

不建议使用`sudo`运行`git`命令，因为这会导致使用root用户的SSH配置，而不是你当前用户的配置。只需使用普通用户运行`git clone`命令。

### 结合以上步骤，重新尝试克隆仓库：

```
sh
复制代码
# 确保当前用户有目录权限，不要使用sudo
git clone git@github.com:Jasonmes/my_frp_client.git
```



## 强制覆盖

```
git reset --hard
git pull

git stash
git pull
```

