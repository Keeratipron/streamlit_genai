import streamlit as st

pages = {
    "CREATE": [
        st.Page("1_texttospeech.py", title="Text to Speech", icon=":material/font_download:"),
        # st.Page("2_voicechanger.py", title="Voice Changer", icon=":material/record_voice_over:"),
        st.Page("3_voices.py", title="Voices", icon=":material/graphic_eq:"),
        st.Page("4_soundeffects.py", title="Sound Effects", icon=":material/air:"),
        st.Page("14_Speech_to_text.py", title="Speech to Text", icon=":material/mic:"),
    ],
    "CONVERSATIONAL": [
        st.Page("5_agents.py", title="Agents", icon=":material/headset_mic:"),
        st.Page("6_conversations.py", title="Conversations", icon=":material/forum:"),
        st.Page("7_phonenumbers.py", title="Phone Numbers", icon=":material/call:"),
    ],
    "WORKFLOWS": [
        st.Page("8_projects.py", title="Projects", icon=":material/collections_bookmark:"),
        st.Page("9_voiceover_studio.py", title="Voiceover Studio", icon=":material/radio:"),
        st.Page("10_dubbing_studio.py", title="Dubbing Studio", icon=":material/translate:"),
        st.Page("11_audio_native.py", title="Audio Native", icon=":material/volume_down:"),
    ],
    "TOOLS": [
        st.Page("12_voice_isolator.py", title="Voice Isolator", icon=":material/contactless:"),
        st.Page("13_ai_speech_classifier.py", title="AI Speech Classifier", icon=":material/branding_watermark:"),
    ],
}

pg = st.navigation(pages)
pg.run()




