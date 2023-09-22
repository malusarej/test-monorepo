import json

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        # Customize JSON serialization here for custom data types
        if isinstance(obj, complex):
            return {"__complex__": True, "real": obj.real, "imag": obj.imag}
        elif isinstance(obj, range):
            return {"__range__": True, "start": obj.start, "stop": obj.stop, "step": obj.step}
        return super().default(obj)

class CustomDecoder(json.JSONDecoder):
    def decode(self, s):
        obj = super().decode(s)
        # Customize JSON deserialization here for custom data types
        if "__complex__" in obj:
            return complex(obj["real"], obj["imag"])
        elif "__range__" in obj:
            return range(obj["start"], obj["stop"], obj["step"])
        return obj

def dumps(obj, **kwargs):
    return json.dumps(obj, cls=CustomEncoder, **kwargs)

def loads(s, **kwargs):
    return json.loads(s, cls=CustomDecoder, **kwargs)
