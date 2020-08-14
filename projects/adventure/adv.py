from room import Room
from player import Player
from world import World

import collections
from ast import literal_eval


# Load world
world = World()

# Fix the file paths
map_file = "projects/adventure/maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "projects/adventure/maps/test_loop.txt"
# map_file = "projects/adventure/maps/test_loop_fork.txt"
# map_file = 'projects/adventure/maps/main_maze.txt'

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
player.current_room = world.starting_room

####################
# Helper functions #
####################


def add_room_to_map(room):
    if room not in room_map:  # If we don't already have it,
        room_map[room] = {'n': '?', 's': '?', 'e': '?', 'w': '?'}  # Add it
        exits = room.get_exits()  # Find the exits variable

        for direction in room_map[room]:  # Look all 4 directions
            if direction not in exits:  # Find the exits: action code
                # If there's no exit, mark it
                room_map[room][direction] = 'NONE'
        return True  # Actually run the code
    else:  # If the room is in the map already, we've visited it
        return False  # We've been here already, no need to mark it up again


def add_relation_to_map(starting_room, direction, ending_room):
    room_map[starting_room][direction] = ending_room  # Where to end
    room_map[ending_room][inverse[direction]] = starting_room  # Where to start


def path_to_nearest_room_with_unexplored_exits(starting_room):
    visited = set()
    path_queue = collections.deque()
    path_queue.append((starting_room, []))  # Start putting em together

    while len(path_queue) > 0:  # If a path exists
        room, path = path_queue.popleft()  # Start removing

        if room in visited:  # If we've been to the room
            continue  # Keep going
        else:
            visited.add(room)  # Add it if we haven't visited

        for each_exit in room_map[room]:  # Keep looking for exits
            if room_map[room][each_exit] == '?':
                return path
            elif room_map[room][each_exit] != 'NONE':
                new_path = path.copy()
                new_path.append(each_exit)
                new_room = room_map[room][each_exit]
                path_queue.append((new_room, new_path))

    return []


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

default_direction = 's'
change_directions = {'n': 'e', 'e': 's', 's': 'w', 'w': 'n'}
inverse = {'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}
room_map = {}


add_room_to_map(player.current_room)


while len(room_map) < len(room_graph):  # If we're not done exploring
    room = player.current_room  # In the room
    exits = room.get_exits()  # Check for exits
    found_unfound_exits = False
    direction = default_direction  # Which way to go

    for _ in range(len(change_directions)):
        if room_map[room][direction] == '?' and direction in exits:  # Shall I go somewhere new?
            found_unfound_exits = True

            player.travel(direction)  # Move
            next_room = player.current_room  # Update the room
            traversal_path.append(direction)  # Add to how I got here

            if not add_room_to_map(next_room):  # Lets go back
                player.travel(inverse[direction])
                traversal_path.pop()

            # Add it to the map
            add_relation_to_map(room, direction, next_room)
            break
        else:
            direction = change_directions[direction]

    if not found_unfound_exits:  # Nowhere to go, go somewhere else
        path = path_to_nearest_room_with_unexplored_exits(room)

        traversal_path.extend(path)  # Putting it all together
        for direction in path:
            player.travel(direction)


##################################
#  VV   PRE GENERATED CODE  VV   #
##################################

# TRAVERSAL TEST
visited_rooms = set()  # A record
player.current_room = world.starting_room

visited_rooms.add(player.current_room)


for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
