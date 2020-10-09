import json

type_fields = {"id": int, "name": str}


class Originals:
    id = 0
    name = ''

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["id", "name"]

        for key, val in kwargs.items():
            setattr(self, key, val)
            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __setattr__(self, key, value):
        if not isinstance(value, type_fields.get(key) if not isinstance(type_fields.get(key), list) else list):
            raise Exception("{} should be a {}".format(key, type_fields.get(key) if not isinstance(type_fields.get(key),
                                                                                                   list) else list))
        super().__setattr__(key, value)

    def __str__(self):
        return json.dumps({"id": self.id, "name": self.name})

    def to_dict(self):
        return {"id": self.id, "name": self.name}
