# Define a smallest_number function  that accepts a list of numbers.
# It should return the smallest value in the list.
#
# smallest_number([1, 2, 3])     => 1
# smallest_number([3, 2, 1])     => 1
# smallest_number([4, 5, 4])     => 4
# smallest_number([-3, -2, -1])  => -3

def smallest_number (smnu:list):
    zwei = smnu[0]
    for eins in smnu:
        if eins <= zwei:
            zwei = eins
    return zwei
	
	
#######################################


# Define a concatenate function that accepts a list of strings. 
#
# The function should return a concatenated string which consists of
# all list elements whose length is greater than 2 characters.
#
# concatenate(["abc", "def", "ghi"])      => "abcdefghi"
# concatenate(["abc", "de", "fgh", "ic"]) => "abcfgh"
# concatenate(["ab", "cd", "ef", "gh"])   => ""

def concatenate (conc:list):
    zwei=""
    for eins in conc:
        if len(eins) > 2:
            zwei += eins
    return zwei


#######################################



# Define a super_sum function that accepts a list of strings. 
# The function should sum the index positions of the first occurence of the letter “s” in each word. 
#
# Not every word is guaranteed to have an “s”.
# Don’t use "sum" as a variable name as it’s a built-in keyword.
#
# super_sum([])                                 => 0
# super_sum(["mustache"])                       => 2
# super_sum(["mustache", "greatest"])           => 8
# super_sum(["mustache", "pessimist"])          => 4
# super_sum(["mustache", "greatest", "almost"]) => 12

def super_sum (susu:list):
    zwei = 0
    for eins in susu:
        zwei += eins.index('s')
    return zwei