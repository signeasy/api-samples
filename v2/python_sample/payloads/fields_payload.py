import json

type_fields = {"type": str, "email": str, "required": bool, "page_number": int, "x": int, "y": int, "height": int,
               "width": int, "additional_info": dict, "recipient_id": int, "original_id": int}


class FieldsPayload:
    email = ''
    type = ''
    required = False
    page_number = 0
    x = 0
    y = 0
    height = 0
    width = 0
    additional_info = {}

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["email", "type", "page_number", "x", "y", "height", "width"]
        for key, val in kwargs.items():
            setattr(self, key, val)

            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

    def __str__(self):
        return json.dumps({"email": self.email, "type": self.type, "required": self.required,
                           "page_number": self.page_number, "x": self.x, "y": self.y, "height": self.height,
                           "width": self.width, "additional_info": self.additional_info})

    def to_dict(self):
        return {"email": self.email, "type": self.type, "required": self.required, "page_number": self.page_number,
                "x": self.x, "y": self.y, "height": self.height, "width": self.width,
                "additional_info": self.additional_info}

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("{} should be a {}".format(name, str(type_fields.get(name))))
        super().__setattr__(name, value)


class EnvelopesFieldsPayload(FieldsPayload):
    recipient_id = 0
    original_id = 0

    def __init__(self, *args, **kwargs):
        mandatory_fields = ["recipient_id", "original_id"]
        for key, val in kwargs.items():
            setattr(self, key, val)

            if key in mandatory_fields:
                mandatory_fields.remove(key)

        if mandatory_fields:
            raise Exception("{} are missing".format(','.join(mandatory_fields)))

        super().__init__(*args, **kwargs)

    def __str__(self):
        return json.dumps({"email": self.email, "type": self.type, "required": self.required,
                           "page_number": self.page_number, "x": self.x, "y": self.y, "height": self.height,
                           "width": self.width, "additional_info": self.additional_info,
                           "recipient_id": self.recipient_id, "original_id": self.original_id})

    def to_dict(self):
        resp = super(EnvelopesFieldsPayload, self).to_dict()
        resp["recipient_id"] = self.recipient_id
        resp["original_id"] = self.original_id
        return resp

    def __setattr__(self, name, value):
        if not isinstance(value, type_fields.get(name)):
            raise Exception("{} should be a {}".format(name, str(type_fields.get(name))))
        super().__setattr__(name, value)