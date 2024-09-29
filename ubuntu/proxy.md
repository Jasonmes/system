1. Determine Your Shell
First, determine which shell you are using. You can check by running:

bash
复制代码
echo $SHELL
Common shells include:

Bash (/bin/bash)
Zsh (/bin/zsh)
2. Edit the Shell Configuration File
Depending on your shell, you'll need to edit the appropriate configuration file:

For Bash: Edit ~/.bashrc
For Zsh: Edit ~/.zshrc
You can edit the file using nano, vim, or any other text editor. For example, using nano:

bash
复制代码
nano ~/.bashrc
Or for Zsh:

bash
复制代码
nano ~/.zshrc
3. Add the Proxy Settings
Add the following lines to the end of the file:

bash
复制代码
export HTTP_PROXY="http://127.0.0.1:7890"
export HTTPS_PROXY="http://127.0.0.1:7890"
4. Apply the Changes
After saving the file, apply the changes by sourcing the configuration file:

For Bash:

bash
复制代码
source ~/.bashrc
For Zsh:

bash
复制代码
source ~/.zshrc
5. Verify the Proxy Settings
To ensure the settings are applied, you can check the values of the environment variables:

bash
复制代码
echo $HTTP_PROXY
echo $HTTPS_PROXY
This will make sure the proxy settings are automatically applied every time you start a new terminal session.