sudo dpkg  -l  so*  就可以找到sogoupinyin
sudo apt-get  purge  sogoupinyin  (为防止登陆不了桌面sudo dpkg -r sogoupinyin暂不支持使用)
重新设置ibus为系统默认输入方式

             点击  语言支持      键盘输入方式系统  选择IBus


卸载fcitx

             $sudo apt-get purge  fcitx


彻底卸载fcitx及相关配置

            $sudo apt-get autoremove

注销系统用户

           不知道为什么，卸载搜狗后我这边的注销按钮不能使用了，只好通过命令注销

           $sudo pkill Xorg