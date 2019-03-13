"""
Created by Alex
"""

from app import create_app

__author__ = 'Alex'

# app = Flask(__name__)
#
# # 开启调试模式1
# # app.debug = True
#
# # 导入配置文件,就可以使用
# app.config.from_object('config')

app = create_app()


if __name__ == '__main__':
    # 开启调试模式2
    app.run(host='0.0.0.0')
