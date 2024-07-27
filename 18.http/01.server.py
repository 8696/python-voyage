import socketserver

from post import PostHandler
from get import GetHandler


PORT = 8083


class HttpHandler(GetHandler, PostHandler):
    pass


# 使用with语句创建一个TCP服务器实例，并指定请求处理程序为 HttpHandler
with socketserver.TCPServer(("", PORT), HttpHandler) as httpd:
    """
    创建TCP服务器实例，并确保在程序结束时正确关闭服务器。

    socketserver.TCPServer(("", PORT), HttpHandler) 创建一个TCP服务器实例。
    - 第一个参数: 服务器绑定的地址和端口。"" 表示绑定到所有可用的网络接口。
    - 第二个参数: 请求处理程序类，即每次接收到请求时实例化的处理程序。

    as httpd 将创建的TCP服务器实例赋值给变量httpd，方便在with块内使用。
    """
    print(f"Serving at port {PORT}")  # 打印一条消息，指示服务器正在运行并监听指定端口
    httpd.serve_forever()  # 启动服务器，开始处理传入的HTTP请求。这个方法会一直运行，直到程序被手动停止
