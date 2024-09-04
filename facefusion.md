# facefusion

## 测试clash

7890是运行了clash后的端口，请运行clash后再做下面的操作

```
curl -x [http://127.0.0.1:7890](http://127.0.0.1:7890/) https://www.google.com.hk/
```

``` 
import os

os.environ['http_proxy'] = "http://127.0.0.1:7890"

os.environ['https_proxy'] = "http://127.0.0.1:7890"
```

```
pip uninstall onnxruntime onnxruntime-gpu
pip install onnxruntime-gpu==1.15.1
```

### 设置CUDA和CuDNN环境变量

确保你已经正确设置了CUDA和CuDNN的环境变量。以下是具体步骤：

#### 创建和设置环境变量脚本

1. **创建激活脚本目录**：

   ```
   mkdir -p ~/miniconda3/envs/facefusion/etc/conda/activate.d
   ```

2. **创建和编辑激活脚本文件**：

   ```
   nano ~/miniconda3/envs/facefusion/etc/conda/activate.d/env_vars.sh
   ```

3. **添加以下内容**：

   ```
   export CUDA_HOME=/usr/local/cuda
   export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
   export PATH=$CUDA_HOME/bin:$PATH
   ```

4. **保存并退出**： 按`Ctrl+O`保存，`Ctrl+X`退出。

#### 安装CUDA Toolkit和CuDNN

1. **激活你的Conda环境**：

   ```
   conda activate facefusion
   ```

2. **安装CUDA Toolkit**：

   ```
   conda install cudatoolkit=11.3
   ```

3. **安装CuDNN**：

   ```
   conda install -c conda-forge cudnn
   ```

### 安装ONNX Runtime GPU版本

确保你已经安装了`onnxruntime-gpu`：

```
pip install onnxruntime-gpu
```

### 验证CUDA是否可用

在你的Conda环境中，运行以下Python脚本验证CUDA是否可用：

```
import onnxruntime as ort

providers = ort.get_available_providers()
print("Available providers:", providers)

if 'CUDAExecutionProvider' in providers:
    print("CUDA is available!")
else:
    print("CUDA is not available.")
```

## 端口转发

```
socat TCP-LISTEN:8080,reuseaddr,fork TCP:127.0.0.1:7860
```

##  运行

```
CUDA_VISIBLE_DEVICES=0 python3 run.py -c facefusion.ini

CUDA_VISIBLE_DEVICES=1 python3 run.py -c facefusion.ini
```

http://192.168.1.172:8080/