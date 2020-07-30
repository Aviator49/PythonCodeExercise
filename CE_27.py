# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]


def word_lengths (wole:str):
    eins = []
    
    zwei = wole.split(" ")
    
    for drei in zwei:
        eins.append(len(drei))
    return eins
	
	
##############################

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup (clean:list):
    
    delimiter = " "
    eins = []
    for zwei in clean:
        if len(zwei) == 0 or zwei.isspace():
            continue
        eins.append(zwei)
    return delimiter.join(eins)