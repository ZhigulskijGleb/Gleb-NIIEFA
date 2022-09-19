def reverse_words(text):
    text=list(text)
    text.reverse()
    for i in text:
        n=''.join(i)
        print (n)
    return n
reverse_words('Привет, как дела')
