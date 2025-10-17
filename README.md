# Image Enhancement Web App

A simple yet powerful web application built with Streamlit and OpenCV to perform fundamental image enhancement tasks in real-time. This tool allows users to upload an image and apply various filters for denoising, sharpening, and edge detection.

<img width="1914" height="907" alt="Image" src="https://github.com/user-attachments/assets/9e909016-eade-40bd-8107-ddf06cae318c" />

## Features

-   **Image Upload**: Upload your own color images (`.jpg`, `.jpeg`, `.png`).
-   **Denoising / Smoothing**:
    -   Apply **Mean**, **Median**, and **Gaussian** filters.
    -   Interactively adjust the kernel size with a slider for real-time results.
-   **Sharpening**:
    -   Enhance image details and edges with a single click using a convolution kernel.
-   **Edge Detection**:
    -   Visualize edges using three popular algorithms:
        -   **Sobel** filter
        -   **Prewitt** filter
        -   **Canny** edge detector
-   **Interactive UI**: A clean and user-friendly interface that displays the original and processed images side-by-side for easy comparison.

---

## Tech Stack

-   **Python**
-   **Streamlit**: For building and deploying the interactive web application.
-   **OpenCV-Python**
-   **NumPy**

---

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/quocnhut134/Image_Enhancing_Tool.git
    ```

2.  **Install the required dependencies:**
    ```bash
    pip install streamlit opencv-python numpy
    ```
    Or, you can install them in the `requirements.txt` file above:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

1.  **Run the Streamlit app:**
    Navigate to the project directory in your terminal and run the following command:
    ```bash
    streamlit run app.py
    ```

2.  **Use the application:**
    -   A new tab will open in your web browser at `http://localhost:8501`.
    -   Use the sidebar to **upload an image file** from your computer.
    -   Once the image is loaded, the processing results will be displayed automatically.
    -   Interact with the widgets in the main panel (e.g., selectbox for denoising method, slider for kernel size) to see the effects in real-time.


## Deployment

You can find and enjoy the deployment web of this application at 'https://imageenhancingtool-zv3dpw58tfhx5ejnuac3tg.streamlit.app/'.
