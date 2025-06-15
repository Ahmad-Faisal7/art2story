def build_story_prompt(caption: str) -> str:
    return (
        f"Write a short imaginative story based on the scene: {caption}. "
        "Describe the setting, emotions, and possible thoughts of the characters. "
        "Make it vivid and engaging."
    )
