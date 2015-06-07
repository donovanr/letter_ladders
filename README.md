# letter_ladders
python code to find the longest word chain where deleting a letter makes another word

Sometimes I stare at words, and try to find smaller words that you can make by removing letters.
Sometimes, you can remove one letter at a time, and continue doing this, and always wind up with a real word.

For instnace, `string -> sting -> sing -> sin -> in -> i` is a chain that reaches one of the two commonly accepted one letter words in the English language.

I was curious to find the longest chain where this is the case.

This code work in two parts. First a word list is read and cleaned up, and a directed graph is made from the list, where
nodes are words, and a directed edge connects two words if you can delete a letter from the longer one to reach the shorter one.
Making the graph can take a while (~ 5--30 mins on my laptop, depending on the list of words).

After the graph is made, finding the longest chain is a simple problem, solved by topological sort on the dierected acyclic graph, and this algorithm:
http://en.wikipedia.org/wiki/Longest_path_problem

My code is adapted from the SO post:
http://stackoverflow.com/questions/17985202/networkx-efficiently-find-absolute-longest-path-in-digraph
