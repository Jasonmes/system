# 清理Mac存储空间指南

## 1. 清理不必要的Conda安装包

执行以下命令来清理 Conda 缓存：

```
conda clean --all
```

### 清理包缓存

1. 清理包缓存：

   ```
   conda clean --packages
   ```

### 清理 tarballs

1. 清理 tarball 文件：

   ```
   conda clean --tarballs
   ```

### 清理日志文件

1. 清理日志文件：

### 查看所有已安装的Conda包

```
conda list
```

### 删除不需要的Conda包

```
conda remove 包名
```

## 2. 清理未使用的Conda环境

### 列出所有Conda环境

```
conda env list
```

### 删除不需要的环境

```
conda env remove -n 环境名
```

## 3. 清理Xcode

### 查找所有安装的Xcode版本

```
sudo find / -name "Xcode.app" 2>/dev/null
```

### 删除旧版本的Xcode（如果有）

假设旧版本路径为 `/Applications/Xcode_旧版本.app`：

```
sudo rm -rf /Applications/Xcode_旧版本.app
```

### 清理Xcode派生数据和缓存

```
rm -rf ~/Library/Developer/Xcode/DerivedData/*
rm -rf ~/Library/Developer/CoreSimulator/Devices/*
rm -rf ~/Library/Caches/com.apple.dt.Xcode/*
```

## 4. 使用内置工具清理存储

### 使用macOS内置存储管理工具

1. 打开 `` 菜单，选择 `关于本机`。
2. 点击 `存储` 标签，然后点击 `管理`。
3. 查看并删除不必要的文件和应用程序。

## 5. 删除大文件和重复文件

### 查找大文件

```
du -sh /* 2>/dev/null | sort -h
```

### 删除不需要的大文件或文件夹

```
sudo rm -rf /path/to/large/file_or_folder
```

## 6. 清理下载文件夹和废纸篓

### 清理下载文件夹

```
rm -rf ~/Downloads/*
```

### 清空废纸篓

```
rm -rf ~/.Trash/*
```

## 7. 分析和清理 `Users` 文件夹

### 找出 `Users` 文件夹中占用空间较大的文件和文件夹

```
du -sh /Users/* 2>/dev/null | sort -h
```

### 删除不必要的文件夹

以下是一个示例脚本，用于删除指定的文件夹及其内容：

```
#!/bin/bash

# 要删除的文件夹列表
folders=(
    "/Users/jasonmes/Library/Application Support/Fusion 360"
    "/Users/jasonmes/Library/Application Support/li.zihua.medis2"
    "/Users/jasonmes/Library/Application Support/Lantern"
    "/Users/jasonmes/Library/Application Support/ubports-installer"
    "/Users/jasonmes/Library/Application Support/balena-etcher"
    "/Users/jasonmes/Library/Application Support/chatgpt-mac"
    "/Users/jasonmes/Library/Application Support/cura"
    "/Users/jasonmes/Library/Application Support/Send Anywhere"
    "/Users/jasonmes/Library/Application Support/Spotify"
    "/Users/jasonmes/Library/Application Support/quark-cloud-drive"
    "/Users/jasonmes/Library/Application Support/TorBrowser-Data"
    "/Users/jasonmes/Library/Application Support/Caches/*"
    "/Users/jasonmes/Library/Application Support/minecraft"
    "/Users/jasonmes/Library/Application Support/Slack"
    "/Users/jasonmes/Library/Application Support/Autodesk"
)

# 遍历文件夹并删除
for folder in "${folders[@]}"; do
    if [ -d "$folder" ] || [ -e "$folder" ]; then
        echo "准备删除: $folder"
        rm -rf "$folder"
    else
        echo "文件夹不存在: $folder"
    fi
done

echo "指定的文件夹已处理"
```

### 保存脚本并运行

1. 将上述脚本保存为 `cleanup.sh` 文件：

   ```
   nano cleanup.sh
   ```

2. 复制并粘贴脚本内容，然后保存并退出：

   - 按 `Ctrl + O` 保存，按 `Enter` 确认，按 `Ctrl + X` 退出。

3. 为脚本文件赋予执行权限：

   ```
   chmod +x cleanup.sh
   ```

4. 运行脚本：

   ```
   ./cleanup.sh
   ```