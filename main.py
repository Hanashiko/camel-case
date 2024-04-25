def camel_case(s):
    result = ""
    for i in s.split():
        result += i.capitalize()
    return result

print(camel_case("hello case"))
