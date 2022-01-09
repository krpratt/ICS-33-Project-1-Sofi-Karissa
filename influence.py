import prompt
from goody       import safe_open
from math        import ceil 
from collections import defaultdict


def read_graph(open_file : open) -> {str:{str}}:
    infl_dict = defaultdict(set)
    for line in open_file:
        friends = line.split(';')
        if len(friends) == 1:
            infl_dict[friends[0]] = set()
        else:
            friend1, friend2 = friends
            infl_dict[friend1].add(friend2)
            infl_dict[friend2].add(friend1)
            
    return infl_dict
                                

def graph_as_str(graph : {str:{str}}) -> str:
    pass


def find_influencers(graph : {str:{str}}, trace : bool = False) -> {str}:
    pass


def all_influenced(graph : {str:{str}}, influencers : {str}) -> {str}:
    pass
       
            
    
if __name__ == '__main__':
    # Write script here
    file = safe_open('Select a file storing a friendship graph: ','r','Illegal File Name')
    infl_dict = read_graph(file)           
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

