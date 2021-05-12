#lua脚本
function main(splash)
	#如有多条Cookies,则多次使用add_cookies()添加
	splash:add_cookie{"sessionid", "12346"}
	splash:go{"https://www.baidu.com/"}
	return splash:html()
end
