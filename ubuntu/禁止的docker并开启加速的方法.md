# 国内禁止的docker并开启加速的方法

https://github.com/DaoCloud/public-image-mirror

你可以使用DaoCloud提供的公共镜像加速服务，以加速Docker镜像的下载。以下是具体步骤：

1. **配置Docker加速器**：

   - 编辑 

     ```
     /etc/docker/daemon.json
     ```

      文件，添加以下内容：

     ```
     {
       "registry-mirrors": [
         "https://docker.m.daocloud.io",
         "https://dockerhub.azk8s.cn",
         "https://hub-mirror.c.163.com",
         "https://mirror.baidubce.com"
       ]
     }
     ```

   - 重启Docker服务：

     ```
     bash
     复制代码
     sudo systemctl daemon-reload
     sudo systemctl restart docker
     ```

2. **使用加速后的镜像**：

   - 替换镜像地址前缀。例如：

     ```
     bash
     复制代码
     docker pull m.daocloud.io/nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
     ```

详情请参考[DaoCloud公共镜像加速器](https://github.com/DaoCloud/public-image-mirror)。

