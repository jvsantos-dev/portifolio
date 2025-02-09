import streamlit as st

# Configuração da página
st.set_page_config(page_title="João Victor", page_icon="logo.png", layout="wide")

# Sidebar - Menu de Navegação
st.sidebar.title("Menu")
pagina = st.sidebar.radio("Navegue entre as páginas:", ["🏠 Sobre Mim", "🚀 Projetos", "💼 Freelancer"])

# Estilos personalizados
st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-size: cover;
        color: black;
    }
    [data-testid="stSidebar"] {
        background-color: #1f4e79;
    }
    header, .css-1d391kg, .css-1kxg7xu {
        visibility: hidden;
    }
    h1, h2, h3, h4, h5, h6 {
        text-align: center;
    }
    p {
        text-align: justify;
        font-size: 18px;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Página "Sobre Mim"
if pagina == "🏠 Sobre Mim":
    st.header("🙋‍♂️ Sobre Mim")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("eu_agora.jpg", width=220)
    with col2:
        st.markdown(
            """
            <div class="container">
            <p>Sou um entusiasta de dados e machine learning, sempre em busca de aprimorar minhas habilidades e explorar novas tecnologias.</p>
            <p>Tenho experiência com Python, SQL, Excel e Power BI, ferramentas que utilizo para transformar dados brutos em insights valiosos e decisões estratégicas.</p>
            <p>Minhas áreas de interesse incluem análise de dados, inteligência artificial e automação de processos.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Página "Projetos"
elif pagina == "🚀 Projetos":
    st.header("🚀 Projetos")
    st.markdown(
        """
        <p>Aqui você encontrará alguns dos meus projetos mais recentes.</p>
        <ul>
            <li><b>Simulador de Corrida</b>: Projeto de simulação baseado em Fórmula E.</li>
            <li><b>Monitoramento Global de Vinícolas</b>: Dashboard de análise com sensores IoT.</li>
            <li><b>Loja Digital</b>: Marketplace para venda de itens digitais.</li>
        </ul>
        """,
        unsafe_allow_html=True
    )

# Página "Freelancer"
elif pagina == "💼 Freelancer":
    st.header("💼 Serviços Freelancer")
    st.markdown(
        """
        <p>Ofereço serviços especializados em:</p>
        <ul>
            <li>🔹 Desenvolvimento de dashboards (Power BI, Python, SQL)</li>
            <li>🔹 Análise de dados e automação de processos</li>
            <li>🔹 Desenvolvimento web (Python, React, APIs)</li>
        </ul>
        <p>Entre em contato para discutir um projeto!</p>
        """,
        unsafe_allow_html=True
    )

# Rodapé - Redes Sociais e CV
st.markdown("---")
st.markdown("<h3 style='text-align: center;'>📬 Conecte-se comigo</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.markdown(f'<a href="https://github.com/seuusuario" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/733/733553.png" width="50"></a>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<a href="https://www.linkedin.com/in/seuusuario" target="_blank"><img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="50"></a>', unsafe_allow_html=True)
with col3:
    st.markdown("[Twitter](https://twitter.com/seuusuario)")
with col4:
    st.markdown("📧 [seuemail@email.com](mailto:seuemail@email.com)")

st.markdown("<br>", unsafe_allow_html=True)
with open("cv_joaovictor.pdf", "rb") as file:
    st.download_button(
        label="📄 Baixar meu CV",
        data=file,
        file_name="Meu_CV.pdf",
        mime="application/pdf"
    )
