import streamlit as st 
import time
# from streamlit_extras.stylable_container import stylable_container

# When open it shows balloons
# st.balloons()

st.title("Sentiment Analysis Web App")
st.subheader("Welcome to the Sentiment Analysis Tool")


#----------------------------------------------------------------------------
### Download Model to local drive
import streamlit as st
import boto3
import os

s3 = boto3.client("s3")
bucket_name = 'mlops-tinybert-sentimentanalysis'
local_path = 'mlops-tinybert-sentimentanalysis/'
s3_prefix = 'ml_model/'

os.makedirs(local_path, exist_ok=True)

def download_dir(local_path, s3_prefix):
    paginator = s3.get_paginator('list_objects_v2')
    objects_found = False # Track if objects are found

    try:
        for result in paginator.paginate(Bucket = bucket_name, Prefix = s3_prefix):
            if 'Contents' in result:
                objects_found = True  # Set to True when objects are found
                for key in result['Contents']:
                    s3_key = key['Key']
                    local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))

                    # Ensuring subdirectory exist for the file
                    os.makedirs(os.path.dirname(local_file), exist_ok=True)

                    # Attempt the file download
                    try:
                        s3.download_file(bucket_name, s3_key, local_file)
                        print(f"Downloaded {s3_key} to {local_file}")
                    
                    except PermissionError as e:
                        print(f"Permission denied for file {local_file}: {e}")
    except Exception as e:
        print(f"Error during download: {e}")
    
    if not objects_found:
            st.warning("No files found at the specified S3 prefix. Please verify the prefix.")
    
#Create download button and link to download.
download_button = st.button('Download Model')

if download_button:
    with st.spinner("Downloading... please wait..."):
        download_dir(local_path, s3_prefix)
    

#----------------------------------------------------------------------------

import torch
from transformers import pipeline

# Input text box
user_text = st.text_area(label="Please enter text below...", label_visibility="visible")

# Analyze and clear buttons
col1, col2 = st.columns(2)
analyze_button = col1.button("Analyze Sentiment")
clear_button = col2.button("Clear")

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
classifier = pipeline('text-classification', model='mlops-tinybert-sentimentanalysis', device = device)
output = classifier(user_text)



# Check if analyze button is clicked
if analyze_button:
    # If there is text, analyze the sentiment or no text is provided, show the warning and image
    if user_text:
        with st.spinner("Working on the input..."):
            time.sleep(0.5)
            st.toast("Analysis completed")
            time.sleep(0.5)
            st.info("Sentiment analysis complete. 👇👇👇")
            time.sleep(0.5)
            st.write(output)
    
    else:
        st.warning("I am speechless here 😶. Please provide some text to analyze sentiment.")
        st.image("https://th.bing.com/th/id/OIP.xqHR0bxoLZeRA1xO_xM41wHaFx?rs=1&pid=ImgDetMain", width=200)