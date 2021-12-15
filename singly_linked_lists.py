class SLNode:
        def __init__(self, val):
            self.value = val
            self.next = None

class SList:
        def __init__(self):
            self.head = None
        def add_to_front(self, val):        # this line takes a value
            new_node = SLNode(val)          # create a new instance of our Node class using the given value
            current_head = self.head        # save the current head in a variable
            new_node.next = current_head    # SET the new node's next TO the list's current head
            self.head = new_node	        # SET the list's head TO the node we created in the last step
            return self	                    # return self to allow for chaining
        def print_values(self):
            runner = self.head              # a pointer to the list's first node
            while (runner != None):         # iterating while runner is a node and not None
                print(runner.value)         # priint the current node's value
                runner = runner.next        # set the runner to it's neighbor
            return self                     # once the loop is done, return self to allow for chaining
        def add_to_back(self, val):         # accepts a value
            if self.head == None:	        # if the list is empty
                self.add_to_front(val)	    # run the add_to_front method
                return self                 # let's make sure the rest of this function doesn't happen if we add to the front
            new_node = SLNode(val)          # create a new instance of our Node class with the given value
            runner = self.head              # set an iterator to start at the front of the list
            while (runner.next != None):    # iterator until the iterator doesn't have a neighbor
                runner = runner.next        # increment the runner to the next node in the list
            runner.next = new_node	        # increment the runner to the next node in the list
            return self
        def remove_from_front(self):
            self.head = self.head.next
            return self
        def remove_from_back(self):
            last_node = self.head
            while last_node.next.next != None:
                last_node = last_node.next
            last_node.next = None
            return self
        def remove_val(self, val):
            if self.head.value == val:
                self.remove_from_front()
            else:
                runner = self.head
                while runner.next.value != val and runner.next.next != None:
                    runner = runner.next
                if runner.next.value == val:
                    runner.next = runner.next.next
            return self
        def insert_at(self, val, n):
            if n==0:
                self.add_to_front(val)
            elif n>0:
                insert_node=self.head
                index=0
                while n!=index+1 and insert_node.next!=None:
                    insert_node=insert_node.next
                    index+=1
                next_node=insert_node.next
                insert_node.next=SLNode(val)
                insert_node.next.next=next_node
            return self

my_list = SList()
my_list.add_to_front("Andy").add_to_front("Dwight").add_to_back("Jim").add_to_back("Pam").add_to_back("Michael").remove_from_front().remove_from_back().remove_val("Andy").insert_at("Michael", 1).print_values()