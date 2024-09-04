## 安装 `ntfs-3g` 在 MacBook

### 1. 安装 Xcode Command Line Tools

确保已经安装了 Xcode Command Line Tools：

```
xcode-select --install
```

### 2. 安装 MacPorts

1. 访问 [MacPorts 官方网站](https://www.macports.org/install.php) 并下载适合您的 macOS 版本的安装程序。

2. 安装完成后，将 MacPorts 的路径添加到您的 shell 配置文件中。

   如果使用 `zsh`：

   ```
   echo 'export PATH="/opt/local/bin:/opt/local/sbin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```
   
   如果使用 `bash`：
   
   ```
   echo 'export PATH="/opt/local/bin:/opt/local/sbin:$PATH"' >> ~/.bash_profile
   source ~/.bash_profile
   ```
   
3. 更新 MacPorts:

   ```
   sudo port selfupdate
   ```

### 3. 安装 `ntfs-3g` 通过 MacPorts

现在，可以简单地使用 MacPorts 安装 `ntfs-3g`：

```
sudo port install ntfs-3g
```

### 4. 后续设置

一旦 `ntfs-3g` 安装成功，您就可以使用它来挂载、读写 NTFS 文件系统。







## 使用 `ntfs-3g` 挂载 NTFS 文件系统

1. **查找设备路径**

   首先，您需要知道要挂载的设备的路径。可以使用 `diskutil` 列出所有磁盘：

   ```
   diskutil list
   ```

   从输出中找到您的 NTFS 分区。它可能看起来像 `/dev/diskXsY`，其中 `X` 和 `Y` 是数字。

要使用 `ntfs-3g` 挂载这个分区，请按照以下步骤操作：

1. **创建挂载点**

   如果您还没有创建，您需要一个目录来挂载 NTFS 分区。这通常在 `/Volumes` 下完成：

   ```
   sudo mkdir /Volumes/moviePan
   ```
   
2. **使用 `ntfs-3g` 挂载分区**

   使用以下命令挂载 NTFS 分区：

   ```
   sudo ntfs-3g /dev/disk2s1 /Volumes/moviePan -o local -o allow_other
   
   sudo mkdir /Volumes/mycode
   sudo ntfs-3g /dev/disk2s2 /Volumes/mycode -o local -o allow_other -o auto_xattr -o auto_cache
   ```
   
3. **访问挂载点**

   一旦分区被挂载，您可以通过 Finder 或命令行访问 `/Volumes/moviePan` 来查看和编辑文件。

4. **卸载**

   当您完成对分区的访问，并想要安全地卸载它时，使用以下命令：

   ```
   sudo umount /Volumes/moviePan
   ```

这就是挂载和卸载您的外部 NTFS 分区的过程。





