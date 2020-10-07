import json

type_fields = {"email": str}


class CC:
    email = ''

    def __init__(self, email):
        self.email = email

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("email should be a string")
        super().__setattr__(name, value)

    def __str__(self):
        return json.dumps({"email": self.email})

    def to_dict(self):
        return {"email": self.email}
