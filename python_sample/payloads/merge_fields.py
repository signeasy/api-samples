import json


class MergeFields:
    label = str
    value = str
    font_size = int

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["label", "value"]
        for key, val in kwargs.items():
            if getattr(self, key, None) is not None:
                if not isinstance(val, getattr(self, key, None)):
                    raise Exception("value for {} is not of valid type".format(key))

                setattr(self, key, val)

                if key in mandatory_fields:
                    mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        return json.dumps({"label": self.label, "value": self.value, "font_size": getattr(self, "font_size", None)})

    def to_dict(self):
        return {"label": self.label, "value": self.value, "font_size": getattr(self, "font_size", None)}
