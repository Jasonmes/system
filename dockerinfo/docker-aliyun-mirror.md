# success: register Aliyun and choose arc 
建议手动拉取镜像到本地节点并重启Pod，也可上传镜像至 ACR 或使用订阅海外源镜像功能，再从 ACR 拉取对应镜像。

加速器地址
https://miivxnbd.mirror.aliyuncs.com   
https://miivxnbd.mirror.aliyuncs.com

1. 安装／升级Docker客户端
推荐安装1.10.0以上版本的Docker客户端，参考文档docker-ce

2. 配置镜像加速器
针对Docker客户端版本大于 1.10.0 的用户

您可以通过修改daemon配置文件/etc/docker/daemon.json来使用加速器

sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://miivxnbd.mirror.aliyuncs.com", "https://mirror.gcr.io",
    "https://docker.registry.cyou",
    "https://docker-cf.registry.cyou",
    "https://dockercf.jsdelivr.fyi",
    "https://docker.jsdelivr.fyi",
    "https://dockertest.jsdelivr.fyi",
    "https://mirror.aliyuncs.com",
    "https://dockerproxy.com",
    "https://mirror.baidubce.com",
    "https://docker.m.daocloud.io",
    "https://docker.nju.edu.cn",
    "https://docker.mirrors.sjtug.sjtu.edu.cn"]
}
EOF
sudo systemctl daemon-reload
sudo systemctl restart docker


# next is not try
基本信息
仓库名称
biw002
biw002
复制
仓库地域
华东1（杭州）
仓库类型
私有
代码仓库
https://github.com/Jasonmes/new_adbforhermes
公网地址
registry.cn-hangzhou.aliyuncs.com/biw002/biw002
registry.cn-hangzhou.aliyuncs.com/biw002/biw002
复制
专有网络
registry-vpc.cn-hangzhou.aliyuncs.com/biw002/biw002
registry-vpc.cn-hangzhou.aliyuncs.com/biw002/biw002
复制
经典网络
registry-internal.cn-hangzhou.aliyuncs.com/biw002/biw002
registry-internal.cn-hangzhou.aliyuncs.com/biw002/biw002
复制
摘要
ubuntu
操作指南
制品描述
1. 登录阿里云Docker Registry
$ docker login --username=aliyun3286929657 registry.cn-hangzhou.aliyuncs.com
用于登录的用户名为阿里云账号全名，密码为开通服务时设置的密码。

您可以在访问凭证页面修改凭证密码。

2. 从Registry中拉取镜像
$ docker pull registry.cn-hangzhou.aliyuncs.com/biw002/biw002:[镜像版本号]
3. 将镜像推送到Registry
$ docker login --username=aliyun3286929657 registry.cn-hangzhou.aliyuncs.com
$ docker tag [ImageId] registry.cn-hangzhou.aliyuncs.com/biw002/biw002:[镜像版本号]
$ docker push registry.cn-hangzhou.aliyuncs.com/biw002/biw002:[镜像版本号]
请根据实际镜像信息替换示例中的[ImageId]和[镜像版本号]参数。

4. 选择合适的镜像仓库地址
从ECS推送镜像时，可以选择使用镜像仓库内网地址。推送速度将得到提升并且将不会损耗您的公网流量。

如果您使用的机器位于VPC网络，请使用 registry-vpc.cn-hangzhou.aliyuncs.com 作为Registry的域名登录。

5. 示例
使用"docker tag"命令重命名镜像，并将它通过专有网络地址推送至Registry。

$ docker images
REPOSITORY                                                         TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
registry.aliyuncs.com/acs/agent                                    0.7-dfb6816         37bb9c63c8b2        7 days ago          37.89 MB
$ docker tag 37bb9c63c8b2 registry-vpc.cn-hangzhou.aliyuncs.com/acs/agent:0.7-dfb6816
使用 "docker push" 命令将该镜像推送至远程。

$ docker push registry-vpc.cn-hangzhou.aliyuncs.com/acs/agent:0.7-dfb6816