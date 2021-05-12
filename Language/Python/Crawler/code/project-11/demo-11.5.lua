#lua脚本
function main(splash,args)
	local treat=require("treat")
	local response=splash:http_post("http://httpbin.rog",body="name=Python")
	return{
		html=treat.as_string(response.body),
		url=response.url,
		statud=response.status
	}
end
