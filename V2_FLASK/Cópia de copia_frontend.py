import streamlit as st
from utils.io_utils import load_config
import cv2
import requests
import base64

config = load_config()

###################STREAMLIT CONFIG#############################
player_img_path = '/content/drive/MyDrive/0. Machine Learning/Projetos/Toxic Comment/prod/images/youtube2.png'
likearea_path = '/content/drive/MyDrive/0. Machine Learning/Projetos/Toxic Comment/prod/images/likearea.png'
icon_path = '/content/drive/MyDrive/0. Machine Learning/Projetos/Toxic Comment/prod/images/keysi_img.jpg'
sidevideos_path = '/content/drive/MyDrive/0. Machine Learning/Projetos/Toxic Comment/prod/images/sidevideos.PNG'

styles_css_path = '/content/drive/MyDrive/0. Machine Learning/Projetos/Toxic Comment/prod/styles.html'

st.set_page_config(layout="wide")

#CSS STYLE
f = open(styles_css_path, 'r')
styles = f.read()
st.markdown(styles, unsafe_allow_html=True)

# Get image and center it
player_img = cv2.imread(player_img_path)
col1, col2, col3 = st.beta_columns([0.1,300,0.1])
col2.image(player_img, use_column_width=True)

# LIKEAREA
top_placement = f"""<div>
                  <p class="videostats">23.764 visualizações * 30 de jun. de 2021</p>
                  <img class="likearea" src="data:image/png;base64,{base64.b64encode(open(likearea_path, "rb").read()).decode()}">
                </div>
              """

st.markdown(top_placement, unsafe_allow_html=True)

#LINE SEPARATOR 

st.markdown('', unsafe_allow_html=True)
<hr class="horizontal-line" style= top:-110px;>
# DESCRIPTION
desc_placement = f"""<div>
                    <img class="profile-icon" src="data:image/png;base64,{base64.b64encode(open(icon_path, "rb").read()).decode()}"> 
                    <p class='channel-name'>Keysi Machine Teacher</p>
                  </div>
                  <div>
                    <p class='body' style=top:-120px> → Uso de Rede Neural para NLP</p>
                    <p class='body' style=top:-130px> → Projeto de conclusão de curso Awari 08/2021</p>
                    <p class='body' style=top:-140px> → Agradecimento especial para Fernando Wittman</p>
                    <p class='show-more' style=top:-145px> MOSTRAR MAIS </p>
                    <hr class="horizontal-line" style= top:-160px;>
                  </div>
                  """

st.markdown(desc_placement, unsafe_allow_html=True)

# BUTTON
popup_placement = f"""
                  <button class='conecte-bt'>CONECTE-SE</button>
                  """

st.markdown(popup_placement, unsafe_allow_html=True)

# SIDEVIDEOS
sidevideos_placement = f"""<div>
                            <img class="sidevideo" src="data:image/png;base64,{base64.b64encode(open(sidevideos_path, "rb").read()).decode()}"> 
                          </div>
                        """

st.markdown(sidevideos_placement, unsafe_allow_html=True)

#COMMENT SECTION
get_action = config['api']['application_url']

comment_section = f"""
                  <form action={{url_for("predict")}} method='POST'> 
                    <input type="text" name="comment" placeholder="Adicionar um comentário público"/>
                    <input type="submit" value="COMENTAR"/>
                  </form>
                  {{text_input}}
                  """
st.markdown(comment_section, unsafe_allow_html=True)








