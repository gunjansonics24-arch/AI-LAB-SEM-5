
def forward_chaining(KB, query):
    facts = set(KB["facts"])
    rules = KB["rules"]

    while True:
        new_facts = set()

        for premises, conclusion in rules:
            if all(premise in facts for premise in premises):
                if conclusion not in facts:
                    new_facts.add(conclusion)

        if query in new_facts:
            return True

        if not new_facts:
            return False

        facts.update(new_facts)


KB = {
    "facts": [
        "Human(Ram)"
    ],

    "rules": [
        (["Human(Ram)"], "Mortal(Ram)"),
        (["Mortal(Ram)"], "Dies(Ram)")
    ]
}

query = "Dies(Ram)"

print("Knowledge Base:")
for fact in KB["facts"]:
    print(fact)

print("\nQuery:", query)

if forward_chaining(KB, query):
    print("\nResult: TRUE")
    print("Query is proved using Forward Chaining.")
else:
    print("\nResult: FALSE")
    print("Query cannot be proved.")
