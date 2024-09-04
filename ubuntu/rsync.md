# rsync



### 解释

- `rsync`：同步文件和目录的工具。
- `-a`：归档模式，表示递归传输文件，并保持所有文件属性。
- `-v`：详细模式，显示详细信息。
- `--progress`：显示拷贝进度。
- `/mnt/backupdata/娑婆诃`：源目录。
- `/mnt/mycode/movie/`：目标目录。



### 1. 拷贝“娑婆诃”

```
rsync -av --progress /mnt/backupdata/娑婆诃 /mnt/mycode/movie/
```

### 2. 拷贝“阿基拉 (1988) 1080P”

```
rsync -av --progress '/mnt/backupdata/阿基拉 (1988) 1080P' /mnt/mycode/movie/
```

