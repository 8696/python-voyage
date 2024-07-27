import os
from urllib.parse import urlparse

from basic import BasicHandler
DIRECTORY = os.path.join(os.path.dirname(__file__), "static")  # 修改：定义静态文件目录

class GetHandler(BasicHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)  # 修改：初始化时指定静态文件目录

    def do_GET(self):
        super().log()
        if self.path == "/user/get":  # 修改：改为普通if判断，不使用match
            self.get_user_info()
        else:
            self.handle_static_files()

    def handle_static_files(self):
        super().do_GET()

    def get_user_info(self):
        super().send_json_response({"name": "Alice", "age": 25})

    def end_headers(self):
        
        if self.command == 'GET':
            extension = self.get_request_extension()
            if extension in ['js', 'css', 'png', 'jpg', 'jpeg', 'gif']:
                self.send_header('Cache-Control', 'public, max-age=31536000')  # 设置缓存
            else:
                self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')  # 设置缓存

        super().end_headers()  # 调用父类方法

    def get_request_extension(self):
        # 解析URL
        parsed_url = urlparse(self.path)
        # 获取路径部分
        path = parsed_url.path
        # 使用os.path.splitext分离路径和扩展名
        _, ext = os.path.splitext(path)
        # 去掉开头的点
        return ext[1:] if ext else ''
    