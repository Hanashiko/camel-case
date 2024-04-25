def camel_case(s: str):
    result: str = ""
    for i in s.split():
        result += i.capitalize()
    return result

print(camel_case("hello case"))
