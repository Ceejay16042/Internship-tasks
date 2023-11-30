import streamlit as st
import time
import io
import base64
from streamlit_option_menu import option_menu
import cv2
from io import BytesIO
from PIL import Image
import numpy as np

#function to download image to local storage
def download_image():
    st.write('Generating Image download link, please wait...')
    time.sleep(5)
    image_stream = io.BytesIO()
    pil_image.save(image_stream, format="JPEG")

    # Convert the BytesIO object to a base64 string
    image_base64 = base64.b64encode(image_stream.getvalue()).decode()

    # Display a link to download the image
    st.markdown(
        f'<a href="data:image/jpeg;base64,{image_base64}" download="captured_image.jpg">Download Image</a>',
        unsafe_allow_html=True
    )


#function to capture frames from webcam
def capture_camera_frame():
    # Placeholder for displaying the captured frame
    image_placeholder = st.empty()
    return image_placeholder


# Function to convert OpenCV image to PIL image and enable realtime image capture
def display_realtime_camera():
     global pil_image
     cap = cv2.VideoCapture(0)
     # Read a frame from the camera
     _, frame = cap.read()
     # Convert the OpenCV frame to a PIL image
     pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
     # Display the image in the Streamlit app
     capture_camera_frame().image(pil_image, use_column_width=True)

#text instructions
def text_instructions():
    st.header("Text Instructions")
    instructions = """
    1. Pay attention to the simulated camera feed.
    2. Observe the GIF for additional information.
    3. Follow the text instructions below.
    """
    st.markdown(instructions)
#program to display a GIF Image
def display_gif():
    # global pil_image
    st.title("Placeholder for GIF Image")
    # speed = st.slider("GIF Speed", min_value=0.1, max_value=2.0, value=1.0, step=0.1)
    gif_url = "https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif"
    st.image(gif_url, use_column_width=True)

def main():

    if 'clicked' not in st.session_state:
        st.session_state.clicked = False
   
   #sidebar menu     
    with st.sidebar:
        navbar_menu = option_menu(
            menu_title="Menu page",
            options=['ImageCapture', 'Registration_Page'],
            icons=["camera", "account"],
            menu_icon='cast',
            default_index=0,
            orientation = "horizontal"
        )

#Registration_page menu
    if navbar_menu == 'Registration_Page':
        st.title(":violet[Welcome to the Registration page]")
        Name = st.text_input('Name')
        Gender = st.text_input('Gender')
        Age = st.text_input('Age')
        Phone_number = st.text_input('Phone')
        Aadhar = st.text_input('Aadhar')
        login = st.button('Register')

#Image capture option menu
    elif navbar_menu == 'ImageCapture':
        display_gif()
        text_instructions()
        display_realtime_camera()
        download_button = st.button('download')
        

#Adding an event listener to trigger the download of the real-time image when the download button is toggled.
        if download_button:
            st.session_state.clicked = True
            download_image()
            
            
            #button to proceed to second image capture
        if st.button("Proceed to Second Image Capture"):
            st.header("Second Image Capture")
            display_realtime_camera()
            download_buttonn = st.button('Downloadd')
            download_image()

        if st.button('Proceed to Thank You Screen!'):
            st.header('Thank You!')
            st.write("Thank you for using our simulated camera feed app. Have a great day")
            
            #Button to Proceed to Thank You Screen
                # if st.button("Proceed to Thank You Screen"):
                #     st.header("Thank You!")
                #     st.write("Thank you for using our simulated camera feed app. Have a great day!")

    else:
        st.write('You have not selected an option')

#crosschecks if the python program is been run in the main program and executes if true
if __name__ == '__main__':
    main()