#6.5 Write code using find() and string slicing (see section 6.10)
#to extract the number at the end of the line below.
#Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(':')
value = text[colon_pos +1:].strip()

float_value = float(value)
print(float_value)