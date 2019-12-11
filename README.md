# pinoy_tweetokenize
A modified version of [tweetokenize](https://github.com/jaredks/tweetokenize) designed for tokenizing Philippine tweets.

Modifications made includes:
- Code updated from Python 2 to Python 3
- Hashtags containing camelcase letters are split into separate tokens. For instance, "#HomeSweetHome" is converted into ['#', 'home', 'sweet', 'home']. Hashtags that don't use camelcase are converted into a single token without the # symbol.
- One unique feature of Tagalog as compared to English is the use of repeating syllables. This allows the speaker to indicate the tense of the verb being used (i.e. maglaba to maglalaba). Elongating some of the syllables of words can indicate expressing a strong emotion (i.e. hehe to hehehehehehe). However, to shorten word count, a limitation was set limiting the maximum number of repeating syllables to three.
- Each emoji is considered to be a separate token.
- A file named 'emojis.txt' is included inside the lexicon folder. This makes adding new emoji for token filtering easier.

## Usage
```python
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

```
