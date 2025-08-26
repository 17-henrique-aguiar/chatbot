import streamlit as st 

st.set_page_config(page_title="Atendimento Escola", page_icon="🎓")
st.title("Atendimento Virtual - Escola")

# Histórico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Perguntas e respostas pré-definidas
faq = {
    "Como posso agendar uma consulta com um advogado?": "Você pode agendar uma consulta diretamente pelo nosso site ou entrando em contato pelo WhatsApp.",
    "Qual o horário de atendimento?": "Estamos disponíveis de segunda a sexta, das 9h às 18h.",
    "Quais documentos preciso levar para abrir um processo?": "Depende do tipo de ação. Em geral, documentos pessoais (RG, CPF), comprovantes relacionados ao caso (contratos, mensagens, boletos) e provas são essenciais.",
    "Vocês atendem em outras cidades ou estados?": "Sim! Fazemos atendimentos online em todo o Brasil e temos parceiros em diversas regiões.",
    "Onde o escritório está localizado?": "Estamos localizados na Rua Peixe, nº 80, Centro",
    "Vocês fazem reconhecimento de firma ou autenticação de documentos?": "Não realizamos serviços cartoriais, mas podemos orientar sobre como e onde fazer isso.",
    "Falar com atendente": "Você pode falar diretamente com um atendente pelo WhatsApp clicando no botão abaixo",

}

# Mostrar histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Campo de input com sugestões de perguntas
pergunta = st.chat_input("Digite sua pergunta ou escolha uma das sugestões abaixo:")

# Mostrar botões de perguntas
for key in faq.keys():
    if st.button(key):
        pergunta = key

# Responder ao usuário
if pergunta: 
    resposta = faq.get(pergunta, "Desculpe, não tenho uma resposta para isso no momento.")

    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.session_state.messages.append({"role": "assistant", "content": resposta})

    # Mostrar mensagens
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        st.markdown(resposta)

# Se for "Falar com atendente", mostra link para WhatsApp
if pergunta == "Falar com atendente":
    whatsapp_url = "https://wa.me/55619000000000"    # número da escola com DDD
    st.markdown(f"[Clique aqui para falar no WhatsApp]({whatsapp_url})")
