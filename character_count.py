import pprint

msg= 'It was a bright cold day in April and clock were striking thirteen'
count={}

for character in msg.upper():
    count.setdefault(character,0)
    count[character]=count[character]+1

pprint.pprint(count)

text=pprint.pformat(count)
print(text)
