import json

type_fields = {"last_name": str, "first_name": str, "email": str, "role_id": int}


class Recipients:
    last_name = ''
    first_name = ''
    email = ''
    role_id = 0

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["first_name", "email", "role_id"]
        for key, val in kwargs.items():
            setattr(self, key, val)

            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        return json.dumps({"last_name": getattr(self, "last_name", None), "first_name": self.first_name,
                           "email": self.email, "role_id": self.role_id})

    def to_dict(self):
        return {"last_name": getattr(self, "last_name"), "first_name": self.first_name, "email": self.email,
                "role_id": self.role_id}

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("{} should be a {}".format(name, str(type_fields.get(name))))
        super().__setattr__(name, value)
