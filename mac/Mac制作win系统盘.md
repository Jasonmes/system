# Mac制作win系统盘

1. 先找到你的u盘diskutil list 

2. 将U盘格式化为ExFAT

你可以先将U盘格式化为ExFAT文件系统：

```
sudo diskutil eraseDisk ExFAT "WININSTALL" MBR /dev/disk3
```

3. 格式化U盘为NTFS格式

​       卸载u盘

   ``` diskutil unmountDisk /dev/disk3```

4. 格式化U盘为NTFS格式：

```
# 速度非常慢
sudo diskutil eraseDisk NTFS "WININSTALL" MBR /dev/disk3 

# 速度很快
sudo mkntfs -Q -v /dev/disk3s1

```

5. 使用`ntfs-3g`挂载新格式化的NTFS分区：

```
sudo ntfs-3g /dev/disk3s1 /Volumes/WININSTALL
```

6. 挂载ISO镜像

首先，需要将ISO镜像挂载到一个虚拟卷上：

```
hdiutil mount /Users/jasonmes/Downloads/your_windows_iso.iso
```

7.  将ISO内容拷贝到U盘

然后，你需要将ISO镜像中的所有文件和文件夹拷贝到U盘的根目录。你可以使用`cp`或`rsync`命令：

### 显示进度

使用以下命令来查看文件拷贝的进度：

```
sudo rsync -avh --no-perms --progress /Volumes/CCCOMA_X64FRE_EN-US_DV9/ /Volumes/WININSTALL/
```

`--progress`选项会显示每个文件的拷贝进度和总体进度。

其他加速拷贝的方法

如果你发现`rsync`还是比较慢，可以尝试以下方法加速拷贝过程：



1. **使用`cp`命令**： 使用`cp`命令也可以进行拷贝，虽然不显示详细进度，但有时会更快：

   ```
   sudo cp -R /Volumes/CCCOMA_X64FRE_EN-US_DV9/* /Volumes/WININSTALL/
   ```

2. **并行拷贝**： 使用`rsync`的`--jobs`选项（如果支持）来并行拷贝文件（请注意，`rsync`在macOS上可能不支持这个选项）：

   ```
   sudo rsync -avh --no-perms --progress --jobs=4 /Volumes/CCCOMA_X64FRE_EN-US_DV9/ /Volumes/WININSTALL/
   ```

3. **检查U盘性能**： 确保U盘的读写速度良好，有些U盘的读写速度较慢可能影响拷贝速度。如果可能，尝试使用性能更好的U盘。

```
sudo rsync -avh /Volumes/ISO_NAME/ /Volumes/WININSTALL/
```

8. 如果你中断了`rsync`的拷贝操作，想要继续复制而跳过已经成功复制的文件，可以使用`rsync`的`--partial`和`--ignore-existing`选项。这会确保已经复制的文件不会被重复拷贝，并且未完成的文件将继续拷贝。

   ### 继续复制

   1. **使用`--partial`选项**：`rsync`将保留部分传输的文件，以便在重新运行时继续从中断处开始。
   2. **使用`--ignore-existing`选项**：跳过已经存在于目标位置的文件。

   以下是继续复制的命令：

   ```
   sudo rsync -avh --partial --ignore-existing --progress /Volumes/CCCOMA_X64FRE_EN-US_DV9/ /Volumes/WININSTALL/
   ```

   ### 参数说明

   - `-a`：归档模式，表示递归复制目录并保留符号链接、文件权限、用户和组等信息。
   - `-v`：详细模式，显示详细的过程。
   - `-h`：人类可读的文件大小（例如：1K，234M，2G）。
   - `--partial`：保留部分传输的文件，以便在恢复时继续从中断处开始。
   - `--ignore-existing`：跳过已经存在于目标位置的文件。
   - `--progress`：显示详细的进度信息。

   

8. 弹出ISO和U盘

拷贝完成后，确保弹出虚拟卷和U盘：

```
# 确保弹出虚拟卷
hdiutil unmount /Volumes/ISO_NAME

# 弹出u盘
diskutil eject /dev/disk3
```

9. 检查U盘内容

为了确认文件是否已正确复制到U盘，你可以执行以下操作：

列出U盘中的文件：

```
ls -R /Volumes/WININSTALL
```