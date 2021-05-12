#lua脚本
function main(splash)
	splash:go("https://www.baidu.com")
	return{
		#返回cookies信息
		splash:get_cookies()
	}
end
