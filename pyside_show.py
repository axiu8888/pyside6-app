
import sys

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QVBoxLayout, QPushButton, QHBoxLayout, \
    QFormLayout, \
    QLineEdit, QStackedLayout, QLabel



def show1():
    # 创建了一个 QApplication 实例，用于管理整个应用程序的事件循环和资源分配。
    app = QApplication()

    # 创建一个空白的 QWidget 对象，它代表着我们的窗体。
    window = QWidget()
    # 设置窗体的标题为 "Simple Window"。
    window.setWindowTitle("Simple Window")
    # 将窗体的大小固定为宽度为 400 像素、高度为 300 像素。
    window.setFixedSize(400, 300)

    # 创建一个 QLabel 对象，并将其作为子组件添加到窗体上。同时，设置标签的显示文本为 "Hello PySide6!"。
    label = QLabel("Hello PySide6!", window)
    # 创建一个 QLabel 对象，并将其作为子组件添加到窗体上。同时，设置标签的显示文本为 "Hello PySide6!"。
    label.move(150, 125)

    # 显示窗体
    window.show()

    # 启动应用程序的事件循环，等待事件的触发和处理，使窗体保持可响应状态。
    app.exec()
    pass


def show2():

    app = QApplication(sys.argv)
    window = QWidget()

    # 创建一个网格布局，作为组合布局的容器
    main_layout = QGridLayout()

    # 创建并设置一个垂直布局
    v_layout = QVBoxLayout()
    v_layout.addWidget(QPushButton('Button 1'))
    v_layout.addWidget(QPushButton('Button 2'))
    v_layout.addWidget(QPushButton('Button 3'))
    v_layout.addWidget(QPushButton('Button 4'))
    # 创建一个容器，并将垂直布局设置给容器
    v_container = QWidget()
    v_container.setLayout(v_layout)
    # 设置边框
    v_container.setStyleSheet("QWidget { border: 2px solid black; padding: 10px; }")
    # 把垂直布局容器添加到网格布局容器中
    main_layout.addWidget(v_container, 0, 0)

    # 创建并设置一个水平布局
    h_layout = QHBoxLayout()
    h_layout.addWidget(QPushButton('Button 1'))
    h_layout.addWidget(QPushButton('Button 2'))
    h_layout.addWidget(QPushButton('Button 3'))
    h_layout.addWidget(QPushButton('Button 4'))
    # 创建一个容器，并将水平布局设置给容器
    h_container = QWidget()
    h_container.setLayout(h_layout)
    # 设置边框
    h_container.setStyleSheet("QWidget { border: 2px solid red; padding: 10px; }")
    # 把水平布局容器添加到网格布局容器中
    main_layout.addWidget(h_container, 0, 1)

    # 创建并设置一个网格布局
    q_layout = QGridLayout()
    q_layout.addWidget(QPushButton('Button 1'), 0, 0)
    q_layout.addWidget(QPushButton('Button 2'), 0, 1)
    q_layout.addWidget(QPushButton('Button 3'), 1, 0)
    q_layout.addWidget(QPushButton('Button 4'), 1, 1)
    # 创建一个容器，并将网格布局设置给容器
    q_container = QWidget()
    q_container.setLayout(q_layout)
    # 设置边框
    q_container.setStyleSheet("QWidget { border: 2px solid green; padding: 10px; }")
    # 把网格布局容器添加到网格布局容器中
    main_layout.addWidget(q_container, 0, 2)

    # 创建并设置一个表单布局
    f_layout = QFormLayout()
    f_layout.addRow('Username', QLineEdit())
    f_layout.addRow('Password', QLineEdit())
    # 创建一个容器，并将表单布局设置给容器
    f_container = QWidget()
    f_container.setLayout(f_layout)
    # 设置边框
    f_container.setStyleSheet("QWidget { border: 2px solid blue; padding: 10px; }")
    # 把表单布局容器添加到网格布局容器中
    main_layout.addWidget(f_container, 1, 0)

    # 创建并设置一个堆叠布局
    s_layout = QStackedLayout()
    s_layout.addWidget(QLabel('页面 1'))
    s_layout.addWidget(QLabel('页面 2'))
    s_layout.addWidget(QLabel('页面 3'))
    s_layout.setCurrentIndex(1)
    # 创建一个容器，并将堆叠布局设置给容器
    s_container = QWidget()
    s_container.setLayout(s_layout)
    # 设置边框
    s_container.setStyleSheet("QWidget { border: 2px solid purple; padding: 10px; }")
    # 把堆叠布局容器添加到网格布局容器中
    main_layout.addWidget(s_container, 1, 1)

    # 设置窗口布局
    window.setLayout(main_layout)
    window.show()

    app.exec()
    pass