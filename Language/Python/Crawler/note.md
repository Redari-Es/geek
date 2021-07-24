
**This is the notes for the book which call"实战Python网络爬虫"**

### Chapter 1    
You need to install python3 npm node.js pip    
config pip source list, you can choose aliyun or tuna.tsinghua    
chat the source list
> pip config list  
    
	
edit ~/.pip/pip.conf    
```
[global]
index-url=http://mirrors.aliyun.com/pypi/simple/
[install]
trusted-host=mirrors.aliyun.com
```
**网页的元素定位：**    
+ 1.通过属性id和name来实现定位    
``````
find_element_by_id()
find_element_by_name()
``````
+ 2.通过HTML标签类型和属性class实现定位    ~~
<br>
```
find_element_by_class_name()   
find_element_by_tag_name()    
```   
<br>

+ 3.通过标签值实现定位，partial_link用于模糊匹配    
```
find_element_by_link_text()   
find_element_by_partial_link_text()    
```    
+ 4.元素的路径定位选择器   
```
find_element_by_xpath()    
find_element_by_css_selector()    
```    
    

--------

### Chapter 2
--------


### Chapter 3
--------

### Chapter 4
--------

### Chapter 5    
**爬虫库Urllib**    



--------

### Chapter 6
安装requests库
> pip install requests    
  
> pip install response


> pip install net-tools    
--------

### Chapter 7
安装requests-cache    
> pip install requests-cache    
  
安装flask框架

若需要对Requests-Cache设置不同的存储机制需安装
> pip install redis    
   
> pip install pymongo    
  

### Chapter 8
**爬虫库Requests-HTML**    
> pip install requests-html    

> pip install coda    
  
> pip install scrapy    
  

**find(selector,containing,clean,first,_encoding)**  
参数说明：  
    selector:使用CSS Selector定位网页元素。  
    containg:字符串类型，默认之为None，通过特定文本查找网页元素。  
    clean:是否清除HTML的\<script\>和\<style\>标签，默认值False    
    first:是否只查找第一个网页元素，默认值为False即查找全部元素。  
    _encoding:设置编码格式，默认值为None。

**xpath(selector,clean,first,_encoding)**    
定义:    
参数说明：
    selector:使用XPath Selector定位网页元素。  
    clean:是否清除HTML的\<script>和\<style>标签，默认值False。  
    first:是否只查找第一个网页元素，默认值为False即查找全部元素。   
    _encoding:设置编码格式，默认值为None。  
定义：  
**search(teemplate)**  
参数说明：  
	template:通过元素内容查找第一个元素  
定义：  
**search_all(template)**  
参数说明：  
    template:通过元素内容查找全部元素  




--------


### Chapter 9
> pip install selenium    
    
> npm install webdriver    
  
具体定义的方式可以查看lib/site-packages/selenium/webdriver/common/keys.py

### Chapter 10    
这一章是关于android手机的app数据爬取,需要配置java和android-sdk和node.js    
暂时不做，跳过    

### Chapter 11
Splash, Mitmproxy与Aiohttp    
splash需要docker应用容器
> sudo pacman -S docker-runit docker-compose docker-machine    
   
> sudo ln -s /etc/runit/sv/docker /run/runit/service/    

> sudo sv restart docker    

> sudo docker run -p 8050:8050 scrapinghub/splash    

> pip install mitmproxy    
    
在安装完之后，你需要让你的android手机与你的电脑在同一网域，点击手机wifi修改内容，将代理改为手动，让**服务器主机名**和**服务器端口**分别输入你的电脑ip和8080端口    
运行mitmweb    
   
> pip install aiohttp    
  
> pip install beatifulsoup4    



### Chapter 12    
> pip install pyocr    
  
> pip install pillow    

> pip install pytesser3    

> pacman tesseract tesseract-data-chi_sim    



### Chapter 13
### Chapter 14
### Chapter 15
### Chapter 16
可以看菜鸟教程里的mongodb    
yay -S mongodb-4.0.bin    
查看/var/lib/mongodb/ 和/var/log/mongodb/ 无则创建，但他安装后有自动建的    
接着更改文件的用户访问权限    
sudo chown 你的用户名 目标文件    
然后运行    
mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --fork   
cat /var/log/mongodb/mongod.log    
可以看到成功    
安装可视化工具    
robomongo和mongobooster    
pip install pymongo    





### Chapter 17
### Chapter 18
### Chapter 19
### Chapter 20
### Chapter 21
### Chapter 22
### Chapter 23
### Chapter 24
### Chapter 25
### Chapter 26
### Chapter 27
### Chapter 28

