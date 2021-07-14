portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]
 
def permutations(route, ports):
    # write the recursive function here
    # remember to print out the route as the recursion ends
    if len(ports) < 1:
        print(' '.join([portnames[i] for i in route])) 
    else:
        for k in range(len(ports)):         
           permutations(route+[ports[k]], ports[:k]+ports[k+1:])
        


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))
