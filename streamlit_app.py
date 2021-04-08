import streamlit as st

# from aitextgen import aitextgen
# import gc

# from transformers import DistilBertTokenizer, DistilBertModel
# import numpy as np

st.title("Testing iframes on S4A")

# st.multiselect(
#     "Select something",
#     [
#         "Some very long text that will be truncated",
#         "Short text",
#     ],
# )

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

"## For https://github.com/jrieke"
url = "https://github.com/jrieke"

"A Markdown link:"
st.markdown(f"[Click here]({url})")

"A HTML link:"
st.markdown(f'<a href="{url}" target="_blank">Click here</a>', unsafe_allow_html=True)

"An iframe (via `st.markdown`):"
st.markdown(f'<iframe src="{url}"></iframe>', unsafe_allow_html=True)

"An iframe (via `st.components.v1.iframe`):"
st.components.v1.iframe(url)


"## For https://www.jrieke.com/"
url = "https://www.jrieke.com/"

"A Markdown link:"
st.markdown(f"[Click here]({url})")

"A HTML link:"
st.markdown(f'<a href="{url}">Click here</a>', unsafe_allow_html=True)

"An iframe (via `st.markdown`):"
st.markdown(f'<iframe src="{url}"></iframe>', unsafe_allow_html=True)

"An iframe (via `st.components.v1.iframe`):"
st.components.v1.iframe(url)