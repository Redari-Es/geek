#find(),xpath(),search(),search_all()
find(selector,containing,clean,first,_encoding)
参数说明：
    selector:使用CSS Selector定位网页元素。
    containg:字符串类型，默认之为None，通过特定文本查找网页元素。
    clean:是否清除HTML的<script>和<style>标签，默认值False。
    first:是否只查找第一个网页元素，默认值为False即查找全部元素。
    _encoding:设置编码格式，默认值为None。
-------------------------------------------------------
定义：
xpath(selector,clean,first,_encoding)
参数说明：
    selector:使用XPath Selector定位网页元素。
    clean:是否清除HTML的<script>和<style>标签，默认值False。
    first:是否只查找第一个网页元素，默认值为False即查找全部元素。
    _encoding:设置编码格式，默认值为None。
    
-------------------------------------------------------
定义：
search(teemplate)
参数说明：
template:通过元素内容查找第一个元素
------------------------------------------------------
定义
search_all(template)
参数说明：
    template:通过元素内容查找全部元素
