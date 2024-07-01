# I want to find all possible combinations of two words given a sentence "word1 word2"
# I need to remove the . or ! or ? from the end of the sentence
# I need to split each word by space
# seems very similar to bubble search
# I loop through the indexes to find value word1 each time
# then I want the index following the index I'm looking at to get word 2

def bigram(sentence):
  list_of_strings = sentence[0:-1].split()
  bigrams = []

  #I want to start at 0 and end at 2nd to last index
  for index_one in range(len(list_of_strings)-1):
    # to find indexes 0 and 1 I want to start  1 ahead of
    # then I need to find 0 and 2
    # then 0 and 3
    # then 1 and 2
    # 1 and 3
    # 2 and 3
    # I want to start at index_one + 1 and end at the last index
    for index_two in range(index_one + 1, len(list_of_strings)):
      bigrams.append(list_of_strings[index_one] + " " + list_of_strings[index_two])

  return bigrams



print(bigram("Welcome to the jungle We Got."))