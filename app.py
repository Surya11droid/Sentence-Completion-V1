import pickle
import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

st.set_page_config(page_title="Next Word Prediction", layout="centered")


@st.cache_resource
def load_resources():
    model = load_model("lstm_model.h5")
    with open("tokenizer.pkl", "rb") as f:
        tokenizer = pickle.load(f)
    with open("max_len.pkl", "rb") as f:
        max_len = pickle.load(f)
    return model, tokenizer, max_len


try:
    model, tokenizer, max_len = load_resources()
except Exception as exc:
    st.error(f"Unable to load the trained model files: {exc}")
    st.stop()


def predict_next_word(text):
    if not text or not text.strip():
        return ""

    sequence = tokenizer.texts_to_sequences([text])[0]
    if not sequence:
        return ""

    padded_sequence = pad_sequences([sequence], maxlen=max_len, padding="pre")
    preds = model.predict(padded_sequence, verbose=0)
    predicted_index = int(np.argmax(preds, axis=-1)[0])

    reverse_word_index = {index: word for word, index in tokenizer.word_index.items()}
    return reverse_word_index.get(predicted_index, "")


st.title("🧠 Next Word Prediction")
st.write("Enter a sentence and the model will predict the next word.")

user_input = st.text_input("✍️ Enter text", placeholder="Type a sentence here...")

if st.button("Predict Next Word"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        next_word = predict_next_word(user_input)
        if next_word:
            st.success(f"**Predicted Next Word:** {next_word}")
        else:
            st.info("The model could not produce a prediction for that input.")

st.markdown("---")
st.caption("LSTM-based next word prediction app")
