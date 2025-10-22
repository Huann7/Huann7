import streamlit as hzf
import numpy as np
import pandas as pd

hzf.set_page_config(page_title="🐈哈基米 - 数字档案", layout="centered", initial_sidebar_state="collapsed")
hzf.markdown(
    """
    
    """,
    unsafe_allow_html=True
)


hzf.title("🐈哈基米 - 数字档案")


hzf.header(" :red[基础信息]")


hzf.text("代号: 肥波😼")
hzf.text("类型:麦当劳之王 | 形态切换: 干饭型/睡觉型/哈气型")
hzf.text("注册地: 地球")
hzf.text("当前状态:活跃🧬 | 哈基米ID:7878 ")


hzf.header("💿技能矩阵:")


col1, col2, col3 = hzf.columns(3)
with col1:
    hzf.metric(label="😻干饭技能", value="98%", delta="666%")  
with col2:
    hzf.metric(label="🙀睡觉能力", value="92%", delta="-200%")  
with col3:
    hzf.metric(label="😾哈气评级", value="85%", delta="7878% (空中型为99%)")


hzf.header(" ❤喜好")

data = {
    "😻超级喜欢": ["麦香鸡腿堡", "比奇堡", "板烧鸡腿堡"],
    "😻无敌喜欢": ["黑椒鸡块", "超级薯条", "无敌可乐"],
    "😻超级无敌喜欢": ["麦旋风", "双层深海鳕鱼堡", "培根酥脆双层牛肉堡"],
    "😻宇宙超级无敌喜欢": ["安格斯牛肉堡", "巨无霸超级麦辣堡", "简单双人套餐"]

}
df = pd.DataFrame(data)
hzf.table(df)

hzf.header("  最新技能代码")


code = """
def 深渊巨口():
    能量核心 = 胸口水晶充能(100%)
    释放(能量=能量核心, 破坏力=9999)
    return "汉堡已被消灭"

def 形态切换(形态):
    if 形态 == "吃饭型😻":
        速度 = 提升(666%)
        敏捷 = 提升(666%)
    elif 形态 == "睡觉型🙀":
        力量 = 降低(200%)
        防御 = 降低(200%)
    return f"已切换为{形态}"
"""
hzf.code(code, language="python")

hzf.text("附上美图一张💟")
image_path = "D:\\IMG20251020_114310.png"
hzf.image(image_path, caption="D盘JPG图片展示", use_column_width=True)
hzf.markdown("---")
hzf.markdown("**下一次任务预警：** :red[中午到底吃什么！！！]  \n**最后更新：** 2025-10-20  \n**系统状态：** 离线🙀 | 困意暴增 | 随时睡觉")


