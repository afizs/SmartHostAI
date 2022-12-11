import streamlit as st
from assembly_ai_plus.assemblyai import AssemblyAI

from zoom_provided import zoom_provider
from config import assemblyai_key

st.set_page_config(
    page_title="SmartHostAI", page_icon="✈️", initial_sidebar_state="expanded"
)

st.write(
    """
# ✈️ SmartHostAI
The co-Host every meeting needs.
"""
)

zoom_id = st.text_input(label='Zoom Meeting ID', max_chars=23)
if zoom_id:
    recording_details = zoom_provider(zoom_id)
    audio_url = recording_details.get("audio_url")
    st.write('#### Meeting Details')
    st.write(f'Recording URL: {audio_url}')
    options = st.multiselect('Participants', 
                             recording_details.get('participants', []), 
                             recording_details.get('participants', []))

    if st.button('Get Bulleted Summary'):
        assembly_ai = AssemblyAI(api_key=assemblyai_key)
        res = assembly_ai.submit_audio_for_transcription(audio_url, 
                                                   summarization = True, 
                                                   summary_type = 'bullets')
        # print('r7qut7yd9i-8ecb-405a-b3a0-759b894c84b1')
        st.write('r7qut7yd9i-8ecb-405a-b3a0-759b894c84b1')
        
        # full_details = assembly_ai.get_transcription_results(res.get('id'), all_details=True)
        # st.json(full_details)
        full_details = assembly_ai.get_transcription_results('r7qut7yd9i-8ecb-405a-b3a0-759b894c84b1',
                                                             all_details = True)
        st.write('### Summary of the meeting: ')
        for bullet in full_details.get('summary').split('-'):
            st.write(bullet)
        
        st.button('Send Email to Selected Participants')
        st.button('Create Tasks in GitHub')
        
        
        
        