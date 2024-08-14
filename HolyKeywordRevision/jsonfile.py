import json

keyword_file = open("keywords.txt", "r")
keyword_and_definitions = keyword_file.readlines()
keyword_file.close()
keywords = []

chapter_reference_list = [
    "Computer Architecture",
    "Algorithms",
    "Designing Algorithms",
    "Programming",
    "Program Development",
    "Program Testing",
    "Ethics",
    "Number Systems & Applications",
    "Logic Gates",
    "Excel Theory",
    "Excel Functions",
    "Computer Networks",
]

# print(keyword_and_definitions)

chapter_index = 0

for keyword_definition in keyword_and_definitions:
    if keyword_definition == "\n":
        chapter_index += 1
        continue

    keyword_definition_list = keyword_definition.split(";")
    print(keyword_definition_list)

    keywords.append({
        "keyword": keyword_definition_list[0],
        "definition": keyword_definition_list[1],
        "chapter": chapter_reference_list[chapter_index]
    })

with open("keywords.json", "w") as final:
    json.dump(keywords, final)
