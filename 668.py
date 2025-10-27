import streamlit as st

# 先放侧边栏导航框架代码
if 'page' not in st.session_state:
    st.session_state.page = "首页"

# 简化的自定义样式
st.markdown("""
<style>
    .nav-btn {padding: 0.7rem; border-radius: 4px; text-align: left; width: 100%;}
    .nav-btn:hover {background: #e6e9ed;}
    .nav-btn.active {background: #e0f2fe; border-left: 3px solid #0ea5e9; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# 侧边栏导航
with st.sidebar:
    pages = ["🐈哈基米 - 数字档案", "折线图", "图片播放器", "音乐播放器", "视频播放器","个😺简历生成"]
    for p in pages:
        if st.button(p, key=p, use_container_width=True):
            st.session_state.page = p

# 动态高亮当前选中项
st.markdown(f"""
<script>
    document.querySelectorAll('.nav-btn').forEach(b => b.classList.remove('active'));
    document.querySelector('button[aria-label="{st.session_state.page}"]').classList.add('active');
</script>
""", unsafe_allow_html=True)


# 2. 再放你的页面内容代码（根据当前选中的页面显示对应的内容）
st.header(st.session_state.page)

if st.session_state.page == "🐈哈基米 - 数字档案":
    # 这里插入你已经写好的“首页”代码
    # 例如：
    
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
    image_path = "IMG20251020_114310.png"
    hzf.image(image_path, caption="D盘JPG图片展示", use_column_width=True)
    hzf.markdown("---")
    hzf.markdown("**下一次任务预警：** :red[中午到底吃什么！！！]  \n**最后更新：** 2025-10-20  \n**系统状态：** 离线🙀 | 困意暴增 | 随时睡觉")


elif st.session_state.page == "折线图":
    # 这里插入已经写好的“个人简历生成器”代码
    # 例如：
    st.write("折线图生成器功能：")
    name = st.text_input("姓名")
    import streamlit as st
    import pandas as pd

# 准备南宁西乡塘5家门店数据
    data = {
    '西乡塘老友粉店': [12,13,14,15,14,13],
    '螺蛳粉': [10,11,12,13,12,11],
    '农院路酸嘢铺': [8,9,10,11,10,9],
    '蛙小侠': [6,7,8,9,8,7],
    '生榨粉': [9,10,11,12,11,10]
    }

# 创建DataFrame
    df = pd.DataFrame(data)
    df.index = pd.Series(['01月','02月','03月','04月','05月','06月'], name='月份')

# 展示数据
    st.dataframe(df)

# 折线图
    st.line_chart(df)
# 柱状图
    st.bar_chart(df)
# 面积图
    st.area_chart(df)

# 西乡塘门店地图数据
    map_data = {
    'latitude': [22.832173,22.839952,22.785994,22.790267,22.857511],
    'longitude': [108.286460,108.246231,108.252411,108.313866,108.341503]
    }
    st.map(pd.DataFrame(map_data))



    
    

elif st.session_state.page == "图片播放器":
    # 其他未完成的页面（暂时显示占位内容）
    st.write("动物图鉴内容：")

    import streamlit as st

    st.set_page_config(page_title="快乐",page_icon="😊" )

    images = [
    {'url':'https://vip.123pan.cn/1821652950/123pan/123panlikebizhi/231223004004.jpg',
     'parm':'熊出没'},
    {'url':'https://wenhui.whb.cn/u/cms/www/202011/19152600az6b.jpg',
     'parm':'猫和老鼠'},
    {'url':'https://wallpaperaccess.com/full/36372.jpg',
     'parm':'洞庭湖边'},
    {'url':'https://img.52desk.com/tp/2325053sNh5.jpg',
     'parm':'懒洋洋'}
    ]

    if 'ind' not in st.session_state:
        st.session_state.ind = 0

    def next_img():
        st.session_state.ind = (st.session_state.ind + 1) % len(images)

    def prev_img():
        st.session_state.ind = (st.session_state.ind - 1) % len(images)


    st.image(images[st.session_state['ind']]['url'],caption=images[st.session_state['ind']]['parm'])


    c1, c2 = st.columns(2)
    with c1:
        st.button("上一张", on_click=prev_img)
    with c2:
        st.button("下一张", on_click=next_img)

elif st.session_state.page == "音乐播放器":
    import streamlit as st

    st.set_page_config(page_title="音乐播放器", page_icon='🎵')

    music = [
        {
            'title': '我知道',
            'artist': 'BY2',
            'duration': '3:46',
            'audio_file': 'https://music.163.com/song/media/outer/url?id=2643537823.mp3',
            'photo': 'https://p1.music.126.net/icdfSZmawPHdYCkQB-E-RA==/109951163200171219.jpg'
        },
        {
            'title': '像晴天像雨天',
            'artist': '江苏泷',
            'duration': '3:11',
            'audio_file': 'https://music.163.com/song/media/outer/url?id=268458378.mp3',
            'photo': 'https://p2.music.126.net/gN6htv5E9WwyOoTASMuvDQ==/109951170483576228.jpg'
        },
        {
            'title': '有些',
            'artist': '粉笔',
            'duration': '2:18',
            'audio_file': 'https://music.163.com/song/media/outer/url?id=2604234517.mp3',
            'photo': 'https://p2.music.126.net/rs_lGvUgkttfbO1YsgsrVg==/109951169743264606.jpg'
        }
    ]

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0

    def next_song():
        st.session_state['ind'] = (st.session_state['ind'] + 1) % len(music)

    def prev_song():
        st.session_state['ind'] = (st.session_state['ind'] - 1) % len(music)

    a1, a2 = st.columns([1, 2], gap='large')

    with a1:
        st.image(
            music[st.session_state['ind']]['photo'],
            use_container_width=True,  
            caption=f"当前播放：{music[st.session_state['ind']]['title']}"
        )

    with a2:
        st.subheader(music[st.session_state['ind']]['title'], divider='blue')
        st.write(f"歌手：{music[st.session_state['ind']]['artist']}")
        st.write(f"时长：{music[st.session_state['ind']]['duration']}")
    
        st.audio(
            music[st.session_state['ind']]['audio_file'],
            format='audio/mp3',
            autoplay=True
        )

    c1, c2 = st.columns(2, gap='small')

    with c1:
        st.button(
            '上一首 ←',  
            on_click=prev_song,
            use_container_width=True
        )

    with c2:
        st.button(
            '下一首 →',  
            on_click=next_song,
            use_container_width=True
        )

    st.caption('-----')
    st.caption('本播放器仅用于学习交流，所有音乐版权归原作者所有')
    






elif st.session_state.page == "视频播放器":
    st.write("数字档案管理：")
    
    import streamlit as st
    st.set_page_config(page_title='视频网站',page_icon='🎞')
    videos = [
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/93/18/25882531893/25882531893-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&trid=c569ab04b83b4eefb46a7d6c348b8e3h&deadline=1761305230&nbs=1&platform=html5&mid=0&oi=771356656&gen=playurlv3&os=cosovbv&og=hw&upsig=9803e484c920e20da6d82a74be45aaab&uparams=e,uipk,trid,deadline,nbs,platform,mid,oi,gen,os,og&bvc=vod&nettype=0&bw=806013&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
            'title': '【驯龙高手2】插曲《Where No One Goes》',
            'episode': '主题'
        },
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/60/00/1135210060/1135210060-1-208.mp4?e=ig8euxZM2rNcNbhVhbdVhwdlhzdghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1761302451&nbs=1&os=cosovbv&mid=0&oi=771356656&uipk=5&platform=html5&trid=21dd36fe9a1043d59b1495bcd3d8cf4h&gen=playurlv3&og=hw&upsig=c9f272d6ab9f392b5312eda212c607e1&uparams=e,deadline,nbs,os,mid,oi,uipk,platform,trid,gen,og&bvc=vod&nettype=0&bw=2417062&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
            'title': '猫抓老鼠',
            'episode': '治愈'
        },
        {
            'url': 'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/15/34/1285573415/1285573415-1-192.mp4?e=ig8euxZM2rNcNbRBhbdVhwdlhWUghwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=771356656&mid=0&nbs=1&gen=playurlv3&og=hw&platform=html5&deadline=1761302717&trid=a029318ba79a480681a867610994c74h&os=cosovbv&uipk=5&upsig=16a3441f4be315a9c9cea9c8f7614064&uparams=e,oi,mid,nbs,gen,og,platform,deadline,trid,os,uipk&bvc=vod&nettype=0&bw=1221273&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
            'title': '【时光音乐会】G.E.M.邓紫棋《唯一》',
            'episode': '演唱会'
        }
    ]

    if 'ind' not in st.session_state:
        st.session_state['ind'] = 0
    st.title( videos[st.session_state['ind']]['title']+'-第' + videos[st.session_state['ind']]['episode']+'片段')
# 显示视频介绍
    st.write("**剧情介绍：**", videos[st.session_state['ind']]['title'])

    st.video(videos[st.session_state['ind']]['url'])
    
    c1, c2, c3 = st.columns(3)

    def play(arg):
        st.session_state['ind'] = int(arg)

    for i in range (len(videos)):
        st.button('第'+str(i+1)+'片段',use_container_width=True,on_click=play,args=([i]))









elif st.session_state.page == "个😺简历生成":
    
    
    import streamlit as st

    st.set_page_config(page_title="个😺简历生成器", page_icon="", layout="wide")

# 页面设置
   

# 左右分栏：左侧输入，右侧预览
    c1,c2 = st.columns([1,2])

    with c1:
        st.subheader("个😺信息表单")
    
    # 基本信息
        name = st.text_input("哈基米名称😺：")
        gender = st.radio("性别", ["男", "女"])
        age = st.number_input("年龄", min_value=18, max_value=60, step=1)
        phone = st.text_input("电话")
        email = st.text_input("邮箱")
    
    # 求职信息
        job = st.text_input("期望职位")
        salary = st.slider("期望薪资(元/月)", 3000, 50000, 10000, step=1000)
    
    # 个人简介
        intro = st.text_area("个人简介", height=100)
        
    # 专业技能
        skills = st.multiselect("专业技能", 
                           ["睡觉", "吃饭", "打瓦", "跑刀", "干农活", "偷吃"])
        exp = st.slider("工作经验(年)", 0, 20, 3)

   
        start_color, end_color = st.select_slider(
        '选择波长的颜色范围',
        options = ['吃饭', '打瓦😼', '干农活', '跑刀😼', '睡觉🐼', '哈气', '发呆'],
        value=('吃饭', '睡觉🐼'))


        st.subheader("你爱咪🐱还是汪🐕")
        my_range = range(1, 21)

        numbers = st.select_slider('选择你的心动值😻', options=my_range, value=5)


# 自定义format_func函数
        def my_format_func(option):
           return f'{option}'

        options_1 = st.multiselect(
        '选择你的午饭😻',
        ['烧鸭饭', '西安面馆', '重庆小面', 'KFC', '麦当当', '河南面馆'],
        ['烧鸭饭', 'KFC'],
        format_func=my_format_func,
        )




        photo = st.file_uploader("上传咪的图片")

        if photo is not None:
    
          bytes_data = photo.getvalue()
          st.image(bytes_data)
     
    




    with c2:
        st.subheader("简历预览")
   
    # 预览姓名
        st.header(name if name else "姓名")

    
  
    # 基本信息预览
        st.write(f"性别：{gender} | 年龄：{age}")
        st.write(f"电话：{phone} | 邮箱：{email}")
        
    # 求职信息预览
        st.subheader("求职意向")
        st.write(f"期望职位：{job if job else '未填写'}")
        st.write(f"期望薪资：{salary}元/月")
    
    # 个人简介预览
        st.subheader("个咪简介😼")
        st.write(intro if intro else "要是每个人都懂咪，那咪岂不是太普通了😼：")
    
    # 技能与经验预览
        st.subheader("专业技能")
        st.write(", ".join(skills) if skills else "未填写")
        st.write(f"工作经验：{exp}年")

        st.write('你的选择介于', start_color, '和', end_color, '之间')


        st.write('你选择了 %s 个心动' % numbers, numbers * ":hearts:")


        st.write('午饭是:', options_1)

        st.header('请选择您的英雄')
        st.subheader('哈基米曼波')
        city = st.selectbox('哈基米突击：', ['橘', 'Three花', '梨花'], format_func=my_format_func, index=2)
# 根据返回值不同，选择不同的特色回答
# 同时应注意返回值不受自定义my_format_func
        if city == '橘':
            st.write('圆头圆脑圆肚皮，我真的羡慕我自己🐱')
        elif city == 'Three花':
            st.write('姐就是女王，自信放光芒😽')
        else:
            st.write('你那软绵绵的咪就别配这么硬的曲了😼”')


        st.header('等下中午吃什么🙀')
        st.subheader('哈基米？？？')

    







    

    
