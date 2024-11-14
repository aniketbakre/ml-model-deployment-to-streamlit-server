import streamlit as st
import time
from PIL import Image

#----------------------------------------------------------------------------
### Download Model to local drive
# import os
import boto3

# AWS S3 client
s3 = boto3.client('s3')

# Define bucket name (ensure this is set to your actual bucket name)
bucket_name = 'mlops-tinybert-sentimentanalysis'

to_download_file_path = 'mlops-tinybert-sentimentanalysis'
s3_prefix = 'ml-models/mlops-tinybert-sentimentanalysis' 


def download_dir(to_download_file_path, s3_prefix):
    # Create the local directory if it does not exist
    os.makedirs(to_download_file_path, exist_ok=True)

    # Create a paginator to handle the list of objects in the S3 bucket
    paginator = s3.get_paginator('list_objects_v2')

    # Iterate through the paginated list of objects in the specified bucket and prefix
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if 'Contents' in result:  # Ensure there are objects under the prefix
            for key in result['Contents']:
                s3_key = key['Key']  # Extract the S3 object key

                # Local file path where the S3 file will be downloaded
                local_file = os.path.join(to_download_file_path, os.path.basename(s3_key))
                
                # Create local directories if they don't exist
                os.makedirs(os.path.dirname(local_file), exist_ok=True)

                # Download the file from S3 to the local directory
                s3.download_file(bucket_name, s3_key, local_file)
download_button = st.button('Download Model')

if download_button:
    download_dir(to_download_file_path, s3_prefix)



# Call the function to download files from S3
download_dir(to_download_file_path, s3_prefix)

#----------------------------------------------------------------------------

st.title("Machine Learning Model Deployment at the Server") # For title
st.header("***My first app: on the streamlit!!!***") # For header
st.subheader("*I am the boss*") # For sub header
st.button(label="Download", key="key")

input = st.text_input(label="Text here", help= " enter your text and pless enter from keyboard")
st.text(input)

st.markdown("---")
input_text = st.text_area("Enter here")
st.text(input_text)

button=st.button("Enter")
if button:
    Image = st.image('https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1txC5L.img?w=768&h=432&m=6&x=333&y=191&s=1098&d=318',width=200)

    st.checkbox("True")

    with st.spinner("please wait"):
        st.write("Model is going to downloat")
        time.sleep(10)
        st.code
st.radio(label="ABC",options=["a","b"])

selection = st.multiselect(label="ABC",options=["a","b"])
st.write(selection)