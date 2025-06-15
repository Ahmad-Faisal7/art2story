from PIL import Image
from blip_utils import extract_caption
from gemini_utils import generate_story_from_caption

# Load image
image = Image.open("art.jpg")

# Get caption
caption = extract_caption(image)
print("🖼️ Caption:", caption)

# Get story from Gemini
story = generate_story_from_caption(caption)
print("\n📖 Story:\n", story)
