# 检查是否已经有一个实例在运行
from pylib import mutex_lock

mutex_name = "bt-collecting-box"  # 使用一个唯一的名称，可以是GUID或应用程序的唯一标识


def run():
    import app
    app.start()


if __name__ == '__main__':
    print("\n")
    mutex_lock.lock('pyqt-app', target=run)
    pass
