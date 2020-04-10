from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
                      )


def get_indices_of_item_weights(weights, length, limit):
    #create hash table
    ht = HashTable(16)

    
    #inputs: an array (weights), length()
    #output: a tuple containing (two values)

    #iterate through array
    for i in range(0, length): 
        
        current = weights[i] 

        #find if current item exists in the hashtable
        diff = hash_table_retrieve(ht, current)


        #if it doesnt exist 
        if diff is None: 
            #store the difference as a key and current as value
            hash_table_insert(ht, limit - current, current)

            #print(current)
        else: 
            return (i, weights.index( hash_table_retrieve(ht, current)))
    return None

print(get_indices_of_item_weights([4, 6, 10, 15, 16], 5,  21))

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
