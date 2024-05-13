import streamlit as st
import pickle

pickle_in = open(r"model (1).pkl", 'rb')
predictor = pickle.load(pickle_in)

# Define a function to predict wine quality
def predict_closing(HIGH,LOW,CLOSE):
    prediction = predictor.predict([[HIGH,LOW,CLOSE]])
    return prediction[0]


# Main Streamlit app
def main():

    st.title('Closing price predictor 📈')
    st.sidebar.header('Input Features')

    HIGH = st.sidebar.text_input('HIGH',"" )
    LOW = st.sidebar.text_input('LOW',"" )
    CLOSE = st.sidebar.text_input('CLOSE',"" )
    # Display the selected input values
    st.subheader('Selected Features:')
    st.write(f'HIGH: {HIGH}')
    st.write(f'LOW: {LOW}')
    st.write(f'CLOSE: {CLOSE}')





    # Add a button to trigger prediction
    if st.sidebar.button('Predict'):
        # Call the prediction function
        prediction = predict_closing(HIGH,LOW,CLOSE)
        st.subheader('OPENING PRICE ')
        st.write(f'OPENING PRICE IS: {prediction}')


# Run the app
if __name__ == '__main__':
    main()
