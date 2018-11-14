# def check_connection(network, first, second):
#     parsed = dict()
#     for l, r in map(lambda i: i.split("-"), network):
#         parsed.setdefault(l, []).append(r)
#         parsed.setdefault(r, []).append(l)
#
#     queue = parsed[first]
#     closed = {first}
#     while queue:
#         current = queue.pop(0)
#         if current in closed:
#             continue
#         if second == current:
#             return True
#         closed.add(current)
#         queue.extend(parsed[current])
#     return False


def check_connection(network, first, second):
    parsed = dict()
    for element in network:
        r, l = element.split("-")
        parsed.setdefault(r, []).append(l)
        parsed.setdefault(l, []).append(r)

    queue = parsed[first]
    closed = set()
    closed.add(first)

    while queue:
        current = queue.pop(0)
        if current in closed:
            continue
        if current == second:
            return True
        closed.add(current)
        queue.extend(parsed[current])
    return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") == True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") == True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") == False, "I don't know any scouts."
