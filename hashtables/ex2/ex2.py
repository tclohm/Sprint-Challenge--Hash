#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):

	"""
	YOUR CODE HERE

	source string represents 
	starting point, source = None
	end point, destination = None
	"""
	cache = {}
	route = [None] * length

	for ticket in tickets:
		cache[ticket.source] = ticket.destination

	current = 'NONE'

	for index in range(length):
		route[index] = cache[current]
		current = cache[current]


	return route


# ticket_1 = Ticket("NONE", "PDX")
# ticket_2 = Ticket("PDX", "DCA")
# ticket_3 = Ticket("DCA", "NONE")

# tickets = [ticket_1, ticket_2, ticket_3]

# expected = ["PDX", "DCA", "NONE"]
# print(reconstruct_trip(tickets, 3))