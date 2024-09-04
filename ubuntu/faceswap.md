# faceswap

```
pip install -U pip setuptools wheel
```

### 2. 设置环境变量

在conda环境中自动设置环境变量。编辑conda环境的激活脚本：

```
bash
复制代码
nano ~/miniconda3/envs/faceswap/etc/conda/activate.d/env_vars.sh
```

添加以下内容：

```
bash
复制代码
export PATH=$CONDA_PREFIX/bin:$PATH
export LD_LIBRARY_PATH=$CONDA_PREFIX/lib:$LD_LIBRARY_PATH
```

保存并退出，然后使这些更改生效：

```
bash
复制代码
source ~/miniconda3/envs/faceswap/etc/conda/activate.d/env_vars.sh
```

### 3. 验证安装

在conda环境中运行以下Python代码，验证TensorFlow是否检测到GPU：

```


import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```

看起来每次启动一个新的终端时，GPU的环境变量配置未生效。你可以尝试以下步骤，确保环境变量在每次激活`faceswap`虚拟环境时自动设置：

### 设置环境变量

1. 创建激活脚本：

   ```
   bash
   复制代码
   mkdir -p ~/miniconda3/envs/faceswap/etc/conda/activate.d
   nano ~/miniconda3/envs/faceswap/etc/conda/activate.d/env_vars.sh
   ```

2. 在`env_vars.sh`中添加以下内容：

   ```
   bash
   复制代码
   export CUDA_VISIBLE_DEVICES=0
   export TF_FORCE_GPU_ALLOW_GROWTH=true
   export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
   export PATH=/usr/local/cuda/bin:$PATH
   ```

3. 保存并退出编辑器。

### 确认脚本是否正确执行

每次激活`faceswap`环境时，确保上述脚本正确执行。可以通过以下步骤验证：

1. 重新激活`faceswap`环境：

   ```
   bash
   复制代码
   conda deactivate
   conda activate faceswap
   ```

2. 检查环境变量是否正确设置：

   ```
   bash
   复制代码
   echo $CUDA_VISIBLE_DEVICES
   echo $TF_FORCE_GPU_ALLOW_GROWTH
   echo $LD_LIBRARY_PATH
   echo $PATH
   ```

### 运行提取命令

确保环境变量正确设置后，再运行提取命令：

```
bash
复制代码
python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/1mp4 -o /workspace/mycode/revenge/faceswap/dataimg/1mp4_extract
```

这样应该能确保每次在新终端激活`faceswap`环境时都能正确使用GPU。

## 提取A人脸

```
python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/A -o /workspace/mycode/revenge/faceswap/dataimg/A_extract

python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/1mp4 -o /workspace/mycode/revenge/faceswap/dataimg/1mp4_extract


python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/2mov -o /workspace/mycode/revenge/faceswap/dataimg/2mov_extract

python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/3mov -o /workspace/mycode/revenge/faceswap/dataimg/3mov_extract

python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/3mov -o /workspace/mycode/revenge/faceswap/dataimg/3mov_extract
```

## 提取B人脸

```
python faceswap.py extract -i /workspace/mycode/revenge/faceswap/dataimg/B -o /workspace/mycode/revenge/faceswap/dataimg/B
```



## 模型训练

```
python faceswap.py train -A /workspace/mycode/revenge/faceswap/dataimg/A_extract -B /workspace/mycode/revenge/faceswap/dataimg/B_extract -m /workspace/mycode/revenge/faceswap/model

```

## 转换人脸

```
python faceswap.py convert -i /workspace/mycode/revenge/faceswap/dataimg/1mp4 -o /workspace/mycode/revenge/faceswap/output/1mp4_change -m /workspace/mycode/revenge/faceswap/model 


python faceswap.py convert -i /workspace/mycode/revenge/faceswap/dataimg/2mov -o /workspace/mycode/revenge/faceswap/output/2mov_change -m /workspace/mycode/revenge/faceswap/model 


python faceswap.py convert -i /workspace/mycode/revenge/faceswap/dataimg/3mov -o /workspace/mycode/revenge/faceswap/output/3mov_change -m /workspace/mycode/revenge/faceswap/model
```

