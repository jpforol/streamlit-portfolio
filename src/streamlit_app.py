import streamlit as st
import base64
from pathlib import Path
from utilities.utilities import load_bootstrap
from forms.contact import contact_form

load_bootstrap()

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded
def img_to_html(img_path):
    img_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
      img_to_bytes(img_path)
    )
    return img_html

@st.experimental_dialog('Contact Me')
def show_contact_form():
    contact_form()

# PAGE SETUP 
about_page = st.Page(
    'views/about_me.py',
    title= 'Sobre mim',
    icon= ':material/account_circle:',
    default= True,
)

projects_page = st.Page(
    'views/projects_page.py',
    title= 'Projetos',
    icon= ':material/bar_chart:',
)
pg = st.navigation(
    {
        'Info': [about_page, projects_page],
    }
    )

# SHARED ON ALL PAGESs
with st.sidebar:
    st.header('João Pedro Forequi de Oliveira')
    st.image('assets\profile_image.png')
    st.markdown(img_to_html('assets\email_icon.png')+'  jpforol@gmail.com', unsafe_allow_html=True)
    st.markdown(img_to_html('assets\linkedin_icon.png')+'  [in/jpforol](https://www.linkedin.com/in/jpforol/)', unsafe_allow_html=True)
    st.markdown(img_to_html('assets\github_icon.png')+'  [/jpforol](https://github.com/jpforol)', unsafe_allow_html=True)
    if st.button('Contate-me'):
        show_contact_form()
    st.markdown('Feito por [João Pedro Forequi de Oliveira](https://www.linkedin.com/in/jpforol/)')

# RUN NAVIGATION
pg.run()