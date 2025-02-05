import streamlit as st
from PIL import Image
import os

# 确保 "uploads" 目录存在
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Streamlit 标题
st.title("📷 在线图片上传")

# 上传文件
uploaded_file = st.file_uploader("选择图片上传", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ {uploaded_file.name} 上传成功！")

# **实时** 显示所有上传的图片
st.subheader("📸 已上传的图片")
uploaded_files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)  # 按时间倒序排列

# 使用多列布局
col1, col2 = st.columns([3, 1])  # 设置列宽比例

with col1:
    for file in uploaded_files:
        img_path = os.path.join(UPLOAD_FOLDER, file)
        img = Image.open(img_path)
        st.image(img, caption=file, use_column_width=True)

with col2:
    st.markdown("<h4>更多功能即将上线！</h4>", unsafe_allow_html=True)
    st.write("比如：支持评论、点赞等功能，敬请期待！")
