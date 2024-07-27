from urllib.parse import urlparse
from basic import BasicHandler


class PostHandler(BasicHandler):
    def do_POST(self):
        super().log()
        if self.path == "/user/save":
            self.save_user_info()
        elif self.path == "/user/update":
            self.update_user_info()
        else:
            super().not_found_JSON()

    def save_user_info(self):
        super().send_json_response({ "user": "save success" })

    def update_user_info(self):
        super().send_json_response({ "user": "update success" })
        