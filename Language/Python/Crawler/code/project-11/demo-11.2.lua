function main(splash, args)
	local ok,reason=splash:go{"http://httpbin.org/post",http_method="POST",body="name=Hubo"}
	if ok then
		return splash:html()
	end
end
