countries = input().split(", ")
capitals = input().split(", ")
mix = {}

result = dict(zip(countries, capitals))

for key, value in result.items():
    print(f"{key} -> {value}")

