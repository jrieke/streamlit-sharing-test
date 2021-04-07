import streamlit as st

# from aitextgen import aitextgen
# import gc

# from transformers import DistilBertTokenizer, DistilBertModel
# import numpy as np

st.title("Test")

# ---- aitextgen ----
# Result: Memory keeps increasing
# @st.cache(allow_output_mutation=True)
# def load_model():
#     return aitextgen()
# model = load_model()
# model = aitextgen()

# model = aitextgen()

# ---- aitextgen w/ manual gc ----
# Result: Memory fluctuates around ~700 MB but doesn't increase
#         I.e. the memory increase above is *just* an issue of (too) slow garbage collection!
#         That's obviously still a problem though, maybe we should run gc manually at each rerun?
#         Also, I need to check if this is the same for other apps, where memory is building up slowly.
# @st.cache(allow_output_mutation=True)
# gc.collect()
# def load_model():
#     return aitextgen()


# model = load_model()
# gc.collect(1)


# model = aitextgen()
# gc.collect()

# ---- transformers ----
# Result: Memory keeps increasing, but then it decreases suddenly (maybe just some delayed GC?)
# def load_model():
#     return DistilBertModel.from_pretrained("distilbert-base-uncased")
# model = load_model()

# ---- huge numpy array ----
# Result: Increases but decreases after some time
# def create_arr():
#     return np.random.rand(1000, 1000, 10)
# arr = create_arr()

# ---- opening files ----
# Result: Increases but decreases
# def read_file():
#     with open("sample.txt") as f:
#         content = f.read()
#     return content
# file_content = read_file()


# st.button("Click to trigger rerun")
st.markdown('<a href="https://github.com/jrieke">sdkf</a>sdlkfs', unsafe_allow_html=True)