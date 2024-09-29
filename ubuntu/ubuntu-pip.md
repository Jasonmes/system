Here's an example of setting up the pip configuration file on a Unix-based system:

bash
复制代码
mkdir -p ~/.config/pip
nano ~/.config/pip/pip.conf
Add the following content:

ini
复制代码
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple