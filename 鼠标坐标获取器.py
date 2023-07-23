import pyautogui
import time

def get_mouse_position():
	position = pyautogui.position()
	print(f"鼠标当前位置：({position.x}, {position.y})")

while True:
	get_mouse_position()
	time.sleep(5)  # 暂停5秒


'''
退出 65.75
加点：(1704, 827)
上：(957, 335)
中：(957, 474)
下：(957, 613)
成功失败继续：(952, 851)
中下 920 1000
右下 1800 1000

以下为测试（Alpha0.2）内容，Beta1.0不使用该流程
第一次尘民广场 留在只能尘民广场
第2次尘民广场 只能前往居民区
居民区 只能前往尘民广场
第3次尘民广场 只能前往拾荒者
拾荒者 前往王城

'''