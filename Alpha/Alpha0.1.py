import cv2
import numpy as np
import pyautogui
import os
import time

def find_big_image(template_path, click_x, click_y, slnum):
    filename = os.path.basename(template_path)

    # 读取模板图像和实时图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE).astype(np.uint8)
    img_rgb = pyautogui.screenshot()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 判断图像大小与实时图像大小是否一致
    if template.shape[:2] == img_rgb.shape[:2] and len(loc[0]) > 0:
        # 如果大小完全一致，在实时图像中单击指定位置
        print("找到匹配项 "+filename)
        pyautogui.click(click_x, click_y)  # 使用pyautogui库执行点击操作
        time.sleep(slnum) 
        return True
    else:
        print("未找到匹配项 "+filename)
        time.sleep(slnum) 
        return False

def find_small_image(template_path ,slnum):
    filename = os.path.basename(template_path)

    # 读取模板图像和实时图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE).astype(np.uint8)
    img_rgb = pyautogui.screenshot()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 找到模板图像在实时图像中的位置并执行点击操作
    if len(loc[0]) > 0:
        print("找到匹配项 "+filename)
        # 获取模板图像的中心位置
        template_center_x = loc[1][0] + template.shape[1] // 2
        template_center_y = loc[0][0] + template.shape[0] // 2
        # 执行点击操作
        pyautogui.click(template_center_x, template_center_y)  # 使用pyautogui库执行点击操作
        time.sleep(slnum) 
        return True
    else:
        print("未找到匹配项 "+filename)
        time.sleep(slnum) 
        return False

def bool_find_big_image(template_path):
    filename = os.path.basename(template_path)

    # 读取模板图像和实时图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE).astype(np.uint8)
    img_rgb = pyautogui.screenshot()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 判断图像大小与实时图像大小是否一致
    if template.shape[:2] == img_rgb.shape[:2] and len(loc[0]) > 0:
        # 如果大小完全一致，在实时图像中单击指定位置
        print("找到匹配项 "+filename)
        return True
    else:
        print("未找到匹配项 "+filename)
        return False

def bool_find_small_image(template_path):
    filename = os.path.basename(template_path)

    # 读取模板图像和实时图像
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE).astype(np.uint8)
    img_rgb = pyautogui.screenshot()
    img_rgb = np.array(img_rgb)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

    # 模板匹配
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 找到模板图像在实时图像中的位置并执行点击操作
    if len(loc[0]) > 0:
        print("找到匹配项 "+filename)
        return True
    else:
        print("未找到匹配项 "+filename)
        return False

def skip(num):
    time.sleep(3)
    while bool_find_small_image('data/8.png') ==True:
        find_small_image('data/8.png',2)
    for _ in range(num):
        pyautogui.click(1800, 1000)
        time.sleep(1)

def out():
    while bool_find_big_image('data/0.png') ==False:
        pyautogui.click(65, 75)
        time.sleep(1)

def dice():
    for _ in range(3):
        pyautogui.click(1800, 1000)
        time.sleep(1)
    time.sleep(3)
    while bool_find_small_image('data/bad.png') == True:
        find_small_image('data/Re1.png',1)
        find_small_image('data/Re2.png',1)
        time.sleep(2)
        #重置
        if bool_find_small_image('data/lost.png') == True:
            lost = 1
            pyautogui.click(952, 851)
            break
    if bool_find_small_image('data/good.png') == True:
        time.sleep(2)
        pyautogui.click(952, 851)
        lost = 0
    elif bool_find_small_image('data/biggood.png') == True:
        time.sleep(2)
        pyautogui.click(952, 851)
        lost = 2
    return lost
    #0为通过 1为重置次数用尽 2为大成功


def Shadow_Castle():
    if find_small_image('data/a1.png',0.2):
        return 1
    elif find_small_image('data/a2.png',0.2):
        return 2
    elif find_small_image('data/a3.png',0.2):
        return 2
    else:
        return 0
'''
big函数比较实时和模板是否一致，一致点击truexy
small函数查找实时里面是否包含模板，包含点击模板在实时中的位置
python main.py
'''
for num in range(3):
    print(str(3-num)+'s后开始执行！')
    time.sleep(1)
Adventure_Results = False
numtimes = 1

while Adventure_Results == False:
    print('这是第'+str(numtimes)+'次冒险')
    find_small_image('data/1.png',0.2)
    find_small_image('data/2.png',2)
    find_small_image('data/3.png',0.2)
    find_small_image('data/4.png',1)
    for _ in range(6):
        find_big_image('data/5.png', 1704, 827 ,0.2)
    #加点
    find_small_image('data/6.png',4)
    find_small_image('data/7.png',1)
    find_small_image('data/8.png',2)
    find_small_image('data/Re2.png',1)
    find_small_image('data/8.png',2)

    find_small_image('data/9.png',1)
    time.sleep(2)
    while bool_find_small_image('data/8.png') ==True:
        find_small_image('data/8.png',1)
    for _ in range(10):
        pyautogui.click(1800, 1000)
        time.sleep(1)
        if bool_find_small_image('data/a1.png') or bool_find_small_image('data/a2.png') or bool_find_small_image('data/a3.png'):
            break
    Shadow_Castle_num = Shadow_Castle()    
    if Shadow_Castle_num == 0:
        out()
        print('影堡事件bad！')
        numtimes = numtimes + 1
        continue
    else:
        if Shadow_Castle_num != 1:
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
        else:
            if dice() != 2:
                out()
                print('需要大成功的事件未大成功')
                numtimes = numtimes + 1
                continue
        skip(3)
#影堡
    time.sleep(3)
    find_small_image('data/9.png',1)
    time.sleep(2)
    while bool_find_small_image('data/8.png') ==True:
        find_small_image('data/8.png',1)
    for _ in range(10):
        pyautogui.click(1800, 1000)
        time.sleep(1)
        if bool_find_small_image('data/a1.png') or bool_find_small_image('data/a2.png') or bool_find_small_image('data/a3.png'):
            break
    Shadow_Castle_num = Shadow_Castle()    
    if Shadow_Castle_num == 0:
        out()
        print('影堡事件bad！')
        numtimes = numtimes + 1
        continue
    else:
        if Shadow_Castle_num != 1:
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
        else:
            if dice() != 2:
                out()
                print('需要大成功的事件未大成功')
                numtimes = numtimes + 1
                continue
        skip(3)
#影堡第二次
    find_small_image('data/gh1.png',1)
    skip(5)
    find_small_image('data/gh2.png',1)
    skip(3)
    find_small_image('data/gh3.png',1)
    time.sleep(3)
    if bool_find_small_image('data/bad.png'):
        find_small_image('data/badgo.png',1)
    elif bool_find_small_image('data/good.png'):
        find_small_image('data/goodgo.png',1)
    skip(3)
#鬼火
    time.sleep(3)
    find_small_image('data/9.png',1)
    time.sleep(2)
    while bool_find_small_image('data/8.png') ==True:
        find_small_image('data/8.png',1)
    for _ in range(10):
        pyautogui.click(1800, 1000)
        time.sleep(1)
        if bool_find_small_image('data/a1.png') or bool_find_small_image('data/a2.png') or bool_find_small_image('data/a3.png'):
            break
    Shadow_Castle_num = Shadow_Castle()    
    if Shadow_Castle_num == 0:
        out()
        print('影堡事件bad！')
        numtimes = numtimes + 1
        continue
    else:
        if Shadow_Castle_num != 1:
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
        else:
            if dice() != 2:
                out()
                print('需要大成功的事件未大成功')
                numtimes = numtimes + 1
                continue
        skip(3)
#影堡第三次
    zsp_bool = False
    time.sleep(3)
    #是否成功获得镯子
    find_small_image('data/cm1.png',1)
    skip(3)
    if bool_find_small_image('data/cm2.png') == True:
        zsp_bool = True
        find_small_image('data/cm2.png',1)
        if dice() == 1:
            out()
            print('骰子用尽')
            numtimes = numtimes + 1
            continue
        skip(3)
    #成功刷到镯子事件
    else:
        skip(4)
        pyautogui.click(957, 474)
        time.sleep(3)
        if bool_find_small_image('data/bad.png'):
            find_small_image('data/badgo.png',1)
        elif bool_find_small_image('data/good.png'):
            find_small_image('data/goodgo.png',1)
        skip(3)
    #未刷到镯子事件
#尘民广场第一次
    find_small_image('data/cm1.png',1)
    skip(3)
    if bool_find_small_image('data/cm2.png') == True:
        zsp_bool = True
        find_small_image('data/cm2.png',1)
        if dice() == 1:
            out()
            print('骰子用尽')
            numtimes = numtimes + 1
            continue
        skip(3)
    #成功刷到镯子事件
    else:
        skip(4)
        pyautogui.click(957, 474)
        time.sleep(3)
        if bool_find_small_image('data/bad.png'):
            find_small_image('data/badgo.png',1)
        elif bool_find_small_image('data/good.png'):
            find_small_image('data/goodgo.png',1)
        skip(3)
    #未刷到镯子事件
#尘民广场第二次
    time.sleep(3)
    find_small_image('data/jmq1.png',1)
    find_small_image('data/jmq0.png',1)
    #容错
    skip(16)
    pyautogui.click(957, 474)
    skip(5)
    time.sleep(3)
    if bool_find_small_image('data/bad.png'):
        find_small_image('data/badgo.png',1)
    elif bool_find_small_image('data/good.png'):
        find_small_image('data/goodgo.png',1)
    skip(5)
#居民区
    if bool_find_small_image('data/cm1.png') == True:
        find_small_image('data/cm1.png',1)
        skip(3)
        if bool_find_small_image('data/cm2.png') == True:
            zsp_bool = True
            find_small_image('data/cm2.png',1)
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
            skip(3)
        #成功刷到镯子事件
        else:
            skip(4)
            pyautogui.click(957, 474)
            time.sleep(3)
            if bool_find_small_image('data/bad.png'):
                find_small_image('data/badgo.png',1)
            elif bool_find_small_image('data/good.png'):
                find_small_image('data/goodgo.png',1)
            skip(3)
        #未刷到镯子事件
#尘民广场第三次 有概率无法进入
    if bool_find_small_image('data/shz1.png') == True:
        time.sleep(3)
        shz_bool = False
        #是否成功获得拾荒者道具
        find_small_image('data/shz1.png',1)
        skip(6)
        if bool_find_small_image('data/shz2.png'):
            find_small_image('data/shz2.png',1)
            shz_bool = True
            skip(4)
        #获得拾荒者道具
        else:
            skip(6)
            pyautogui.click(957, 474)
            skip(4)
        #未获得拾荒者道具
#拾荒者第一次 概率无法进入
    if bool_find_small_image('data/shz1.png') == False:
        if shz_bool == False:
            out()
            print('拾荒者事件bad！')
            numtimes = numtimes + 1
            continue
    #判断是否可以进入拾荒者营地，如果无法进入，判断是否获得拾荒者道具
    else:
        find_small_image('data/shz1.png',1)
        skip(6)
        if bool_find_small_image('data/shz2.png'):
            find_small_image('data/shz2.png',1)
            shz_bool = True
            skip(4)
        #获得拾荒者道具
        else:
            skip(6)
            pyautogui.click(957, 474)
            skip(4)
        #未获得拾荒者道具
        if shz_bool == False:
            out()
            print('拾荒者事件bad！')
            numtimes = numtimes + 1
            continue
#拾荒者第二次 同时判断拾荒者事件是否完成
    if bool_find_small_image('data/cm1.png') == True:
        find_small_image('data/cm1.png',1)
        skip(3)
        if bool_find_small_image('data/cm2.png') == True:
            zsp_bool = True
            find_small_image('data/cm2.png',1)
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
            skip(3)
        #成功刷到镯子事件
        else:
            skip(4)
            pyautogui.click(957, 474)
            time.sleep(3)
            if bool_find_small_image('data/bad.png'):
                find_small_image('data/badgo.png',1)
            elif bool_find_small_image('data/good.png'):
                find_small_image('data/goodgo.png',1)
            skip(3)
        #未刷到镯子事件
#尘民广场第三次 如果前面只进两次，有概率现在可以进入
    if zsp_bool == False:
        out()
        print('尘民广场事件bad！')
        numtimes = numtimes + 1
        continue
#判断尘民广场事件是否完成
    time.sleep(3)
    find_small_image('data/wc1.png',1)
    find_small_image('data/wc10.png',1)
    #容错
    skip(3)
    time.sleep(6)
    find_small_image('data/wcpass.png',1)
    time.sleep(6)
    skip(3)
    time.sleep(3)
    find_small_image('data/wc2.png',1)
    find_small_image('data/wc20.png',1)
    #容错
    skip(3)
    if bool_find_small_image('data/wcgood.png')==True:
        find_small_image('data/wcgood.png',2)
        if dice() == 1:
            out()
            print('骰子用尽')
            numtimes = numtimes + 1
            continue
        else:
            time.sleep(3)
            skip(3)
    else:
        out()
        print('王城事件bad！')
        numtimes = numtimes + 1
        continue
#王城两次
    time.sleep(3)
    find_small_image('data/sd0.png',1)
    find_small_image('data/sd.png',1)
    #容错
    time.sleep(3)
    skip(4)
    pyautogui.click(957, 474)
    skip(6)
    pyautogui.click(957, 474)
    skip(14)
#神殿
    if bool_find_small_image('data/sjs.png') == False or bool_find_small_image('data/sjs0.png') == False:
        out()
        print('步数不够！无法进入世界之树！')
        numtimes = numtimes + 1
        continue
    else:
        find_small_image('data/sjs.png',1)
        find_small_image('data/sjs0.png',1)
        #容错
        time.sleep(3)
        skip(4)
        if bool_find_small_image('data/sjsgood.png') == True:
            find_small_image('data/sjsgood.png',1)
            if dice() == 1:
                out()
                print('骰子用尽')
                numtimes = numtimes + 1
                continue
            else:
                time.sleep(3)
                skip(4)
        elif:
            out()
            print('世界树事件bad！')
            numtimes = numtimes + 1
            continue
#世界树
    time.sleep(3)
    find_small_image('data/boss.png',1)
    find_small_image('data/boss0.png',1)
    #容错
    skip(4)
    find_small_image('data/boss1.png',1)
    skip(6)
    skip(4)
    time.sleep(6)
    find_small_image('data/boss2.png',1)
    skip(4)
    skip(4)
    print('完整运行！')
    break