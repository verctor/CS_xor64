# 生成cobaltstrike所需的xor64.bin

Usage: `python xor.py`

生成xor64.bin文件，注意原版xor64.bin的读取使用的是`readresource`方法，但是这里生成的是多个xor decode stub，所以读取要用`pickOptions`方法，自己改java代码的时候要注意啦

Tested on：win7 sp1，win10 v1803
有问题欢迎提出来
