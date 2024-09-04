您好，您可以使用以下命令来配置 pip 使用清华大学的镜像源：

Copy code
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
这样，当你使用 pip 安装软件包时，它会从清华大学的镜像源中下载软件包。

如果你想恢复使用官方的 PyPI 源，可以使用以下命令：

Copy code
pip config set global.index-url https://pypi.org/simple
希望这能帮到您。