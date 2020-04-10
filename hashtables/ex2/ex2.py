from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)



class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


#inputs: array of objects that have a source and destination property
#outputs: an array of strings for route
def reconstruct_trip(tickets, length):
    #create a new hashtable with the length
    hashtable = HashTable(length)

    #an array 
    route = [None] * (length - 1)

    """
    YOUR CODE HERE
    """
    
    current = "NONE"
    #count = 0 
    for i in range(0, length):

       
        #insert all tickets into hash table
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)

        #the current nodes value is the key to the next destination

        if current is not None: 
        
            #get current value
            current = hash_table_retrieve(hashtable, current)

        


        
        
        #route[i] = current
        

    return route
        

ticket_1 = Ticket("PIT", "ORD")
ticket_2 = Ticket("XNA", "SAP")
ticket_3 = Ticket("SFO", "BHM")
ticket_4 = Ticket("FLG", "XNA")
ticket_5 = Ticket("NONE", "LAX")
ticket_6 = Ticket("LAX", "SFO")
ticket_7 = Ticket("SAP", "SLC")
ticket_8 = Ticket("ORD", "NONE")
ticket_9 = Ticket("SLC", "PIT")
ticket_10 = Ticket("BHM", "FLG")

tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]


print(reconstruct_trip(tickets, 10))