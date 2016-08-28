from markov_python.cc_markov import MarkovChain
from fetch_data import createSoup

article = raw_input('Provide the URL: ')

def skipLine():
  for i in range(3):
    print ''
#useful function for making space on the output console

def theScreen(text):
  skipLine()
  print "Here is your article: "
  skipLine()
  print createSoup(text)
  skipLine()
  print "Now, let's come up with some cool Markovian Magic. Your sentence will appear below..."
  skipLine()
  markovMagic(text)
#purpose of this function is to show the user the text before it becomes Markovian-ized

def markovMagic(blob):
  mc = MarkovChain()
  mc.add_string(createSoup(blob))
  mc_array = mc.generate_text()
  #print mc_array #useful for testing to compare array to final output
  DotheString(mc_array)
#this function gives you your Markovian array of values

def DotheString(the_string):
  output = ''
  x = 0
  for word in the_string:
    output += str(word)
    x += 1
    if x < len(the_string):
      output += " "
    else:
      output += "."
  output = output.capitalize()
  print output
  skipLine()
#this function converts the Markovian array into a string

theScreen(article)
#kicks off the function-fest of the program
