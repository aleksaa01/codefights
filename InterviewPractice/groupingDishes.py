def groupingDishes(dishes):
    ingredients = {}
    for row in dishes:
        dish = row[0]
        for i in range(1, len(row)):
            if row[i] in ingredients:
                ingredients[row[i]].append(dish)
            else:
                ingredients[row[i]] = [dish, ]

    res = []
    for ing in sorted(ingredients.keys()):
        dishes = ingredients[ing]
        if len(dishes) <= 1:
            continue
        res.append([ing, ] + sorted(dishes))

    return res



"""
You are given a list dishes, where each element consists of a list of strings beginning with the name of the dish,
followed by all the ingredients used in preparing it. You want to group the dishes by ingredients,
so that for each ingredient you'll be able to find all the dishes that contain it (if there are at least 2 such dishes).

Return an array where each element is a list beginning with the ingredient name,
followed by the names of all the dishes that contain this ingredient.
The dishes inside each list should be sorted lexicographically,
and the result array should be sorted lexicographically by the names of the ingredients.
"""