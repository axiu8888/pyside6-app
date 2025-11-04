
# 说明

## 安装环境


```
pip install -r requirements.txt
```

## 打包成exe

首先安装 `pip install pyinstaller`，然后执行下面的打包命令

```
# 有控制台
pyinstaller --onefile app.py

# 无控制台
pyinstaller --onefile -F -w app.py
```


## 注册成Windows服务

```
pip install pywin32

python install_service.py install
python install_service.py start

```

