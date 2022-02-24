# JSON - JavaScriptObjectNotation
import json
x = '{"name": "Ion", "age": 30, "city": "Iasi"}'
y = json.loads(x)
print(y, type(y))

z = y
print(z, type(z))
a = ["mere", "pere"]
print(json.dumps(a), type(a))
a = "hello"
print(json.dumps(a), type(a))
a = 42
print(json.dumps(a), type(a))
a = True
print(json.dumps(a), type(a))
a = None
print(json.dumps(a), type(a))