import streamlit as st
from agent import crew

st.title("Assistente PDF")

# Inicializar o histórico de mensagens na session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir mensagens anteriores
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Campo de input do chat
if prompt := st.chat_input("Digite sua pergunta..."):
    # Adicionar mensagem do usuário ao histórico
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Mostrar mensagem do usuário
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Mostrar resposta do assistente
    with st.chat_message("assistant"):
        with st.spinner('Pensando...'):
            # Obter resposta do crew
            result = crew.kickoff(inputs={"customer_question": prompt})
            
            if hasattr(result, 'tasks_output') and len(result.tasks_output) > 0:
                response = result.tasks_output[0].raw
                st.markdown(response)
                
                # Adicionar resposta ao histórico
                st.session_state.messages.append({"role": "assistant", "content": response})
            else:
                st.error("Não foi possível gerar uma resposta.")

