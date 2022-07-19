import json
from dict2xml import dict2xml
import inflect
inflector = inflect.engine()


size = 20

orig_data = {}

for x in range(1, size+1):
    orig_data[x] = inflector.number_to_words(x)


def format_data_one(data):
    ret = ""
    for k in data:
        if ret:
            ret += " "
        ret += '''"%s"="%s"''' % (k, data[k])
    return ret


print("python\n%s\n" % orig_data)
print("json\n%s\n" % (json.dumps(orig_data)))
print("xml\n%s\n" % (dict2xml(orig_data)))
print("key value %s\n" % (format_data_one(orig_data)))

json_len = len(json.dumps(orig_data))
xml_len = len(dict2xml(orig_data))
kv_len = len(format_data_one(orig_data))

print("Summary")
print("json: %d which is %d percent larger than key value" % (json_len, 100-((kv_len/json_len) * 100)))
print("xml: %d which is %d percent larger than key value" % (xml_len, 100-((xml_len/json_len) * 100)))
print("key value: %d" % kv_len)

