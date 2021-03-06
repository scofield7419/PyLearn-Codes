#web

#服务器
#底层代码由专门的服务器软件实现，我们用 Python 专注于生成 HTML 文档。因为我们不希望接触到 TCP 连接、HTTP 原始请
#求和响应格式，所以，需要一个统一的接口，让我们专心用 Python 编写 Web 业务。

#这个接口就是 WSGI：Web Server Gateway Interface。

#WSGI 接口定义非常简单，它只要求 Web 开发者实现一个函数，就可以
#响应 HTTP 请求。我们来看一个最简单的 Web 版本的“Hello, web!”：

def application2(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	return [b'<h1>Hello, web!</h1>']
#两个参数：
# environ：一个包含所有 HTTP 请求信息的 dict 对象；
# start_response：一个发送 HTTP 响应的函数。


def application(environ, start_response):
	start_response('200 OK', [('Content-Type', 'text/html')])
	body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
	return [body.encode('utf-8')]







