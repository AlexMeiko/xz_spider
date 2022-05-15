# xz_spider

## 介绍  

一个简单的写真爬虫，目前已支持多线程   
a simple spider which can get girl photo.  
这是一个使用Python编写的爬虫，目前仅在Python3.7上测试过。
代码可能较不规范。但我会尽量把它写规范的(超大声🤗  
  
## 环境依赖


|Requirement         |
|--------------------|
|Python3             |
|lxml                |
|fake_useragent      | 

## 📖使用  

**1.安装所需包**  

```shell script 
pip install -r requirements.txt
```
**2.使用vim等文本编辑器更改脚本内参数**  

|变量名            |对应参数     | 
|-----------------|-----------| 
|Threads          |线程数      | 
|Start_Page       |起始页      | 
|End_Page         |结束页      | 


**3.运行getxz.py**  
```shell script 
python3 getxz.py
```  
**4.坐等，爬到的文件在当前目录的data目录中**

## 📢声明：  

爬虫爬取的写真源自硬盘少女(diskgirl.com)，本软件(脚本)仅作学习使用，所有一切倒卖等行为均与本人**无关**。


## License 许可证

This project is under the Apache-2.0 license.

本项目基于 Apache-2.0 协议发布，并增加了 SATA 协议。

当你使用了使用 SATA 的开源软件或文档的时候，在遵守基础许可证的前提下，你必须马不停蹄地给你所使用的开源项目 “点赞” ，比如在 GitHub 上
star，然后你必须感谢这个帮助了你的开源项目的作者，作者信息可以在许可证头部的版权声明部分找到。

本项目的所有代码文件、配置项，除另有说明外，均基于上述介绍的协议发布，具体请看分支下的 LICENSE。

此处的文字仅用于说明，条款以 LICENSE 文件中的内容为准。
