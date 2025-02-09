# Seção de Projetos
st.header("📂 Projetos")
projetos = [
    {"nome": "Consulta climática", "descricao": "Saiba o tempo do mundo inteiro", "link": "https://lnkd.in/dts3xhJp"},
    {"nome": "Loja de Layouts", "descricao": "Plataforma online para venda de itens digitais", "link": "https://github.com/seuprojeto2"},
]

col1, col2 = st.columns(2)
for i, projeto in enumerate(projetos):
    with (col1 if i % 2 == 0 else col2):
        st.subheader(projeto["nome"])
        st.write(projeto["descricao"])
        st.write(f"[🔗 Veja mais]({projeto['link']})")
