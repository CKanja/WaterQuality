import streamlit as st
import joblib
import pickle
from sklearn.preprocessing import StandardScaler

# Load the pickled model
with open('water_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load the pickled scaler
with open('water_scaler.pkl', 'rb') as f:
    scale = pickle.load(f)

# Define the Streamlit app
def main():
    st.title('Water Quality Prediction')
    # Display the banner image
    st.image('https://images.unsplash.com/photo-1617155093730-a8bf47be792d?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D', use_column_width=True)

     # Inject custom CSS to increase the font size of slider titles
    st.markdown("""
        <style>
            .stSlider label {
                font-size: 20px; /* Adjust the font size as desired */
                font-weight: bold; /* Make the titles bold */
            }
        </style>
    """, unsafe_allow_html=True)
    
    # Add input fields for user input
    ph = st.slider('pH', min_value=0.0,max_value=14.0, step=0.1)
    Hardness = st.slider('Hardness', min_value=100, max_value=300, step=1)
    Solids = st.slider('Solids', min_value=10000, max_value=30000, step=100)
    Chloramines = st.slider('Chloramines', min_value=0.0, max_value=20.0, step=0.1)
    Sulfate = st.slider('Sulfate', min_value=200, max_value=600, step=1)
    Conductivity = st.slider('Conductivity', min_value=100, max_value=700, step=1)
    Organic_carbon = st.slider('Organic Carbon', min_value=5.0, max_value=50.0, step=0.1)
    Trihalomethanes = st.slider('Trihalomethanes', min_value=50, max_value=150, step=1)
    Turbidity = st.slider('Turbidity', min_value=1.0, max_value=100.0, step=0.1)

    # When the user clicks the 'Predict' button
    if st.button('Predict'):
        # Prepare the input data
        input_data = [[ph, Hardness, Solids,  Chloramines, Sulfate, Conductivity, Organic_carbon, Trihalomethanes, Turbidity]] 
        # Transform the input data using the pre-fitted scaler
        scaled_input_data = scale.transform(input_data)
        
        prediction = model.predict(scaled_input_data)
        probabilities = model.predict_proba(scaled_input_data)
        
        # Display the prediction
        if prediction[0] == 0:
            st.error('The water quality is predicted to be non-potable.')
            st.image('https://newsigns.com.au/cdn/shop/products/Non-Potable-Water.jpg?v=1608608300', width=300)           

        else:
            st.success('The water quality is predicted to be potable.')
            st.image('https://www.australiansafetysigns.net.au/cdn/shop/products/prohibition_POTABLE_WATER.jpeg?v=1571438535', width=300)
                       

if __name__ == '__main__':
    main()
