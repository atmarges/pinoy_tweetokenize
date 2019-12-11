from tweetokenize.tokenizer import Tokenizer

tweets = [
    "Ang dami kong kailangang gawin ngayong araw... :(",
    "Salamat at gumana din. Kapagod... 😫",
    "Thank you Lord. Natapos ko din lahat ng homeworks. 🙏😊",
]

# Create Tokenizer instance
tokenizer = Tokenizer()

# Test tokenize() method
tokens = tokenizer.tokenize(tweets[1])
output = ', '.join(tokens)
print(output.encode('utf-8'))  # Can't print on console unless encoded to utf-8

# Test tokenize_set() method
tokens_set = tokenizer.tokenize_set(tweets)
output = [', '.join(i) for i in tokens_set]
for i in output:
    print(i.encode('utf-8'))
