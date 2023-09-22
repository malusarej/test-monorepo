import unittest
from jsonapi import CustomEncoder, CustomDecoder, dumps, loads

class TestJSONAPI(unittest.TestCase):

    def test_custom_encoder_complex(self):
        # Test encoding a complex number
        obj = complex(1, 2)
        encoder = CustomEncoder()
        encoded = encoder.encode(obj)
        self.assertEqual(encoded, '{"__complex__": true, "real": 1.0, "imag": 2.0}')

    def test_custom_decoder_complex(self):
        # Test decoding a complex number
        json_str = '{"__complex__": true, "real": 3.0, "imag": 4.0}'
        decoder = CustomDecoder()
        decoded = decoder.decode(json_str)
        self.assertEqual(decoded, complex(3, 4))

    def test_custom_encoder_range(self):
        # Test encoding a range object
        obj = range(1, 10, 2)
        encoder = CustomEncoder()
        encoded = encoder.encode(obj)
        self.assertEqual(encoded, '{"__range__": true, "start": 1, "stop": 10, "step": 2}')

    def test_custom_decoder_range(self):
        # Test decoding a range object
        json_str = '{"__range__": true, "start": 2, "stop": 20, "step": 5}'
        decoder = CustomDecoder()
        decoded = decoder.decode(json_str)
        self.assertEqual(decoded, range(2, 20, 5))

    def test_dumps_and_loads_complex(self):
        # Test dumps and loads with complex number
        obj = complex(2, 3)
        json_str = dumps(obj)
        loaded_obj = loads(json_str)
        self.assertEqual(loaded_obj, obj)

    def test_dumps_and_loads_range(self):
        # Test dumps and loads with range object
        obj = range(5, 50, 10)
        json_str = dumps(obj)
        loaded_obj = loads(json_str)
        self.assertEqual(list(loaded_obj), list(obj))

if __name__ == '__main__':
    unittest.main()
