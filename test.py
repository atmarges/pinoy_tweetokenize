from tweetokenize.tokenizer import Tokenizer

tweets = [
    "Ang dami kong kailangang gawin ngayong araw... :(",
    "Salamat at gumana din. Kapagod... 😫",
    "Thank you Lord. Natapos ko din lahat ng homeworks. 🙏😊",
]

# Create Tokenizer instance
tokenizer = Tokenizer()

# Test tokenize() method
tokens = ', '.join(tokenizer.tokenize(tweets[1]))
print(tokens.encode('utf-8'))  # Can't print on console unless encoded to utf-8

# Test tokenize_set() method
tokens = [', '.join(i) for i in tokenizer.tokenize_set(tweets)]
for i in tokens:
    print(i.encode('utf-8'))
