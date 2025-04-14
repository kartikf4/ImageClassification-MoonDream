
import moondream as md
import os
from PIL import Image

# Initialize for Moondream Cloud
model = md.vl(api_key ="")

# Load an image
image = Image.open("temple.jpg")

# Generate a caption
caption = model.caption(image)["caption"]
print("Caption:", caption)

# Ask a question
answer = model.query(image, "What's in this image?")["answer"]
print("Answer:", answer)

# Stream the response
for chunk in model.caption(image, stream=True, length="short")["caption"]:
    print(chunk, end="", flush=True)

detect = model.detect(image,"people")["objects"]
print("Detect:", detect)




