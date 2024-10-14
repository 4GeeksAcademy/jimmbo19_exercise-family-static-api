

from random import randint

class FamilyStructure:
        def __init__(self, last_name):
            self.last_name = last_name

            # example list of members
            self._members = [
                {"id": self._generateId(),
                "first_name": "John ",
                "last_name": self.last_name,
                "age": 33 ,
                "lucky_numbers": [7, 13, 22]},
                {"id": self._generateId(),
                "first_name": "Jane  ",
                "last_name": self.last_name,
                "age": 35 ,
                "lucky_numbers": [10, 14, 3]},
                {"id": self._generateId(),
                "first_name": "Jimmy  ",
                "last_name": self.last_name,
                "age": 33 ,
                "lucky_numbers": [1]},
            
            ]

        # read-only: Use this method to generate random members ID's when adding members into the list
        def _generateId(self):
            return randint(0, 99999999)

        def add_member(self, member):
            
            new_member = {
                "id": self._generateId(),
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
            self._members.append(new_member)
            return new_member 

        def delete_member(self, id):
            member = next((m for m in self._members if m["id"] == id), None)
            if member:
                self._members.remove(member)
                return {"done": True} 
            return {"done": False}  

        def get_member(self, id):
            member = next((m for m in self._members if m["id"] == id), None)
            return member  

        

        # this method is done, it returns a list with all the family members
        def get_all_members(self):
            return self._members
