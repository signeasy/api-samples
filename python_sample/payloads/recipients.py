import json


class Recipients:
    last_name = ''
    first_name = ''
    email = ''
    role_id = 0

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["first_name", "email", "role_id"]
        for key, val in kwargs.items():
            if getattr(self, key, None) is not None:
                if not isinstance(val, type(getattr(self, key, None))):
                    raise Exception("value for {} is not of valid type".format(key))

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
