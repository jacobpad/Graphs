import random
from random import randint
import collections


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME
        ######################################################################
        # Reset Graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add User(s)
        for i in range(num_users):
            self.add_user(f'User {i}')

        # Create Frendships
        total_friendships = num_users * avg_friendships  # total_friendships
        added_friendships = 0

        while added_friendships < total_friendships:
            user_id_1 = randint(1, self.last_id)
            user_id_2 = randint(1, self.last_id)

            if user_id_1 != user_id_2 and user_id_2 not in self.friendships[user_id_1]:
                self.add_friendship(user_id_1, user_id_2)
                added_friendships += 2

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        ######################################################################
        path_queue = collections.deque()
        path_queue.append([user_id])

        while len(path_queue) > 0:
            path = path_queue.popleft()
            friend_id = path[-1]

            if friend_id in visited:
                continue

        visited[friend_id] = path

        # Enqueue more friends
        for id in self.friendships[friend_id]:
            new_path = path.copy()
            new_path.append(id)
            path_queue.append(new_path)

        # %age of connected users
        friend_coverage = (len(visited)-1) / (len(self.users)-1)
        print(
            f'Users in extended network (percentage): {friend_coverage*100:.01f}%')

        # Deg of seperation
        total_len = 0
        for p in visited.values():
            total_len += len(p) - 1
        if len(visited) > 1:
            avg_sep = total_len / (len(visited) - 1)
            print(f'Avg degree of seperation: {avg_sep}')
        else:
            print('No friends')

        return visited


# if __name__ == '__main__':
#     sg = SocialGraph()
#     sg.populate_graph(10, 2)
#     print(sg.friendships)
#     connections = sg.get_all_social_paths(1)
#     print(connections)



if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10000, 100)
    print(sg.friendships)
    print('\n')
    connections = sg.get_all_social_paths(1)
    print(connections)
