import pickle
import streamlit as st


pickle_in = open(r"trading_model (1).pkl", 'rb')
predictor = pickle.load(pickle_in)

# Define a function to predict wine quality
def predict_closing(OPEN,HIGH,LOW,CLOSE,OPEN_CLOSE,HIGH_LOW,CHANGE):
    prediction = predictor.predict([[OPEN,HIGH,LOW,CLOSE,OPEN_CLOSE,HIGH_LOW,CHANGE]])
    prob = predictor.predict_proba([[OPEN,HIGH,LOW,CLOSE,OPEN_CLOSE,HIGH_LOW,CHANGE]])
    return prediction[0],prob[0][0],prob[0][1]


# Main Streamlit app
def main():

    st.title('Closing price predictor 📈')
    st.sidebar.header('Input Features')
    OPEN = st.sidebar.text_input('OPEN',"" )
    HIGH = st.sidebar.text_input('HIGH',"" )
    LOW = st.sidebar.text_input('LOW',"" )
    CLOSE = st.sidebar.text_input('CLOSE',"" )
    PREV_CLOSE = st.sidebar.text_input('PREV_CLOSE',"" )

    # Display the selected input values
    st.subheader('Selected Features:')
    st.write(f'OPEN: {OPEN}')
    st.write(f'HIGH: {HIGH}')
    st.write(f'LOW: {LOW}')
    st.write(f'CLOSE: {CLOSE}')
    st.write(f'PREV CLOSE: {PREV_CLOSE}')


    # Add a button to trigger prediction
    if st.sidebar.button('Predict'):
        # Call the prediction function
        OPEN_CLOSE = float(OPEN) - float(CLOSE)
        HIGH_LOW = float(HIGH) - float(LOW)
        CHANGE = (float(CLOSE) - float(PREV_CLOSE))/float(CLOSE)
        prediction = predict_closing(OPEN,HIGH,LOW,CLOSE,OPEN_CLOSE,HIGH_LOW,CHANGE)
        st.subheader('OPENING PRICE ')
        st.write(f'Prediction and probabilities are : {prediction[0]}')
        st.write(f'Probabilty of 0 :{prediction[1]}')
        st.write(f'Probabilty of 1 :{prediction[2]}')
        if prediction[0] == 1:
            st.write('The opening price is predicted to increase tomorrow.')
        else:
            st.write('The opening price is predicted to decrease tomorrow.')
        st.write()

# Run the app
if __name__ == '__main__':
    main()
