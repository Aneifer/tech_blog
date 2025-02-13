def wortzaehler(text):
    woerter = text.split()
    return len(woerter)

text = "Sein, oder nicht sein, das ist hier die Frage."
print(wortzaehler(text))