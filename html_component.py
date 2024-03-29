"""
try and see if we can pass in html file into streamlt

date                name           comment
02/12/2024          TomN           initial creations


"""

import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.stylable_container import stylable_container
from css.right_box import right_box
from css.right_box_1 import right_box_1
import css.right_form_title as right_form_title
import css.Variables as Variables
import base64
from streamlit_javascript import st_javascript # [5]
from st_click_detector import click_detector # [8]

TITLE_OF_PAGE = "Tom's Resume"
favicon = "img/tnV2.png"

st.set_page_config(page_title=TITLE_OF_PAGE, 
                   page_icon = favicon, 
                   layout = 'centered', 
                   initial_sidebar_state = 'auto'
                   )

@st.cache_data # [4]
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


st_theme = st_javascript("""window.getComputedStyle(window.parent.document.getElementsByClassName("stApp")[0]).getPropertyValue("color-scheme")""")
st.session_state["page_theme"] = st_theme

## load javascript
temp="""    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">"""
st.markdown('{}'.format(temp), unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        source_code = f.read()
        source_code = source_code.replace('\n', '')

        ## get images and calculated variables from css/Variables.py
        bin_str = get_base64_of_bin_file('img/resume-background.jpg')
        source_code = source_code.replace('background-image:url("./../img/resume-background.jpg");', f'background-image: url("data:image/jpg;base64,{bin_str}");')
        temp = str(int(Variables.get_variables("page-width"))-300)
        temp2 = str(int(Variables.get_variables("page-height"))+54)
        source_code = source_code.replace('background-size: calc(var(--page-width) + 300px) calc(var(--page-height) + 54px);', f'background-size: {temp}px {temp2}px;')
        bin_str = get_base64_of_bin_file('img/profile-picture.jpg')
        source_code = source_code.replace('background-image: url(./../img/profile-picture.jpg);', f'background-image: url("data:image/jpg;base64,{bin_str}");')    
        bin_str = get_base64_of_bin_file('img/laptop-bg.jfif')
        source_code = source_code.replace('background-image: url(../img/laptop-bg.jfif);', f'background-image: url("data:image/jpg;base64,{bin_str}");')
        temp = str(int(Variables.get_variables("profile-height"))*1.05)
        source_code = source_code.replace('height: calc(var(--profile-height) * 1.05);', f'height: {temp}px;')
        temp = str(int(Variables.get_variables("profile-width"))*1.05)
        source_code = source_code.replace('width: calc(var(--profile-width) * 1.05);', f'width: {temp}px;')
        temp = str(int(Variables.get_variables("page-width"))-323)
        source_code = source_code.replace('width: calc(var(--page-width) - 323px);', f'width: {temp}px;')
        temp = str(int(Variables.get_variables("page-width"))+300)
        source_code = source_code.replace('background-size: calc(var(--page-width) + 300px) 6000px;', f'background-size: {temp}px 6000px;')

        ## get variables from css/Variables.py
        source_code = source_code.replace('var(--page-width)', f'{Variables.get_variables("page-width")}px')
        source_code = source_code.replace('var(--page-height)', f'{Variables.get_variables("page-height")}px')
        source_code = source_code.replace('var(--profile-height)', f'{Variables.get_variables("profile-height")}px')
        source_code = source_code.replace('var(--profile-width)', f'{Variables.get_variables("profile-width")}px')
        source_code = source_code.replace('var(--resume-title-height)', f'{Variables.get_variables("resume-title-height")}px')
        source_code = source_code.replace('var(--left-box-width)', f'{Variables.get_variables("left-box-width")}px')
        source_code = source_code.replace('var(--right-box-width)', f'{Variables.get_variables("right-box-width")}px')

        ## check if dark mode or light mode
        temp = str(int(Variables.get_variables("page-width"))+300)
        temp2 = str(int(Variables.get_variables("page-height")))
        if st.session_state["page_theme"] == "dark":
            bin_str = get_base64_of_bin_file('img/resume-background.jpg')
            source_code += f""".overwrite{{
                background-image:url("data:image/jpg;base64,{bin_str}");
                background-position: center;
                background-repeat: no-repeat;
                background-size: {temp}px {temp2}px;
                width: {temp}px;
                height: {temp2}px;
                margin-left: -150px;
                z-index: -2;
                float: top;
                }}
            .right-form{{background-color: #dedede;}}
            .stApp{{color: #36454F;}}"""
        else: # [7]
            temp = str(int(Variables.get_variables("page-width"))+300)
            temp2 = str(int(Variables.get_variables("page-height")))
            bin_str = get_base64_of_bin_file('img/resume-background.jpg')
            source_code += f""".stApp{{ 
                background-color: black;
                }}
                .overwrite{{
                background-image:url("data:image/jpg;base64,{bin_str}");
                background-position: center;
                background-repeat: no-repeat;
                background-size: {temp}px {temp2}px;
                width: {temp}px;
                height: {temp2}px;
                margin-left: -150px;
                z-index: -2;
                float: top;
                }}"""

        ## load css into markdown
        st.markdown('<style>{}</style>'.format(source_code), unsafe_allow_html=True)
        


## load css
local_css("css/resume.css")
local_css("css/style.css")

## load html
with open('resume.html', 'r') as f:
    source_code = f.read()
    source_code = source_code.replace('\n', '')
    st.markdown(source_code, unsafe_allow_html=True)




