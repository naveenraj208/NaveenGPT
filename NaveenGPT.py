import streamlit as st
import openai
from streamlit_chat import message


openai.api_key="API_Key"
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSMauupF7TkdJhqJD1fUFii7TVvPQjeF26KXQ&usqp=CAU', width=800, caption='')




st.title("Naveen GPT")
st.write("This is a AI software developed to answer your question and make your life easier.It can write essays for you,get you answers during exam and crack a joke for you.It can do everything you name.Welcome to the world of NAVEEN GPT....")


response_container=st.container()
container = st.container()


if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []






def generate_response(prompt):
    st.session_state['messages'].append({"role": "user", "content": prompt})
    st.session_state['past'].append(prompt)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state['messages']
    )
    response = completion.choices[0].message.content
    st.session_state['messages'].append({"role": "assistant", "content": response})
    st.session_state['generated'].append(response)
    return response




with container:
    with st.form(key="my_form", clear_on_submit=True):
        user_input = st.text_area("You", key="input", height=100)
        submit_button=st.form_submit_button(label="Ask")


    if submit_button and user_input:
        output= generate_response(user_input)
#        st.write(output)


if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
       




st.markdown("""
    <style>
      
        }
    </style>
""", unsafe_allow_html=True)





# Use st.markdown to display CSS styles
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


 

