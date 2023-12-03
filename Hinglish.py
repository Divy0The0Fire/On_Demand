#pip install mtranslate
from mtranslate import translate

# Hinglish text
hinglish_phrase = "kayse ho tum yaar"

# Translate Hinglish to English
english_translation = translate(hinglish_phrase, 'en', 'auto')

# Display the translations
print(f"Hinglish: {hinglish_phrase}")
print(f"English: {english_translation}")
