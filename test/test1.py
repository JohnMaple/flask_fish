"""
Created by Alex
Desc: 线程隔离
"""
import threading
import time

from werkzeug.local import Local


class A:
    b = 1


my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('sub thread ' + str(my_obj.b))


new_t = threading.Thread(target=worker, name='justin_thread')
new_t.start()
time.sleep(1)


print('main thread ' + str(my_obj.b))
