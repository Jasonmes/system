你可以使用以下步骤在Ubuntu下自定义Nvidia显卡的输出分辨率为标准4K（3840x2160）：

1. **查看可用的显示输出**： 首先，使用以下命令查看当前连接的显示设备名称（例如`HDMI-0`, `DP-1`等）：

   ```
   xrandr
   ```

   记下连接到Sony电视的输出名称。

2. **添加4K分辨率模式**： 使用`cvt`命令生成一个3840x2160分辨率的模式行：

   ```
   cvt 3840 2160 60
   ```

   输出结果可能类似于：

   ```
   # 3840x2160 59.98 Hz (CVT) hsync: 134.94 kHz; pclk: 712.75 MHz
   Modeline "3840x2160_60.00"  712.75  3840 3888 3920 4000  2160 2163 2168 2222 -hsync +vsync
   ```

   复制从`Modeline`开始的一行。

3. **创建并添加模式**： 用以下命令添加该模式：

   ```
   xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync
   ```

   然后将模式应用到你的显示设备（假设你的显示设备名称为`HDMI-0`）：

   ```
   xrandr --addmode HDMI-0 3840x2160_60.00
   ```

4. **应用新模式**： 使用以下命令设置新的分辨率模式：

   ```
   xrandr --output HDMI-0 --mode 3840x2160_60.00
   ```

请确保将`HDMI-0`替换为在第一步中找到的正确的显示设备名称。

这将临时设置分辨率，如果你想要使其永久化，可以将这些命令添加到启动脚本中。





##### 您说：

我记得我用的是dp线



###### ChatGPT 说：

ChatGPT

记忆已更新

如果你使用的是DisplayPort（DP）线，那么在设置4K分辨率时，需要将`HDMI-0`替换为相应的DP端口名称。假设你在第一步中发现的DP端口名称是`DP-0`，以下是你需要使用的命令：

1. **添加4K分辨率模式**：

   ```
   xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync
   ```

2. **将模式应用到DP端口**：

   ```
   xrandr --addmode DP-0 3840x2160_60.00
   ```

3. **应用新模式**：

   ```
   xrandr --output DP-0 --mode 3840x2160_60.00
   ```

确保将`DP-0`替换为实际显示设备的名称。如果有问题或者无法找到正确的端口名称，可以重新执行`xrandr`命令以获取准确的信息。





##### 您说：

(base) biw002@biw002:~$ xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync Can't open display (base) biw002@biw002:~$ xrandr --addmode DP-0 3840x2160_60.00 Can't open display (base) biw002@biw002:~$ xrandr --output DP-0 --mode 3840x2160_60.00 Can't open display (base) biw002@biw002:~$ sudo docker images^C (base) biw002@biw002:~$ xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync Can't open display (base) biw002@biw002:~$ xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync



###### ChatGPT 说：

ChatGPT

你遇到的错误提示“Can't open display”通常是因为没有正确设置`DISPLAY`环境变量，或者你在没有X服务器环境（例如通过SSH或在非图形界面）下执行了`xrandr`命令。要解决这个问题，可以尝试以下方法：

1. **确认你在图形界面（X Server）下运行命令**：
   确保你是在桌面环境中（例如GNOME, KDE等）打开的终端中执行命令。如果你通过SSH连接到远程主机，需要使用X11转发或直接在主机的图形界面下操作。

2. **设置`DISPLAY`环境变量**：
   在终端中运行以下命令以确保`DISPLAY`变量已正确设置：

   ```
   export DISPLAY=:0
   ```

   然后再次尝试运行`xrandr`命令。

3. **使用`sudo`运行图形界面命令**：
   如果你使用`sudo`来运行`xrandr`，需要确保`DISPLAY`和`XAUTHORITY`变量被传递。例如：

   ```
   sudo DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync
   ```

4. **检查X Server是否运行**：
   使用以下命令检查X Server是否正在运行：

   ```
   ps -e | grep X
   ```

   如果没有X Server进程在运行，你可能需要启动一个图形会话。

执行完这些步骤后，再尝试自定义你的显示分辨率。





##### 您说：

(base) biw002@biw002:~$ export DISPLAY=:0 (base) biw002@biw002:~$ xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync Can't open display :0



###### ChatGPT 说：

ChatGPT

The error message `Can't open display :0` indicates that the `DISPLAY` environment variable is not set correctly, or the X server is not accessible in your current terminal session. This can happen if you're running the commands in a different context (e.g., via SSH or in a terminal that doesn't have access to the display server).

Here are a few steps to troubleshoot and resolve this issue:

### 1. **Check Display Access:**

- If you're connected via SSH, try connecting with the 

  ```
  -Y
  ```

   or 

  ```
  -X
  ```

   option to enable X11 forwarding:

  ```
  ssh -Y username@hostname
  ```

- If you're on the local machine but in a terminal without display access, try switching to a terminal that has display access.

### 2. **Check the DISPLAY Variable:**

- Ensure that the `DISPLAY` variable is correctly set. On many systems, it should be set automatically when you open a terminal within a graphical session.

- You can check the value of 

  ```
  DISPLAY
  ```

   with:

  ```
  echo $DISPLAY
  ```

- If it returns an empty value, you may not have access to the display. If you're working locally, try running the command in a different terminal session.

### 3. **Run with `sudo`:**

- If you need to run 

  ```
  xrandr
  ```

   with root privileges, make sure you preserve the 

  ```
  DISPLAY
  ```

   variable and X server access:

  ```
  sudo DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xrandr --newmode "3840x2160_60.00" 712.75 3840 3888 3920 4000 2160 2163 2168 2222 -hsync +vsync
  ```

### 4. **Check if X Server is Running:**

- Ensure that the X server is running. If you're in a GUI session, this should be the case, but you can verify by running:

  ```
  ps -e | grep Xorg
  ```

- If no X server is running, you won't be able to use `xrandr` to modify display settings.

### 5. **Use `xhost` to Allow Root Access:**

- You may need to allow root access to the display server if you're using 

  ```
  sudo
  ```

  :

  ```
  xhost +SI:localuser:root
  ```

- After this, try running the `xrandr` command again.

If none of these steps resolve the issue, please provide additional context, such as whether you're running this locally, through SSH, or in another specific environment.