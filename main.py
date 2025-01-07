import streamlit as st

pages = {
    "CREATE": [
        st.Page("1_texttospeech.py", title="Text to Speech"),
        st.Page("2_voicechanger.py", title="Voice Changer"),
        st.Page("3_voices.py", title="Voices"),
        st.Page("4_soundeffects.py", title="Sound Effects"),
    ],
    "CONVERSATIONAL": [
        st.Page("5_agents.py", title="Agents"),
        st.Page("6_conversations.py", title="Conversations"),
        st.Page("7_phonenumbers.py", title="Phone Numbers"),
    ],
    "WORKFLOWS": [
        st.Page("8_projects.py", title="Projects"),
        st.Page("9_voiceover_studio.py", title="Voiceover Studio"),
        st.Page("10_dubbing_studio.py", title="Dubbing Studio"),
        st.Page("11_audio_native.py", title="Audio Native"),
    ],
    "TOOLS": [
        st.Page("12_voice_isolator.py", title="Voice Isolator"),
        st.Page("13_ai_speech_classifier.py", title="AI Speech Classifier"),
    ],
}

pg = st.navigation(pages)
pg.run()




