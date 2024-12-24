import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
import pickle

# Set up page configuration
st.set_page_config(
    page_title="Industrial Copper",
    initial_sidebar_state="expanded",
    layout="wide"
)

# User input values for select box and encoded for respective features
class Option:
    country_values = [25, 26, 27, 28, 30, 32, 38, 39, 40, 77, 78, 79, 80, 84, 89, 107, 113]
    status_values = [
        "Won", "Draft", "To be approved", "Lost", "Not lost for AM", "Wonderful",
        "Revised", "Offered", "Offerable"
    ]
    status_encoded = {
        "Lost": 0, "Won": 1, "Draft": 2, "To be approved": 3, "Not lost for AM": 4,
        "Wonderful": 5, "Revised": 6, "Offered": 7, "Offerable": 8
    }
    item_type_values = ["W", "WI", "S", "Others", "PL", "IPL", "SLAWR"]
    item_type_encoded = {"W": 5, "WI": 6, "S": 3, "Others": 1, "PL": 2, "IPL": 0, "SLAWR": 4}
    application_values = [
        2, 3, 4, 5, 10, 15, 19, 20, 22, 25, 26, 27, 28, 29, 38, 39, 40, 41, 42, 56, 58, 59,
        65, 66, 67, 68, 69, 70, 79, 99
    ]
    product_ref_values = [
        611993, 164141591, 640665, 1670798778, 628377, 1668701718, 640405, 1671863738,
        1332077137, 1693867550, 1668701376, 1671876026, 628117, 164337175, 1668701698,
        1693867563, 1282007633, 1721130331, 1665572374, 628112, 611728, 1690738206,
        1722207579, 640400, 1668701725, 164336407, 611733, 1690738219, 1665584320,
        1665572032, 1665584642, 929423819, 1665584662
    ]
    product_ref_frequency = {
        611993: 45727, 164141591: 28785, 640665: 27375, 1670798778: 18916, 628377: 18574,
        1668701718: 15284, 640405: 9715, 1671863738: 5162, 1332077137: 4561, 1693867550: 1825,
        1668701376: 1216, 1671876026: 823, 628117: 775, 164337175: 653, 1668701698: 374,
        1693867563: 293, 1282007633: 281, 1721130331: 257, 1665572374: 202, 628112: 177,
        611728: 148, 1690738206: 147, 1722207579: 125, 640400: 83, 1668701725: 56,
        164336407: 49, 611733: 45, 1690738219: 19, 1665584320: 12, 1665572032: 10,
        1665584642: 2, 929423819: 1, 1665584662: 1
    }

# Title and menu
st.markdown(
    "<h1 style='font-size: 32px; text-align: center; color: grey;'>Copper Selling Price and Status Prediction</h1>",
    unsafe_allow_html=True
)

select = option_menu(
    "",
    options=["Selling Price", "Status"],
    icons=["cash", "toggles"],
    orientation="horizontal",
)

# Selling Price Prediction
if select == "Selling Price":
    st.markdown(
        "<h5 style='color: grey;'>To predict the selling price of copper, please provide the following information:</h5>",
        unsafe_allow_html=True
    )
    with st.form("prediction"):
        col1, col2 = st.columns(2)
        with col1:
            quantity = st.number_input(label="Quantity (Min 0.1)", min_value=0.1)
            customer_frequency = st.number_input(label="Customer Frequency", min_value=1)
            country = st.selectbox(label="Country", options=Option.country_values)
            status = st.selectbox(label="Status", options=Option.status_values)
            application = st.selectbox(label="Application", options=Option.application_values)
            item_type = st.selectbox(label="Item Type", options=Option.item_type_values)
        with col2:
            thickness = st.number_input(label="Thickness", min_value=0.1)
            width = st.number_input(label="Width", min_value=1.0)
            product_ref = st.selectbox(label="Product Ref", options=Option.product_ref_values)
            item_date = st.date_input(label="Item Date")
            delivery_date = st.date_input(label="Delivery Date")
            
            st.markdown('<br>', unsafe_allow_html=True)            
            button=st.form_submit_button('PREDICT',use_container_width=True)

    if button:
        if not all([item_date, delivery_date, country, item_type, application, product_ref,
                    customer_frequency, status, quantity, width, thickness]):
            st.error("Please fill in all required fields.")
        else:
            with open("Regressor.pkl", "rb") as file:
                predict_model = pickle.load(file)

            status = Option.status_encoded[status]
            item_type = Option.item_type_encoded[item_type]
            delivery_time_taken = abs((item_date - delivery_date).days)
            quantity_log = np.log1p(quantity)
            thickness_log = np.log1p(thickness)
            product_ref = Option.product_ref_frequency[product_ref]
            customer_frequency_log = np.log1p(customer_frequency)
            item_year = item_date.year
            delivery_year = delivery_date.year
            item_day = item_date.day
            item_dayofweek = item_date.weekday()
            delivery_dayofweek = delivery_date.weekday()

            user_data = np.array([[
                quantity_log, country, status, item_type, application, thickness_log, width,
                delivery_time_taken, item_year, item_day, item_dayofweek, delivery_year,
                delivery_dayofweek, customer_frequency_log, product_ref
            ]])
            pred = predict_model.predict(user_data)
            selling_price = np.exp(pred[0])
            st.subheader(f":green[Predicted Selling Price :] {selling_price:.2f}")

# Status Prediction
elif select == "Status":
    st.markdown(
        "<h5 style='color: grey;'>To predict the status of copper, please provide the following information:</h5>",
        unsafe_allow_html=True
    )
    with st.form("classifier"):
        col1, col2 = st.columns(2)
        with col1:
            item_date = st.date_input(label="Item Date")
            country = st.selectbox(label="Country", options=Option.country_values)
            item_type = st.selectbox(label="Item Type", options=Option.item_type_values)
            application = st.selectbox(label="Application", options=Option.application_values)
            product_ref = st.selectbox(label="Product Ref", options=Option.product_ref_values)
            customer_frequency = st.number_input(label="Customer Frequency", min_value=1)
        with col2:
            delivery_date = st.date_input(label="Delivery Date")
            quantity = st.number_input(label="Quantity", min_value=0.1)
            width = st.number_input(label="Width", min_value=1.0)
            thickness = st.number_input(label="Thickness", min_value=0.1)
            selling_price = st.number_input(label="Selling Price", min_value=0.1)
            
            st.markdown('<br>', unsafe_allow_html=True)            
            button=st.form_submit_button('PREDICT',use_container_width=True)

    if button:
        if not all([item_date, delivery_date, country, item_type, application, product_ref,
                    customer_frequency, quantity, width, thickness, selling_price]):
            st.error("Please fill in all required fields.")
        else:
            with open("Classifier.pkl", "rb") as file:
                model = pickle.load(file)

            item_type = Option.item_type_encoded[item_type]
            product_ref = Option.product_ref_frequency[product_ref]
            delivery_time_taken = abs((item_date - delivery_date).days)
            quantity_log = np.log1p(quantity)
            thickness_log = np.log1p(thickness)
            selling_price_log = np.log1p(selling_price)
            customer_frequency_log = np.log1p(customer_frequency)
            item_year = item_date.year
            delivery_year = delivery_date.year
            item_day = item_date.day
            item_dayofweek = item_date.weekday()
            delivery_dayofweek = delivery_date.weekday()

            user_data = np.array([[
                quantity_log, country, item_type, application, thickness_log, width,
                selling_price_log, delivery_time_taken, item_year, item_day, item_dayofweek,
                delivery_year, delivery_dayofweek, customer_frequency_log, product_ref
            ]])
            status = model.predict(user_data)

            if status == 1:
                st.subheader(f":green[Status of the copper : ] Won")
            else:
                st.subheader(f":red[Status of the copper :] Lost")
