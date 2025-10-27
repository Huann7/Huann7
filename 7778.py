import streamlit as st

# 页面设置
st.title("个人简历生成器")

# 左右分栏：左侧输入，右侧预览
c1,c2 = st.columns(2)

with c1:
    st.subheader("个人信息表单")
    
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
                           ["Python", "HTML/CSS", "JavaScript", "SQL", "Excel", "PPT"])
    exp = st.slider("工作经验(年)", 0, 20, 3)

   
    start_color, end_color = st.select_slider(
    '选择波长的颜色范围',
    options=['吃饭', '打瓦😼', '干农活', '跑刀😼', '睡觉🐼', '哈气', '发呆'],
    value=('吃饭', '睡觉🐼'))


    st.subheader("你爱咪🐱还是汪🐕")
my_range = range(1, 21)

numbers = st.select_slider('选择你的心动值😻', options=my_range, value=5)

st.header('等下中午吃什么🙀')
st.subheader('哈基米？？？')
# 自定义format_func函数
def my_format_func(option):
    return f'吃{option}'

options_1 = st.multiselect(
    '选择你的午饭😻',
    ['烧鸭饭', '西安面馆', '重庆小面', 'KFC', '麦当当', '河南面馆'],
    ['烧鸭饭', 'KFC'],
    format_func=my_format_func,
    )








with c2:
    st.subheader("简历预览")
    st.image("https://ts4.tc.mm.bing.net/th/id/OIP-C.5CnLkmtVjLuPnWLjTNd2pAAAAA?rs=1&pid=ImgDetMain&o=7&rm=3",width=100)
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

    st.write('你选择了 ')
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








