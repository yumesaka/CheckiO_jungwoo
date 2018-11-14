class Friends:
    def __init__(self, connections):
        self.connections = list(connections)

    def add(self, connection):
        is_in = False
        if connection in self.connections:
            is_in = False
        else:
            self.connections.append(connection)
            is_in = True
        print(self.connections)
        return is_in

    def remove(self, connection):
        is_in = False
        if connection in self.connections:
            self.connections.remove(connection)
            is_in = True

        else:
            is_in = False

        print(self.connections)
        return is_in

    def names(self):
        name_in_connections = set()
        for connection in self.connections:
            for name in connection:
                name_in_connections.add(name)
        print(name_in_connections)
        return name_in_connections

    def connected(self, name):
        name_connected = set()
        for connection in self.connections:
            if name in connection:
                for element in connection:
                    name_connected.add(element)
        if name in name_connected:
            name_connected.remove(name)
        print(name_connected)
        return name_connected




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"

