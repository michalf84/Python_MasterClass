import shelve

bit=["bacon","lettuce","tomato","bread"]
beans_on_toast=["beans","bread"]
scrambled_egg=["eggs","butter","milk"]

soup=["tin of soup"]
paste=["pasta","cheese"]

# with shelve.open("recipes") as recipes:
    # recipes["bit"]=bit
    # recipes["beans_on_toast"]=beans_on_toast
    # recipes["soup"]=soup

    # recipes["bit"].append("potato") won't see it appended since data is appended to file but in memory was already loaded we won't see it!
    # TO FIX above problem solution below SOLUTION 1
    # temp_list=recipes["bit"]
    # temp_list.append("potato")
    # recipes["bit"]=temp_list
    # for snack in recipes:
    #     print(snack, recipes[snack])

#
with shelve.open("recipes",writeback=True) as recipes:
    recipes["bit"]=bit
    recipes["beans_on_toast"]=beans_on_toast
    recipes["soup"]=soup

    recipes["bit"].append("potato")
    # the disadvantage is that the above is updated in cache not in DB on closure it synchs that can lead to heavy IO to fix it see below
    # we can invike synch to force synch to db after action
    recipes["soup"]=soup
    recipes.synch()
    # be careful because now you won't see printed new value as it wrote to db but cache is old. best use updt emethod discused befofe
    soup.append("cream")
    for snack in recipes:
        print(snack, recipes[snack])