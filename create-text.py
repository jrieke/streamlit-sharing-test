# Creates an 80 MB file

with open("sample.txt", "w") as f:
    for _ in range(5000000):
        f.write("Hello Streamlit ")