
# Semantic Network using Python

# Representing nodes and relationships

semantic_network = {
    "Dog": {
        "IS-A": "Mammal",
        "HAS-A": "Tail",
        "CAN-DO": "Bark"
    },

    "Cat": {
        "IS-A": "Mammal",
        "HAS-A": "Tail",
        "CAN-DO": "Meow"
    },

    "Mammal": {
        "IS-A": "Animal",
        "HAS-A": "Warm Blood"
    },

    "Animal": {
        "NEEDS": "Food",
        "CAN-DO": "Move"
    }
}

# Display semantic network
print("===== Semantic Network =====")

for node, relations in semantic_network.items():

    for relation, value in relations.items():

        print(node, "--", relation, "-->", value)


# Search for relationships
print("\n===== Dog Relationships =====")

for relation, value in semantic_network["Dog"].items():
    print(relation, ":", value)


# Check whether a relationship exists
def check_relation(node, relation):

    if node in semantic_network:
        if relation in semantic_network[node]:
            return semantic_network[node][relation]

    return "Relationship not found"


print("\nDog IS-A:",
      check_relation("Dog", "IS-A"))

print("Cat CAN-DO:",
      check_relation("Cat", "CAN-DO"))

print("Mammal IS-A:",
      check_relation("Mammal", "IS-A"))
