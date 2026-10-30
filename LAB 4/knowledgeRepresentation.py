
# Knowledge Representation using Python

# Representing knowledge using dictionaries

knowledge_base = {
    "Amit": {
        "age": 20,
        "course": "MCA",
        "subject": "Artificial Intelligence",
        "marks": 85
    },

    "Riya": {
        "age": 21,
        "course": "MCA",
        "subject": "Python",
        "marks": 90
    },

    "Rahul": {
        "age": 22,
        "course": "MCA",
        "subject": "Machine Learning",
        "marks": 78
    }
}

# Display all knowledge
print("Knowledge Base:")
for student, details in knowledge_base.items():
    print(student, ":", details)

# Retrieve specific knowledge
print("\nStudent Details:")
print("Amit's Age:", knowledge_base["Amit"]["age"])
print("Riya's Subject:", knowledge_base["Riya"]["subject"])

# Apply reasoning using facts
print("\nStudent Performance:")

for student, details in knowledge_base.items():

    if details["marks"] >= 80:
        result = "Excellent"
    else:
        result = "Needs Improvement"

    print(student, ":", result)

# Add new knowledge
knowledge_base["Neha"] = {
    "age": 20,
    "course": "MCA",
    "subject": "Data Science",
    "marks": 88
}

print("\nAfter Adding New Knowledge:")
print(knowledge_base["Neha"])
