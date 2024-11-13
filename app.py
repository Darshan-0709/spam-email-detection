import streamlit as st
import pickle

model = pickle.load(open('spam.pkl', 'rb'))
cv = pickle.load(open('vectorizer.pkl', 'rb'))

st.title("Email Span Classification Application")
st.write("This is a Machine Learingin applicatino to classify emails as sapm or ham.")
user_input = st.text_area("Enter an email to classify", height= 150)
if st.button("Classify"):
    if user_input:
        data = [user_input]
        vect = cv.transform(data).toarray()
        pred = model.predict(vect)
        if pred[0] == 0:
            st.write("This email is not spam")
            st.success("This email is not spam")
        else:
            st.write("This email spam")
            st.error("This email is spam")
        print(pred[0])
    else:
        print("Please try agai")