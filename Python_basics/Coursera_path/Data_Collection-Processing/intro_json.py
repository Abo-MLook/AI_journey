
"""
Again, python provides a module for doing this. The module is called json.
We will be using two functions in this module, loads and dumps.

"""
# json.loads() takes a string as input and produces a python object (a dictionary or a list) as output.
import json
a_string = '\n\n\n{\n "resultCount":25,\n "results": [\n{"wrapperType":"track", "kind":"podcast", "collectionId":10892}]}'
print(a_string)
d = json.loads(a_string)
print("------")
print(type(d))
print(d)
print(d.keys())
print(d['resultCount'])
# print(a_string['resultCount'])


"""The other function we will use is dumps. It does the inverse of loads. 
    It takes a python object, typically a dictionary or a list, and returns a string,
    in JSON format. It has a few other parameters. 
    Two useful parameters are sort_keys and indent.
    """
print()
print("-" * 20)
print()


def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2) # take dict and convret it to str with json format


d = {'key1': {'c': True, 'a': 90, '5': 50}, 'key2': {'b': 3, 'c': "yes"}}

print(d)
print('--------')
print(type(pretty(d)))
print(pretty(d))
