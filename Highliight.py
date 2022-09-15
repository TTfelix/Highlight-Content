import fitz
import pandas as pd

doc = fitz.open("R121.pdf")
df  = pd.read_csv("rr.csv")

data  = list(pd.read_csv("rr.csv"))


for p in doc:
  blocks = p.get_text("dict")["blocks"]
  for b in blocks:  # iterate through the text blocks
      for l in b["lines"]:  # iterate through the text lines
          for s in l["spans"]:  # iterate through the text spans
            if any(word == s["text"] for word in data):
              print(s["text"])
              line_quad = fitz.recover_line_quad(l)
              p.add_highlight_annot(line_quad)
