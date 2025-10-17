import streamlit as st
import cv2
import numpy as np
from PIL import Image


def denoise_image(image, method='Median', kernel_size=5):
    if method == 'Mean':
        return cv2.blur(image, (kernel_size, kernel_size))
    elif method == 'Median':
        if kernel_size % 2 == 0:
            kernel_size += 1
        return cv2.medianBlur(image, kernel_size)
    elif method == 'Gaussian':
        if kernel_size % 2 == 0:
            kernel_size += 1
        return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return image

def sharpen_image(image):
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1,  9, -1],
                                  [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)
    return sharpened_image

def detect_edges(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sobelx = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    sobel_combined = cv2.magnitude(sobelx, sobely)
    sobel_combined = np.uint8(sobel_combined)

    kernelx = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernely = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    prewittx = cv2.filter2D(gray_image, -1, kernelx)
    prewitty = cv2.filter2D(gray_image, -1, kernely)
    prewitt_combined = cv2.add(prewittx, prewitty)

    canny_edges = cv2.Canny(gray_image, threshold1=100, threshold2=200)

    return sobel_combined, prewitt_combined, canny_edges

st.set_page_config(layout="wide")
st.title("Image Enhancing Tool")

st.sidebar.title("Control Panel")
uploaded_file = st.sidebar.file_uploader("Upload a color image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    original_image_bgr = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    original_image_rgb = cv2.cvtColor(original_image_bgr, cv2.COLOR_BGR2RGB)

    st.header("Original Image")
    st.image(original_image_rgb, caption='Uploaded Image', width='stretch')

    st.markdown("---")

    st.header("1. Denoising / Smoothing")

    denoise_method = st.selectbox(
        "Select denoising algorithm:",
        ('Mean', 'Median', 'Gaussian')
    )
    kernel_size_denoise = st.slider("Select Kernel Size:", 3, 21, 5, step=2)

    denoised_img_bgr = denoise_image(original_image_bgr, denoise_method, kernel_size_denoise)
    denoised_img_rgb = cv2.cvtColor(denoised_img_bgr, cv2.COLOR_BGR2RGB)

    col1, col2 = st.columns(2)
    with col1:
        st.image(original_image_rgb, caption='Original Image', width='stretch')
    with col2:
        st.image(denoised_img_rgb, caption=f'Image after Denoising ({denoise_method})', width='stretch')


    st.markdown("---")

    st.header("2. Sharpening")
    sharpened_img_bgr = sharpen_image(original_image_bgr)
    sharpened_img_rgb = cv2.cvtColor(sharpened_img_bgr, cv2.COLOR_BGR2RGB)

    col3, col4 = st.columns(2)
    with col3:
        st.image(original_image_rgb, caption='Original Image', width='stretch')
    with col4:
        st.image(sharpened_img_rgb, caption='Image after Sharpening', width='stretch')

    st.markdown("---")

    st.header("3. Edge Detection")
    sobel, prewitt, canny = detect_edges(original_image_bgr)

    st.write("The resulting images show edges detected by three different filters:")

    col5, col6, col7 = st.columns(3)
    with col5:
        st.image(sobel, caption='Sobel Filter', width='stretch')
    with col6:
        st.image(prewitt, caption='Prewitt Filter', width='stretch')
    with col7:
        st.image(canny, caption='Canny Edge Detector', width='stretch')

else:
    st.info("Please upload an image to get started.")
    
    
    