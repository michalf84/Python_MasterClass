import shelve
with shelve.open("shelvetest") as fruit:
    fruit["orange"]=" as sweet orange"
    fruit["apple"]="red or green fruit"
    fruit["lemon"]="a lemon fruit"
    fruit["grape"]=" a swee t orange citrus frint"
    fruit["lime"]="similar to lemon fruit"

    print(fruit["lemon"])

# it wont work as it is outside with thus sleve closes
# print(fruit["lemon"])

# we can open shelve without  WITH statement, but then shelve must be closed manually

# you can mispell dicitonary that willput wrong values to db to remove them hou run
#     del fruit["erroredname"]

# update value
    fruit["grape"]="changed value"

    for x in fruit:
        print(x,":", fruit[x])