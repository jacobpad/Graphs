from graph import Graph
print('\n\n')
print('∆'*75)
print('\n')
print('STARTING HERE vvv\n')

def earliest_ancestor(ancestors, starting_node):
    graph = Graph() # Instantiate graph

    for (parent, child) in ancestors: # Loop over the relationship from ancestors
        try:
            graph.get_neighbors(parent) # Try to get parent neighbors
        except KeyError:
            graph.add_vertex(parent) # If not ^, add the vertex
        try:
            graph.get_neighbors(child) # Try to get child neighbors
        except KeyError:
            graph.add_vertex(child) # If not ^, add the vertex
        graph.add_edge(child, parent) # Put the edges together

    def dft_ancestor_depth(child_id, depth): # Yep, it's a function within a function
        parents = graph.get_neighbors(child_id) # Set the parents
        current_depth = depth # This was passed in
        (earliest_id, deepest) = (child_id, current_depth) # Get something to work with
        for parent in parents: # Looping
            (ancestor_id, total_depth) = dft_ancestor_depth(parent, current_depth + 1) # recurse iiiiiiit
            if (total_depth > deepest) or (total_depth == deepest and ancestor_id < earliest_id): # The if
                (earliest_id, deepest) = (ancestor_id, total_depth) # Reset
        return (earliest_id, deepest) # The return

    (final, depth) = dft_ancestor_depth(starting_node, 0) # Returns
    if depth == 0:
        return -1
    else:
        return final





    





























print('\nENDING HERE ^^^')