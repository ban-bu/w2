import streamlit as st
from PIL import Image
import os

# 确保 "uploads" 目录存在
UPLOAD_FOLDER = "uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Streamlit 标题
st.title("📷 Upload your images")

# 上传文件
uploaded_file = st.file_uploader("Choose the image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"✅ {uploaded_file.name} Upload Successfully！")

# **实时** 显示所有上传的图片（两列布局）
st.subheader("📸 Uploaded Images")
uploaded_files = sorted(os.listdir(UPLOAD_FOLDER), reverse=True)  # 按时间倒序排列

if uploaded_files:
    col1, col2 = st.columns(2)  # 创建两列

    for i, file in enumerate(uploaded_files):
        img_path = os.path.join(UPLOAD_FOLDER, file)
        img = Image.open(img_path)

        # 交替放入左右两列
        if i % 2 == 0:
            with col1:
                st.image(img, caption=file, use_container_width=True)
        else:
            with col2:
                st.image(img, caption=file, use_container_width=True)
