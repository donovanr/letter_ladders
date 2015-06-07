# functions for finding the longerst letter ladders in a word corpus

import networkx as nx

# group words by their length
def group_wordlist_by_len(some_wordlist):
    word_lens_some_wordlist = [len(word) for word in some_wordlist]
    
    some_wordlist_grouped_by_length = [[] for x in xrange(max(word_lens_some_wordlist)+1)]
    for i,word_len in enumerate(word_lens_some_wordlist):
        some_wordlist_grouped_by_length[word_len].append(some_wordlist[i])
    return some_wordlist_grouped_by_length


# starting with an edgeless graph where the nodes are words in the wordlist,
# add an edge between two words if you can delete a letter from the longer word
# to reach a smaller word that's also in the wordlist

# You also need to have grouped the wordlist into sublists of words of the same length,
# where the L-th sublist contains all the words of length L

# this function works on one word (L) length at a time, and adds eges to the word graph in place

def ersosion_filter_nx(L,some_graph,some_wordlist_grouped_by_len):    
    for word in some_wordlist_grouped_by_len[L]:
        for l,letter in enumerate(word):
            candidate = word[:l] + word[(l+1):]
            if candidate in some_wordlist_grouped_by_len[L-1]:
                some_graph.add_edge(candidate,word)


# find all longest (and next-longest paths in a DAG G

def find_all_longest_and_next_longest_paths(G):
    dist = {} # stores [node, distance] pair
    for node in nx.topological_sort(G):
        # pairs of dist,node for all incoming edges
        pairs = [(dist[v][0]+1,v) for v in G.pred[node]]
        if pairs:
            dist[node] = max(pairs)
        else:
            dist[node] = (0, node)
    node,(max_length,_)  = max(dist.items(), key=lambda x:x[1])
    
    max_node_set = [[],[]]
    max_node_set[0] = [x[0] for x in dist.items() if x[1][0] == max_length]   # longest paths
    max_node_set[1] = [x[0] for x in dist.items() if x[1][0] == max_length-1] # next longest paths

    all_longest_and_next_longest_paths = [[],[]]
    for i,node_set in enumerate(max_node_set):
        all_start_end_pairs = []
        for a_max_node in max_node_set[i]:
            start_end_pair = []
            length = max_length
            while length > 0:
                start_end_pair.append(a_max_node)
                length,a_max_node = dist[a_max_node]
            all_start_end_pairs.append(start_end_pair)
        
        every_single_max_path = []
        for unique_ends in all_start_end_pairs:
            for p in nx.all_shortest_paths(G,source=unique_ends[-1],target=unique_ends[0]):
                every_single_max_path.append(list(reversed(p)))
        all_longest_and_next_longest_paths[i] = every_single_max_path
    
    return all_longest_and_next_longest_paths

# pretty print out the longest and next longest paths
def print_paths(path_set):
    print 'length of longest path is ' + str(len(path_set[0][0]))
    for path in path_set[0]:
        print path
    
    print '\n'

    print 'length of next longest path is ' + str(len(path_set[1][0]))
    for path in path_set[1]:
        print path
