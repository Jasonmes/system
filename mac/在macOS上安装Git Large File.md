## 在macOS上安装Git Large File Storage (Git LFS) 的步骤如下：



1. **安装Homebrew**：如果你的Mac上还没有安装Homebrew，这是一个非常方便的包管理工具，可以通过下面的命令安装：

   ```
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   安装过程中可能会提示输入密码，并需要联网下载。

2. **安装Git LFS**：通过Homebrew安装Git LFS非常简单，只需打开终端（Terminal）并运行以下命令：

   ```
   brew install git-lfs
   ```

3. **初始化Git LFS**：安装完成后，你需要设置Git LFS。这可以通过以下命令完成：

   ```
   git lfs install
   ```

   这个命令会设置Git的全局钩子，以便Git LFS能够管理大文件。

4. **使用Git LFS**：要让Git LFS管理特定文件类型，你需要在Git仓库中运行如下命令：

   ```
   git lfs track "*.filetype"
   ```

   例如，要跟踪所有PDF文件，你可以使用`git lfs track "*.pdf"`命令。跟踪的文件类型会被记录在`.gitattributes`文件中。

5. **提交更改**：在`.gitattributes`文件中添加了跟踪的文件类型后，需要将这个文件提交到你的仓库中：

   ```
   git add .gitattributes
   git commit -m "Track large files with Git LFS"
   ```

这样，Git LFS就安装并配置好了。以后当你提交和推送那些被Git LFS跟踪的文件时，这些文件将会被存储在Git LFS对象存储中，而不是作为常规的Git对象存储。



## 使用这个方法可以追踪相同的后缀名的大文件

1. **使用通配符**：如果这些大文件虽然位于不同的路径，但具有相同的文件扩展名（比如都是`.bin`），你可以使用通配符来跟踪它们。例如：

   ```
   git lfs track "*.bin"
   ```

   这会跟踪所有`.bin`文件，无论它们位于仓库中的哪个位置。

2. **分别跟踪不同类型的文件**：如果文件类型不同，你需要为每种类型的文件运行一次`git lfs track`命令。例如：

   ```
   git lfs track "*.pdf"
   git lfs track "*.psd"
   ```