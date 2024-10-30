import streamlit as st
from src.components.startconversation import InitialConversation
from src.utils import get_chat_completions, moderation_check
from src.components.intent_confirmation import IntentConfirmation
from src.components.get_dictionary_str import GetDictionaryString
from src.pipeline.get_top_insurance import GetTopInsurance
from src.components.start_conv_reco import ConvRecommendation
from src.pipeline.logger import logging

st.title('Health Insurance Chatbot')

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.conversation = InitialConversation().initialize_conversation()
    introduction = get_chat_completions(st.session_state.conversation)
    st.session_state.messages.append({'role': 'assistant', 'content': introduction})

    st.session_state.top_insurance = None
    st.session_state.conversation_reco = []

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message['content'])



user_input = st.chat_input("Message Insurance Chatbot")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    st.session_state.messages.append({
        'role': 'user',
        'content': user_input
    })
    if user_input == "exit":
        with st.chat_message("assistant"):
            st.markdown("Thankyou for using the service!!!")
        st.stop()
    else:
        moderation = moderation_check(user_input)
        
        if moderation == "Flagged":
            with st.chat_message("assistant"):
                st.markdown("Sorry, your message has been flagged by the system. Please restart your conversation.")
            st.stop()
            
        if st.session_state.top_insurance is None:
            st.session_state.conversation.append({"role": "user", "content": user_input})

            response_assitant = get_chat_completions(st.session_state.conversation)

            moderation = moderation_check(response_assitant)
            if moderation == "Flagged":
                with st.chat_message("assistant"):
                    st.markdown("Sorry, the message has been flagged by the system. Connecting you to human expert.")
                st.stop()
            
            confirmation = IntentConfirmation().get_intent_confirmation(response_assitant)
            moderation = moderation_check(confirmation)
            if moderation == "Flagged":
                with st.chat_message("assistant"):
                    st.markdown("Sorry, the message has been flagged by the system. Connecting you to human expert.")
                st.stop()
            
            
            
            if "No" in confirmation:
                st.session_state.messages.append({
                'role': 'assistant',
                'content': response_assitant
                })

                with st.chat_message("assistant"):
                    st.markdown(response_assitant)
                st.session_state.conversation.append({"role": "assistant", "content": response_assitant})
                
            else:
                response = GetDictionaryString().getDictionary(response_assitant)
                moderation = moderation_check(response)
                if moderation == "Flagged":
                    with st.chat_message("assistant"):
                        st.markdown("Sorry, the message has been flagged by the system. Connecting you to human expert.")
                    st.stop()
                    
                st.session_state.top_insurance = GetTopInsurance().get_top_insurance(response)
                logging.info("Top 3 insurance data received")
                
                if len(st.session_state.top_insurance) == 0:
                    with st.chat_message("assistant"):
                        st.markdown("Sorry, we do not have insurance that match your requirements. Connecting you to a human expert.")
                    st.stop()
                
                conversation_reco = ConvRecommendation().initialize_conv_reco(st.session_state.top_insurance)
                st.session_state.conversation_reco.append({"role": "user", "content": "This is my user profile" + response})
                
                recommendation = get_chat_completions(conversation_reco)
                
                st.session_state.conversation_reco.append({"role": "assistant", "content": recommendation})
                
                st.session_state.messages.append({
                    'role': 'assistant',
                    'content': recommendation
                })

                with st.chat_message("assistant"):
                    st.markdown(recommendation)

                print(recommendation + '\n')
        else:
            st.session_state.conversation_reco.append({"role": "user", "content": user_input})
            
            response_assitant_reco = get_chat_completions(st.session_state.conversation_reco)
            
            moderation = moderation_check(response_assitant_reco)
            if moderation == "Flagged":
                with st.chat_message("assistant"):
                    st.markdown("Sorry, the message has been flagged by the system. Connecting you to human expert.")
                st.stop()
            
            print('\n' + response_assitant_reco + '\n')
            st.session_state.conversation_reco.append({"role": "assitant", "content": response_assitant_reco})
            st.session_state.messages.append({
                'role': 'assistant',
                'content': response_assitant_reco
            })

            with st.chat_message("assistant"):
                st.markdown(response_assitant_reco)