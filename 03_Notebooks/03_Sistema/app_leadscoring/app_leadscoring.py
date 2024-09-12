from codigo_de_ejecucion import *
import streamlit as st
from streamlit_echarts import st_echarts
from PIL import Image

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# LOADING IMAGES

im_sidebar = Image.open('03_Notebooks/03_Sistema/app_leadscoring/featured.jpg')
im_title = Image.open('03_Notebooks/03_Sistema/app_leadscoring/logo_app.png')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# PAGE CONFIGURATION
st.set_page_config(
     page_title = 'Lead Scoring Analyzer',
     page_icon = '03_Notebooks/03_Sistema/app_leadscoring/icon.png',
     layout = 'wide',
     initial_sidebar_state = "expanded",
     menu_items={
         'Get Help': None,
         'Report a bug': None,
         'About': "### Risk Scoring Analyzer. \n\n The purpose of this data-driven application is to automate the calculation of fees that make each new loan-customer binomial profitable by estimating the expected financial loss based on probability of default, loss given default, and exposure at default risk model predictions.\n&nbsp; \n  \n - Source code can be found [here](https://github.com/pabloelt/risk-scoring-for-a-neobank-company). \n - Further project details are available [here](https://pabloelt.github.io/project/project5/)."
     })

st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# SIDEBAR
with st.sidebar:
    st.image(im_sidebar)
    st.markdown('')

    # Botones
    col1, col2, col3, col4, col5 = st.columns([0.5,1,0.25,1,0.5])
    with col2:
        form_button = st.button('NEW LEAD WEB FORM')
    with col4:
        calculate_button = st.button('CALCULATE SCORING')

    st.markdown('---')

    st.markdown("<p style='text-align: center; color: #BBDEFC; font-size: 1.25em; font-weight: bold;'>SERVER-SIDE PARAMETERS</p>", unsafe_allow_html=True)

    # Server-side features - Input
    col1,col2 = st.columns(2)
    with col1:
        origen = st.selectbox('Lead origin:',
                              ['API','Landing Page Submission','Lead Add Form','OTROS'],0)
        ult_actividad = st.selectbox('Last activity:',
                                     ['Chat Conversation','Converted to Lead','Email Link Clicked','Email Opened','Page Visited on Website','SMS Sent','OTROS'],0)
        visitas_total = st.slider('Total visits:', 0, 20, value = 3)
        score_perfil = st.slider('Profile score:', 0, 20, value = 18)
    with col2:
        fuente = st.selectbox('Lead source:',
                              ['Chat','Direct Traffic','Google','Organic Search','Reference','OTROS'],0)
        tiempo_en_site_total = st.number_input('Total time on website (min)', value=0, placeholder="Type time...")
        paginas_vistas_visita = st.slider('Page views per visit:', 0, 25, value = 5)
        score_actividad = st.slider('Activity score:', 0, 20, value = 12)


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# MAIN

# Title image
col1, col2, col3 = st.columns([1,8,1])
with col2:
    st.image(im_title)
    st.markdown(' ')

placeholder = st.empty()

with placeholder.container():
    # Subtitle
    st.markdown("<p style='text-align: left; color: #BBDEFC; font-size: 1.25em; font-weight: bold;'>LEAD WEB FORM</p>", unsafe_allow_html=True)
    st.markdown(' ')

    # Lead web form features - Input
    # Personal details
    st.markdown("<p style='text-align: left; color: #BBDEFC; font-size: 1em;'>Personal details</p>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        pais = st.selectbox('Country:', ['Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia, Plurinational State of', 'Bonaire, Sint Eustatius and Saba', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Congo, The Democratic Republic of the', 'Cook Islands', 'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City State)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran, Islamic Republic of', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea, Democratic People's Republic of", 'Korea, Republic of', 'Kuwait', 'Kyrgyzstan', "Lao People's Democratic Republic", 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao', 'Macedonia, Republic of', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Federated States of', 'Moldova, Republic of', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saint Barthélemy', 'Saint Helena, Ascension and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin (French part)', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten (Dutch part)', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan, Province of China', 'Tajikistan', 'Tanzania, United Republic of', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela, Bolivarian Republic of', 'VietNam', 'Virgin Islands, British', 'Virgin Islands, U.S.', 'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe'],235)
        ocupacion = st.selectbox('Current occupation:',
                                     ['Businessman','Housewife','Student','Unemployed','Working Professional','OTROS'],0)
        conociste = st.selectbox('How did you hear about our company?',
                                      ['Select','Facebook','Google','Newspaper','Review','Word of mouth','Youtube','OTROS'],0)
    with col2:
        ciudad = st.text_input('City:', value='New York', max_chars=60, type="default")
        ambito = st.selectbox('Specialization:',
                                     ['Select','Banking, Investment And Insurance','Business Administration','Finance Management','Human Resource Management','IT Projects Management','International Business','Marketing Management','Media and Advertising','Operations Management','Supply Chain Management','Travel and Tourism','OTROS'],0)
        proposito = st.selectbox('What matters most to you in choosing this course?',
                                       ['Select','Better Career Prospects','Flexibility & Convenience','Unknown','OTROS'],0)
       
    st.markdown('---')

    col1,col2 = st.columns(2)
    with col1:
        st.markdown('Would you like to recieve more information?')

    with col2:
        st.markdown("Are you interested in downloading a free copy of our book?")
    
    col1,col2,col3 = st.columns([0.65,0.85,1.5])
    with col1:
        llamar = st.radio('Phone call',['Yes','No'], 0, horizontal = True)

    with col2:
        enviar_email = st.radio('Email',['Yes','No'], 0, horizontal = True)

    with col3:
        descarga_lm = st.radio('Interested',['Yes', 'No'], 0, horizontal = True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Dataset creation

df_lead = pd.DataFrame({'origen': origen,
                        'fuente': fuente,
                        'ult_actividad': ult_actividad,
                        'ambito': ambito,
                        'ocupacion': ocupacion,
                        'descarga_lm': descarga_lm,
                        'visitas_total': visitas_total,
                        'tiempo_en_site_total': tiempo_en_site_total * 60,
                        'paginas_vistas_visita': paginas_vistas_visita,
                        'score_actividad': score_actividad,
                        'score_perfil': score_perfil,
                        'pais': pais,
                        'ciudad': ciudad,
                        'llamar': llamar,
                        'enviar_email': enviar_email}
                        ,index=[0])

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# CALCULATE RISK:
if calculate_button:
    scoring, scoring_roi = ejecutar_modelo(df_lead)
    scoring = int(scoring*100)
    placeholder.empty()
    placeholder_results = st.empty()

    def formatter_function(val):
        if val == 0.875*100:
            return('A')
        elif val == 0.625*100:
            return('B')
        elif val == 0.375*100:
            return('C')
        elif val == 0.125*100:
            return('D')
        return('')
    

    chart_options = {
        "stateAnimation": {"duration":300,
                           "easing":"cubicOut"},
        "animation": "True",
        "animationThreshold":2000,
        "animationDuration": 1000,
        "animationEasing": "cubicInOut",
        "animationDelay": 500,
        "animationDurationUpdate": 1000,
        "animationEasingUpdate": "cubicInOut",
        "animationDelayUpdate": 500,

        "tooltip": {"formatter": "{b} : {c}%"},
        "series": [{"type": 'gauge',
                    "startAngle": 200,
                    "endAngle": -20,
                    "min": 0,
                    "max": 100,
                    "splitNumber": 10,
                    "animationThreshold": 2000,
                    "animationDuration": 1000,
                    "animationDurationUpdate": 1000,
                    "animationDelayUpdate": 500,
                    "animationEasing": 'cubicInOut',

                     "axisLine": {"lineStyle": {"width": 15,
                                                "color": [[0.25, '#FF6E76'],
                                                          [0.5, '#FDDD60'],
                                                          [0.75, '#58D9F9'],
                                                          [1, '#7CFFB2']]}},
                     "pointer": {"icon": 'path://M12.8,0.7l12,40.1H0.7L12.8,0.7z',
                                 "length": '15%',
                                 "width": 20,
                                 "offsetCenter": [0, '-65%'],
                                 "itemStyle": {"color": 'auto'}},
                      "axisTick": {"length": 10,
                                   "lineStyle": {"color": 'auto',
                                                 "width": 1}},
                      "splitLine": {"length": 15,
                                    "lineStyle": {"color": 'auto',
                                                  "width": 3}},
                      "axisLabel": {"color": '#464646',
                                    "fontSize": 25,
                                    "distance": -70,
                                    "formatter": formatter_function("{value}")},
                      "title": {"offsetCenter": [0, '-40%'],
                                "fontSize": 25},
                      "detail": {"valueAnimation": "True",
                                 "fontSize": 80,
                                 "offsetCenter": [0, '0%'],
                                 "formatter": "{value}",
                                 "color": 'auto'},
                      "data": [{"value": scoring,
                                "name": 'Lead Scoring'}]}],
                      "progress": {"show": "True", "width": 1,}
                                };
    
    st.markdown('---')
    col1,col2 = st.columns([1,0.8])
    if scoring_roi == 1:
        with col1:
            st.markdown("<h4 style='text-align: center; color: #7CFFB2;'>It is cost-effective to manage this lead.</h4>", unsafe_allow_html=True)
        with col2:
            if scoring >= 75:
                st.markdown("<h4 style='text-align: center; color: #7CFFB2;'>Priority: Very high. </h4>", unsafe_allow_html=True)
            elif 50 <= scoring < 75:
                st.markdown("<h4 style='text-align: center; color: #58D9F9;'>Priority: High. </h4>", unsafe_allow_html=True)
            elif 25 <= scoring < 50:
                st.markdown("<h4 style='text-align: center; color: #FDDD60;'>Priority: Medium. </h4>", unsafe_allow_html=True)
            elif 25 > scoring:
                    st.markdown("<h4 style='text-align: center; color: #FF6E76;'>Priority: Low. </h4>", unsafe_allow_html=True)
    elif scoring_roi == 0:
        with col1:
            st.markdown("<h4 style='text-align: center; color: #FF6E76;'>It is not cost-effective to manage this lead.</h4>", unsafe_allow_html=True)
    
    st.markdown('---')
    results_plot = st_echarts(options=chart_options, width="100%", key=0, height='550%')

    
