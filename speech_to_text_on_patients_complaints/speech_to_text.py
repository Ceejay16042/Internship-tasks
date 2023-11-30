import speech_recognition as sr
import spacy

def speech_to_text(audio_file_path):
    # Create a speech recognition object
    global text
    recognizer = sr.Recognizer()

    # Use the provided audio file as a source for recognition
    with sr.AudioFile(audio_file_path) as source:
        # Record the entire audio file
        audio_data = recognizer.record(source)
        
        # Use Google Web Speech API to convert audio to text
        text = recognizer.recognize_google(audio_data)
    print('Extracted words from audio file:')
    print(text)

def extract_keywords(text):
    # Load spaCy NLP model
    nlp = spacy.load("en_core_web_sm")
    
    # Process the text with spaCy
    doc = nlp(text)

    # Extract keywords based on Part-of-Speech (POS) tags
    # Select words that are nouns, proper nouns, or adjectives
    keywords = [token.text for token in doc if token.pos_ in ["NOUN", "PROPN", "ADJ"]]
    print('\n')
    print('Keywords extracted from the audio file are:')
    print(keywords)

speech_to_text('patients_complaints2.wav')
extract_keywords(text)




