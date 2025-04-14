import streamlit as st
from moondreamlib import MoonDreamInitialize
from PIL import Image

#Initial page configuration
st.set_page_config(
    page_title="MoonDream",
    page_icon="🌙",
    layout="wide"
)

# Title and description
st.title("MoonDream")       
st.write("Welcome to the MoonDream app!")
st.write("This app allows you to generate captions for images and ask questions about them.")

@st.cache_resource
def get_moondream():
    return MoonDreamInitialize(api_key=st.secrets["moondream_api_key"])

moondream = get_moondream()

def upload_image():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"],key=page)
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="This is the Uploaded Image", use_column_width=True)
        return image 
    return None


# Sidebar for user input
st.sidebar.title("Do Magic with MoonDream 🔮")
page = st.sidebar.radio("Select a page", ("Caption Image", "Query Image", "Detect Image"))
#logic for caption the image
if page == "Caption Image":
    st.sidebar.subheader("Caption Image")
    st.title("Caption the Image")
    st.sidebar.write("Upload an image to generate a caption.")
    image = upload_image()
    if image :
        detail=st.radio("Select Caption level", ["normal", "short", "long"],horizontal=True)
        if st.button("Generate Caption"):
            with st.spinner("Generating caption..."):
                caption = moondream.description(image,detail)
                st.success("Caption generated!")
                st.write(caption)
if page =='Query Image':
        st.sidebar.subheader("Query Image")
        st.title("Query the Image")
        st.sidebar.write("Upload an image to ask a question.")
        image = upload_image()
        if image:
            question = st.text_input("Ask your question:",placeholder="How many objecets are there?")
            if st.button("Ask"):
                with st.spinner("Getting answer..."):
                    answer = moondream.query(image, question)
                    st.success("Answer received!")
                    st.write(answer)
if page == "Detect Image":
    st.sidebar.subheader("Detect Image")
    st.title("Detect the Image")
    st.sidebar.write("Upload an image to detect objects.")
    image = upload_image()
    if image:
        st.write("Enter the object to detect (e.g., 'person', 'car', 'dog'). Use lowercase letters.")
        object = st.text_input("Object to detect:", placeholder="person")
        if st.button("Detect"):
            with st.spinner("Detecting objects..."):
                detect = moondream.detect(image, object)
                st.success("Objects detected!")
                st.write(detect)
                st.balloons()

        
