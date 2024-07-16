import streamlit as st
from forms.contact import contact_form

@st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()
    
st.title('Inteligência Artificial | Data & Analytics')

# Resumo Profissional
st.write('\n')
st.subheader('Resumo Profissional')
st.write('Com mais de 4 anos de experiência em métricas de software e arquitetura de soluções em Data & Analytics, possuo uma sólida formação em Análise de Pontos de Função e na utilização de tecnologias de nuvem Azure. Durante três anos, atuei como Analista de Métricas de Software, desenvolvendo habilidades em avaliação e mensuração de software, e há um ano, venho desempenhando o papel de analista dentro da Inteligência Artificial focado em Data & Analytics.')

# Educação
st.write('\n')
st.subheader('Educação', anchor=False)
st.write(
    """
    **Mestrado**: Computação Aplicada em Inteligência Artificial | IFES (Em andamento)
    - Dissertação (Em andamento): Proposta de uma arquitetura para construção de jogos sérios para aprendizado do pensamento crítico
    """
)
st.write(
    """
    **Graduação**: Ciência da Computação | UVV (2017 - 2021)
    - Dissertação (Finalizada): DEEP LEARNING APLICADA PARA RECONHECIMENTO DE PLACAS VEICULARES | Repositório em manutenção
    - Voluntário de pesquisa: Estudo sobre aplicações de Eye Tracking e suas implementações [link](https://acpgrupo.wixsite.com/arqcidadepatrimonio/arquiteturaeneurociencia)
    """
)
    
# Experiência e Qualificações
st.write('\n')
st.subheader('Experiência e Qualificações', anchor=False)
st.write(
    """
    - Profissional experiente em arquitetura de soluções com especialização em Data & Analytics
    - Focado em implementar soluções práticas de Inteligência Artificial e criar arquiteturas de dados robustas e escaláveis
    - Hábil em projetar arquiteturas de alto nível e desenvolver relatórios analíticos
    - Experiência significativa em trabalhar com clientes na apresentação e venda de produtos baseados nas soluções desenvolvidas, garantindo a comunicação eficaz dos benefícios e valores das soluções tecnológicas
    - Experiência com tecnologias Azure, como Azure Data Factory, Azure Databricks, Azure DevOps e Power BI, além de conhecimento avançado em Python e SQL.
    """
)


# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programação: Python, SQL, PySpark
    - Visualização de Dados: PowerBI, MS Excel, Plotly
    - Modelagem: Regressão logística, regressão linear, árvores de decisão, redes neurais
    - Bancos de Dados: Postgres, MongoDB, MySQL, Azure SQL
    
    ##### Outras Habilidades
    - Experiência em MLOps
    - Containerização
    - CI/CD
    """
)
st.subheader("Soft Skills", anchor=False)
st.write(
    """
    - Excelente comunicação: Capaz de explicar conceitos técnicos complexos de forma clara e acessível
    - Trabalho em equipe: Colaboração eficaz com equipes multidisciplinares
    - Liderança: Capacidade de liderar projetos e equipes, garantindo a entrega de soluções de alto impacto
    - Resolução de problemas: Habilidade em identificar problemas e propor soluções práticas e eficazes
    - Adaptabilidade: Capacidade de se adaptar rapidamente a novas tecnologias e metodologias
    - Orientação para resultados: Foco em entregar resultados de qualidade dentro dos prazos estabelecidos
    - Iniciativa: Proatividade em identificar oportunidades de melhoria e implementar soluções
    """
)