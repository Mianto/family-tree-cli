from typing import List
import json
from collections import defaultdict


PERSON_KEY = "person"
RELATIONSHIP_KEY = "relationships"
PERSON_TO_RELATIONSHIP_KEY = "person_to_relationship"
ADJ_RELATIONSHIP = {
    "son": "father",
    "daughter": "father",
    "wife": "husband",
    "husband": "wife"
}
PLURAL_TO_SINGULAR_RELATIONSHIP = {
    "sons": "son",
    "daughters": "daughter",
    "wives": "wife"
}


class PersonService:
    def __init__(self) -> None:
        self.person_list: List[str] = []
        self.relationship: List[str] = []
        self.person_to_relationship = defaultdict(list)

    def add_person(self, person) -> None:
        self._load_from_json()
        if person in self.person_list:
            raise Exception("Person with name {} already present", person)
        self.person_list.append(person)
        self._save_to_json()

    def add_relationship(self, relation) -> None:
        self._load_from_json()
        if relation in self.relationship:
            raise Exception("Relationship {} already present", relation)
        self.relationship.append(relation)
        self._save_to_json()

    def connect_person_relationship(self, person1, person2, relation) -> None:
        self._load_from_json()
        if person1 not in self.person_list or person2 not in self.person_list:
            raise Exception("Person not present")
        
        if relation not in self.relationship:
            raise Exception("Relationship not present")
        
        self.person_to_relationship[person1].append([person2, relation])
        if relation in ADJ_RELATIONSHIP.keys():
            self.person_to_relationship[person2].append([
                person1, ADJ_RELATIONSHIP[relation]])

        self._save_to_json()

    def find_count_in_relation(self, relation_name, person_name):
        self._load_from_json()
        if person_name not in self.person_list:
            raise Exception("Person not present")

        if person_name not in self.person_to_relationship.keys():
            raise Exception("No relationship found for : {}", person_name)
        
        singular_name = relation_name
        
        if relation_name in PLURAL_TO_SINGULAR_RELATIONSHIP.keys():
            singular_name = PLURAL_TO_SINGULAR_RELATIONSHIP[relation_name]
        
        count = 0
        for person, relations in self.person_to_relationship.items():
            for relation in relations:
                if relation[0] == person_name and relation[1] == singular_name: 
                    count += 1
        return count

    def find_relative(self, relative, person_name):
        self._load_from_json()
        if person_name not in self.person_list:
            raise Exception("Person not present")
        
        for person, relations in self.person_to_relationship.items():
            for relation in relations:
                if relation[1] == relative and relation[0] == person_name:
                    return person
            
    
    def _load_from_json(self):
        try:
            with open('json_data.json', 'r') as f:
                data = json.load(f)
                self.person_list = data[PERSON_KEY]
                self.relationship = data[RELATIONSHIP_KEY]
                self.person_to_relationship = defaultdict(list, data[PERSON_TO_RELATIONSHIP_KEY])
        except Exception as e:
            # print(e)
            pass

    def _save_to_json(self):
        di = {PERSON_KEY: self.person_list, RELATIONSHIP_KEY: self.relationship,
              PERSON_TO_RELATIONSHIP_KEY: self.person_to_relationship}
        with open('json_data.json', 'w+') as outfile:
            json.dump(di, outfile)
