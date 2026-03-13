import csv
import sys
from typing import TypedDict

from util import Node, StackFrontier, QueueFrontier


class Person(TypedDict):
    name: str
    birth: str
    movies: set[str]


class Movie(TypedDict):
    title: str
    year: str
    stars: set[str]


# Maps names to a set of corresponding person_ids
names: dict[str, set[str]] = {}  # name: {person_ids} (loaded as str from csv)

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people: dict[str, Person] = {}  # person_id: {name, birth, movies{1,2,3}}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies: dict[str, Movie] = {}  # movie_id: {title, year, stars{5,4,3}}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set(),
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set(),
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


def shortest_path(source: str, target: str):  # person_id, person_id
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target.

    If no possible path, returns None.
    """

    # TODO
    # raise NotImplementedError

    if source == target:
        return []

    # Breadth-First search
    queue = QueueFrontier()
    queue.add(Node(state=source, parent=None, action=None))  # source_node

    explored_states = {source}  # set(nodes)

    # process BFS queue
    while not queue.empty():
        node = queue.remove()

        if node.state == target:
            # build path via backtracking
            path = []  # [(movie_id, person_id)]
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent

            # source is not included in path
            # path: source -> target
            path.reverse()
            return path

        # state transition from current node
        # all movies of current person that connects to next person
        for movie_id in people[node.state]["movies"]:
            for person in movies[movie_id]["stars"]:
                if person in explored_states:
                    # all relationship paths originating from this node is already processed
                    # skip redundant cycles
                    continue

                queue.add(Node(state=person, parent=node, action=movie_id))

        explored_states.add(node.state)

    return None


def main():
    if len(sys.argv) > 2:
        sys.exit("Usage: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Loading data...")
    load_data(directory)
    print("Data loaded.")

    source = person_id_for_name(input("Name: "))
    if source is None:
        sys.exit("Person not found.")
    target = person_id_for_name(input("Name: "))
    if target is None:
        sys.exit("Person not found.")

    path = shortest_path(source, target)

    if path is None:
        print("Not connected.")
    else:
        degrees = len(path)
        print(f"{degrees} degrees of separation.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie_id = path[i + 1][0]
            if movie_id is not None:
                movie = movies[movie_id]["title"]
                print(f"{i + 1}: {person1} and {person2} starred in {movie}")


if __name__ == "__main__":
    main()
