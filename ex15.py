from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_agian = raw_input(">")
txt_again = open (file_agian)

print txt_again.read()