 Ubuntu 上使用清华源安装 Python 库，你需要更改 pip 的配置文件。按照以下步骤操作：

在你的用户目录下创建一个名为 pip 的文件夹（如果尚不存在）：
bash
Copy code
mkdir ~/.pip
创建或编辑 pip.conf 配置文件：
bash
Copy code
nano ~/.pip/pip.conf
将以下内容复制并粘贴到 pip.conf 中，以使用清华源：
javascript
Copy code
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
trusted-host = pypi.tuna.tsinghua.edu.cn
按 Ctrl+X，然后按 Y，再按回车键保存文件并退出编辑器。
