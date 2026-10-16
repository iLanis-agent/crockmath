import json, math

def tenths(x):
    return math.floor(x * 10 + 0.5) / 10

def fixed1(x):
    return f"{tenths(x):.1f}"

def article(n):
    s = str(abs(int(n)))
    return "an" if s.startswith("8") or s.startswith("11") or s.startswith("18") else "a"

def convert_truth(minutes):
    if minutes <= 0:
        raise ValueError("the oven time must be above zero")
    high = tenths(minutes / 30 * 2)
    low = tenths(minutes / 30 * 4.5)
    return f"{minutes} oven minutes becomes about {fixed1(high)} hours on high or {fixed1(low)} hours on low honestly."

def fill_truth(load, cooker):
    if load <= 0:
        raise ValueError("the load must be above zero")
    if cooker <= 0:
        raise ValueError("the cooker must be above zero")
    f = tenths(load / cooker)
    if f > 1:
        band = "more stew than the cooker holds"
    elif f < 0.5:
        band = "under half full, so it runs hot and fast - check it early"
    elif f <= 0.7:
        band = "right in the half-to-three-quarter band"
    else:
        band = "past three-quarters, so it runs slow and crowds the lid"
    return (f"{fixed1(load)} quarts of stew in {article(cooker)} {fixed1(cooker)}-quart cooker "
            f"fills it {fixed1(f)} of the way, {band} honestly.")

def serving_truth(servings):
    if servings <= 0:
        raise ValueError("the serving count must be above zero")
    cups = tenths(servings * 1.5)
    quarts = tenths(cups / 4)
    word = "serving" if servings == 1 else "servings"
    verb = "asks" if servings == 1 else "ask"
    return f"{servings} {word} {verb} {fixed1(cups)} cups, {fixed1(quarts)} quarts, of stew honestly."

cases = []

def add(fn_name, args):
    try:
        fn = {"convertTruth": convert_truth, "fillTruth": fill_truth, "servingTruth": serving_truth}[fn_name]
        cases.append({"fn": fn_name, "args": args, "result": fn(*args)})
    except ValueError as e:
        cases.append({"fn": fn_name, "args": args, "error": str(e)})

# convertTruth
add("convertTruth", [60])   # 4.0 high, 9.0 low
add("convertTruth", [30])   # 2.0 high, 4.5 low
add("convertTruth", [45])   # 3.0 high, 6.8 low (6.75 -> 6.8)
add("convertTruth", [90])   # 6.0 high, 13.5 low
add("convertTruth", [0])    # error
# fillTruth
add("fillTruth", [3, 6])    # 0.5 in band
add("fillTruth", [2, 6])    # 0.3 under half
add("fillTruth", [5, 6])    # 0.8 past three-quarters
add("fillTruth", [4.2, 6])  # 0.7 edge -> in band
add("fillTruth", [7, 6])    # 1.2 more than it holds
add("fillTruth", [4, 8])    # an 8-quart article, 0.5 band
add("fillTruth", [0, 6])    # error
add("fillTruth", [3, 0])    # error
# servingTruth
add("servingTruth", [6])    # 9.0 cups, 2.3 quarts
add("servingTruth", [1])    # singular
add("servingTruth", [4])    # 6.0 cups, 1.5 quarts
add("servingTruth", [12])   # 18.0 cups, 4.5 quarts
add("servingTruth", [0])    # error

with open("expected.json", "w") as f:
    json.dump(cases, f, indent=2)
    f.write("\n")
print(f"{len(cases)} cases written")
for c in cases:
    print(c["fn"], c["args"], "->", c["result"] if "result" in c else "ERR: " + c["error"])
