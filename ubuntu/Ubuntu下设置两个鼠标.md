## Ubuntu下如何设置两个鼠标

在Ubuntu或其他Linux发行版下实现多个鼠标光标（cursor），你可能需要使用特定的软件或者配置。这通常不是默认支持的功能，但可以通过一些工具如`xinput`和`Multi-Pointer X`（MPX，是X.Org Server的一部分）来实现。

MPX支持从X Server 1.7起开始，能够为每个连接的指针设备提供独立的光标。但是，配置起来可能比较复杂，因为它通常不是为一般的桌面用户场景设计的。

以下是一个简化的指导，用于在Ubuntu中设置多个鼠标光标：

1. 确认你的X版本支持MPX。可以通过运行`X -version`来检查。

2. 查找你的鼠标设备的名称和ID。可以通过命令`xinput list`来获取。

3. 为每个鼠标设备创建一个新的光标。可以使用`xinput create-master`命令来做这件事。例如：

   ```
   xinput create-master "Second Pointer"
   ```

   这会创建一个新的"虚拟"输入设备组，包括一个指针和一个键盘。

4. 将你的物理鼠标设备附加到新创建的虚拟设备。可以使用`xinput reattach`命令来做这件事。例如：

   ```
   xinput reattach <device id> <master device id>
   ```

   其中`<device id>`是你的鼠标设备ID，`<master device id>`是你在上一步创建的"Second Pointer"的ID。

请注意，这些步骤可能会导致系统的输入设备行为变得不稳定，特别是如果你不熟悉X服务器的配置。而且，并不是所有的应用程序都能很好地支持多个鼠标输入。如果你需要这种功能进行特定的工作或开发，建议在进行之前详细了解相关的文档和教程。









One-click prompts

------