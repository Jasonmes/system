sudo docker run --network host --gpus all \
           -e HTTP_PROXY=http://localhost:7890 \
           -e HTTPS_PROXY=http://localhost:7890 \
           -e ALL_PROXY=socks5://localhost:7890 \
           -v /home/biw002/workspace/yasi/:/yasi \
           -it yasi:1.3