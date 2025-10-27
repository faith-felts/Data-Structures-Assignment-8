class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, number):
        contact = Contact(key, number)
        index = self.hash_function(key)
        current = self.data[index]

        if current is None:
            self.data[index] = Node(key, contact)
            return

        while current:
            if current.key == key:
                current.value = contact
                return
            if current.next is None:
                break
            current = current.next
        current.next = Node(key, contact)

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i, node in enumerate(self.data):
            print(f"Index {i}:", end=" ")
            if node is None:
                print("Empty")
            else:
                current = node
                while current:
                    print(f"- {current.value}", end=" ")
                    current = current.next
                print()


# --- Test your hash table implementation ---
table = HashTable(10)

table.print_table()

table.insert("Dave", "909-876-1234")
table.insert("Levi", "111-555-0002")

print("\nAfter inserts:")
table.print_table()

contact = table.search("Dave")
print("\nSearch result:", contact)
print()

print("Adding Amy and May (possible collision test):")
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")
table.print_table()
print()

# --- Edge Case #2: Duplicate key ---
print("Updating Levi's number:")
table.insert("Levi", "999-444-9999")
table.print_table()
print()
# --- Edge Case #3: Searching for missing contact ---
print("Searching for a missing contact (Faith):")
contact = table.search("Faith")
print("Search result:", contact)  # Expect None


'''
Why is a hash table the right structure for fast lookups?
A hash table is a great choice for storing and looking up data quickly because it doesn’t have to search through every item like a list does. 
Instead, it uses a hash function to turn a key into a specific index in the table. 
That means the program can jump right to where the data should be, which makes lookups and inserts really fast—usually in constant time, O(1).
This is especially useful when there are a lot of records, because the performance stays efficient no matter how large the dataset grows.

How did you handle collisions?
In my program, I handled collisions using separate chaining. This means that if two contacts happen to hash to the same index, I store them in a linked list at that position. 
Each node holds one contact, and the next pointer connects them. 
When I search for a name, the program walks through the linked list at that index until it finds the right one. 
This way, no data is lost, and duplicate keys can be easily updated.

When might an engineer choose a hash table over a list or tree?
An engineer would probably pick a hash table over a list or tree when speed is the main goal. 
A list has to search one item at a time, and a tree, while more organized, still needs comparisons at each level. 
A hash table is simple, direct, fast, and perfect for things like quick data lookups.
'''
