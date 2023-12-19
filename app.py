import streamlit as st

# Define the images and initial variables
images = [
    'https://i.imgur.com/37gItE1_d.webp?maxwidth=760&fidelity=grand',
    'https://i.imgur.com/oykl4LU.jpg',
    'https://www-megabad-com-res.cloudinary.com/image/upload/q_auto:good/fl_progressive/f_auto/hersteller-hansgrohe-axor-starck-v-einhebel-731060',
    'https://i.imgur.com/PTavudA.jpg',
    'https://i.imgur.com/TOq6yzn.jpg',
    'https://i.imgur.com/Az68b7B.jpg',
    'https://i.imgur.com/cIsAXfS.jpg',
    'https://i.imgur.com/htBYxea.jpg',
    'https://i.imgur.com/PKu2X4u.jpg',
    'https://www-megabad-com-res.cloudinary.com/image/upload/q_auto:good/fl_progressive/f_auto/hersteller-geberit-badkeramik-bambini-armaturen-einhebel-2629504'
]
current_image_index = 0
smashes = 0
passes = 0
choices = []

# Streamlit app layout
st.title("Smash or Pass")

# Button functionalities inside a loop
while current_image_index < len(images):
    st.image(images[current_image_index])
    
    if st.button("Smash"):
        smashes += 1
        choices.append('Smash')
        current_image_index += 1

    if st.button("Pass"):
        passes += 1
        choices.append('Pass')
        current_image_index += 1

# Show results
st.header("Results:")
st.write(f"Smashes: {smashes}")
st.write(f"Passes: {passes}")
st.subheader("Overview:")
for i in range(len(images)):
    st.image(images[i])
    st.write(choices[i])