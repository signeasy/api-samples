import json

type_fields = {"label": str, "value": str, "font_size": int}


class MergeFields:
    label = ''
    value = ''
    font_size = 0

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["label", "value"]
        for key, val in kwargs.items():
            setattr(self, key, val)

            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        return json.dumps({"label": self.label, "value": self.value, "font_size": getattr(self, "font_size", None)})

    def to_dict(self):
        return {"label": self.label, "value": self.value, "font_size": getattr(self, "font_size", None)}

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("{} should be a {}".format(name, str(type_fields.get(name))))
        super().__setattr__(name, value)
