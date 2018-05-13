data = 'X-DSPAM-Confidence:0.8475'
Confidence = data.find(':')
spot = float(Confidence)
print(spot)