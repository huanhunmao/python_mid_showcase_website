import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')
col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')  # 确保路径指向实际的图像文件

with col2:
    st.title('Marxu')
    content = """Hello, I am Marxu"""  # 修正拼写错误

    st.info(content)

# content = """dajsjdas ajsd adasd asd ajsdjajsdjasd """
#
# st.write(content)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('data.csv', sep=';')

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        print(row['title'])
        st.header(row['title'])
        st.write(row['description'])
        st.image('images/' + row['image'])
        st.write(f"[Source code]({row['url']})")