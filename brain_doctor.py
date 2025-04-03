import os

groq_api_key=os.environ.get("groq_api_key")

import base64
image_path="acne.jpg"
image_file=open(image_path,"rb")
encoded_imae=base64.b64encode(image_file.read()).decode('utf-8')

from groq import groq

client=Groq()