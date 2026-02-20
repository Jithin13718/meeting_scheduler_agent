from app.services.scaledown import compress_prompt

def learn_preferences(user_history: dict) -> dict:
    """
    Learn user scheduling preferences using ScaleDown compression.
    :param user_history: Dictionary of past meetings/preferences
    :return: Dictionary of learned preferences
    """
    compressed = compress_prompt(
        context="Meeting preference learning",
        prompt=str(user_history),
        model="gpt-4o"
    )
    return {"preferences": compressed}