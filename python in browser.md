<h1>How We Can Run Python In Browser</h1><br>
<h1>To Run Python In Browser We Use The Streamlit</h1><br>
<h1>Command to install Streamlit</h1><br>
        
    pip install streamlit
<h1>How to Import streamlit </h1>

    import streamlit as st
<h2>Command To run file</h2><br>
    
    streamlit run first_app.py
<h2>Codes Of Streamlit</h2><br>

    st.button("Click me")
    st.download_button("Download file", data)
    st.feedback("thumbs")
    st.link_button("Go to gallery", url)
    st.page_link("app.py", label="Home")
    st.data_editor("Edit data", data)
    st.checkbox("I agree")
    st.toggle("Enable")
    st.radio("Pick one", ["cats", "dogs"])
    st.selectbox("Pick one", ["cats", "dogs"])
    st.multiselect("Buy", ["milk", "apples", "potatoes"])
    st.slider("Pick a number", 0, 100)
    st.select_slider("Pick a size", ["S", "M", "L"])
    st.text_input("First name")
    st.number_input("Pick a number", 0, 10)
    st.text_area("Text to translate")
    st.date_input("Your birthday")
    st.time_input("Meeting time")
    st.file_uploader("Upload a CSV")
    st.camera_input("Take a picture")
    st.color_picker("Pick a color")

<h1>How To Make Title</h1><br>

    st.title("Login Page")
<h2>To Write This Code Import Streamlit As st</h2><br>
<h2>How To Make Input Box</h2><br>

    username = st.text_input("Username")
<h1>How To Display Media On The Wabpage Using Python</h1><br>

    st.image("./header.png")
    st.audio(data)
    st.video(data)
    st.video(data, subtitles="./subs.vtt")
    st.logo("logo.jpg")
