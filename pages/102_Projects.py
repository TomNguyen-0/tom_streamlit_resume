# https://docs.streamlit.io/library/api-reference/widgets/st.page_link

import streamlit as st
# import streamlit.components.v1 as components
# from streamlit_javascript import st_javascript
from components.write_to_firebase import log_company_type
from streamlit.components.v1 import html


TITLE_OF_PAGE = "Tom's Projects"
favicon = "img/tnV2.png"
if "initial_page" not in st.session_state:
    st.session_state["initial_page"] = "streamlit_app.py"
else:
    st.set_page_config(page_title=TITLE_OF_PAGE, 
                   page_icon = favicon, 
                   layout = 'centered', 
                   initial_sidebar_state = 'auto'
                   )
    
## 2. write to url params
if "COMPANY_NAME" not in st.session_state:
    st.session_state["COMPANY_NAME"] = "na"
st.query_params["company"]= st.session_state["COMPANY_NAME"]
    
col1, col2 = st.columns(2)

# st.page_link("streamlit_app.py",label=":blue[Project] - :green[Javascript]", icon="🌎")
company_name = st.session_state["COMPANY_NAME"]
with col1:
    st.title("Projects")
    st.page_link(f"https://tom-nguyen.streamlit.app/?company={company_name}-projects",label=":blue[Project] - :green[Python]: Resume", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/tom_streamlit_resume",label=":grey[GitHub] - :green[Python]: Tom's Resume", icon="🗄️")
    st.divider()
    st.image("img/projects/piano.jpg", use_column_width=True, caption="Game: Piano")
    st.page_link("https://february-golden-ticket.netlify.app",label=":blue[Game] - :green[Javascript]: Piano", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/february-golden-ticket",label=":grey[GitHub] - :green[Javascript]: Piano", icon="🗄️")
    st.divider()
    st.image("img/projects/tic_tac_toe.jpg", use_column_width=True, caption="Game: Tic Tac Toe")
    st.page_link("https://january-golden-ticket.netlify.app/",label=":blue[Game] - :green[Javascript]: Tic Tac Toe", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/january-golden-ticket",label=":grey[GitHub] - :green[Javascript]: Tic Tac Toe", icon="🗄️")
    st.divider()
    st.image("img/projects/connect_4.jpg", use_column_width=True, caption="Game: Connect Four")
    st.page_link("https://tom-nguyen-resume.netlify.app/developer/games.html",label=":blue[Game] - :green[Javascript]: Connect Four", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/connect_four",label=":grey[GitHub] - :green[Javascript]: Connect Four", icon="🗄️")
    st.divider()
    st.image("img/projects/fix_errors_and_computers.jpg", use_column_width=True, caption="Game: Shooting Computer errors")
    st.page_link("https://tom-nguyen-resume.netlify.app/developer/games.html",label=":blue[Game] - :green[Javascript]: Shooting Computer errors", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/games",label=":grey[GitHub] - :green[Javascript]: Shooting Computer errors", icon="🗄️")
    st.divider()
    st.image("img/projects/badge_collector.jpg", use_column_width=True, caption="Game: Badge Collector")
    st.page_link("https://tom-nguyen-resume.netlify.app/developer/games.html",label=":blue[Game] - :green[Javascript]: Badge Collector", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/games",label=":grey[GitHub] - :green[Javascript]: Badge Collector", icon="🗄️")
    st.divider()
    st.image("img/projects/christmas_card.jpg", use_column_width=True, caption="Javascript: Christmas Card")
    st.page_link("https://december-golden-ticket.netlify.app",label=":blue[Card] - :green[Javascript]: Christmas Card", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/december-golden-ticket",label=":grey[GitHub] - :green[Javascript]: Christmas Card", icon="🗄️")
    st.divider()
    st.image("img/projects/moving_turkey.jpg", use_column_width=True, caption="Javascript: Moving Turkey")
    st.page_link("https://november-golden-ticket.netlify.app",label=":blue[Card] - :green[Javascript]: Moving Turkey", icon="📁")
    st.page_link("https://github.com/TomNguyen-0/november-golden-ticket",label=":grey[GitHub] - :green[Javascript]: Moving Turkey", icon="🗄️")
    st.divider()
    st.image("img/projects/todo_list.jpg", use_column_width=True, caption="Javascript: Task Manager")
    st.page_link("https://tom-nguyen-fsdi-106-assignment04.netlify.app/",label=":blue[Project] - :green[Javascript]: Task Manager", icon="📁")
    st.page_link("https://github.com/TomNguyen-FSDI/Task-Manager",label=":grey[GitHub] - :green[Javascript]: Source Code", icon="🗄️")
    st.divider()
    st.image("img/projects/ClickUp.jpg", use_column_width=True, caption="SASS: ClickUp Website")
    st.page_link("https://tom-nguyen.netlify.app/developer/clickup/about",label=":blue[Project] - :green[Sass]: CSS pre-processor", icon="📁")
    st.page_link("https://github.com/TomNguyen-FSDI/sassy-responsive-website",label=":gray[GitHub] - :green[Sassy]: Source Code", icon="🗄️") 
    st.divider()
    st.image("img/projects/catalog.jpg", use_column_width=True, caption="React: Grocery Website")
    st.page_link("https://tomnguyen-fsdi.github.io/organika/",label=":blue[Project] - :green[React]: Grocery Website", icon="📁")
    st.page_link("https://github.com/TomNguyen-FSDI/organika",label=":gray[GitHub] - :green[React]: Source Code", icon="🗄️")
    st.divider()
    st.image("img/projects/coffee_store.jpg", use_column_width=True, caption="HTML: Coffee Website")
    st.page_link("https://tom-nguyen-cr.netlify.app/",label=":blue[Project] - :green[HTML]: Coffee Website", icon="📁")
    st.page_link("https://github.com/TomNguyen-FSDI/Coffee-Shop",label=":gray[GitHub] - :green[HTML]: Source Code", icon="🗄️")
    st.divider()
# with col2:
#     st.title("Source Code")

user_dict = st.experimental_user.to_dict() #[3]
if user_dict["email"] != "test@example.com":
    from components.write_to_firebase import log_company_type
    log_company_type("projects")


# if st.link_button("Go to gallery", "https://streamlit.io/gallery"):
#     # log_company_type("project_javascript")
#     st.write("project - JavaScript")

# if st.button("Page 2"):
#     st.switch_page("https://tom-nguyen-fsdi-106-assignment04.netlify.app/")
    
    