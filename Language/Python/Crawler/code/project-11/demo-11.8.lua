#lua脚本
function main(splash)
	splash:set_custom_headers({
		["User-Agent"]="Splash"
		["Referer"]="https://www.baidu.com/"
	})
	splash:go("http://httpbin.org/get")
	return{
		splash:html()
	}
end
