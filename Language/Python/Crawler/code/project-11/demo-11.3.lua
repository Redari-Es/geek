
# lua脚本
function main(splash,args)
	slash:go("http://httpbin.org")
	splash:wait(5)
	return {
		html=splash:html()
	}
end
    
