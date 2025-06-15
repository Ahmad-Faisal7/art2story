from PIL import Image
from blip_utils import extract_caption
from generate_prompt import build_story_prompt

# Load an image (local image path)
image = Image.open("art.jpg")  # replace with your image path

# Extract caption
caption = extract_caption(image)

print("Generated Caption:", caption)

prompt = build_story_prompt(caption)

print("Prompt: ", prompt)