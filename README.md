# pyWebduino

项目进行中……

## 环境配置
首先安装websocket-client，这里推荐使用virtualenv。

    git clone https://github.com/bluebanboom/pyWebduino
    cd pyWebduino
    virtualenv . --no-site-packages
    source bin/activate
    pip install -r requirements.txt

## rgbled.py：

rgbled.py是控制板载的RGBled，依次显示红色、绿色、蓝色。

注意更改`boardURL = 'ws://'`为你的smart开发板的IP地址。
