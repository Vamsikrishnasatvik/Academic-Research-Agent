import re

def get_citations(text):
    return re.findall(r"\[(\d+)\]", text)