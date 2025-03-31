def piece_of_cake(prices, optionals=None, **ingredients):
    """
    Calculates the total price for the recipe based on ingredient quantities and their prices.
    
    :param prices: Dictionary where keys are ingredient names and values are the price per 100 grams.
    :param optionals: List of ingredients to be ignored when calculating the price (optional).
    :param ingredients: Ingredient names and their quantities in grams to be purchased.
    :return: Total price for all the ingredients needed for the recipe.
    """
    if optionals is None:
        optionals = []

    total_price = 0

    for ingredient, quantity in ingredients.items():
        if ingredient not in optionals and ingredient in prices:
            total_price += (prices[ingredient] * quantity) / 100

    return total_price


if __name__ == "__main__":
    prices = {
        "flour": 1.5,
        "sugar": 2.0,
        "butter": 3.0,
        "egg": 0.5
    }

    ingredients = {
        "flour": 200,
        "sugar": 100,
        "butter": 50,
        "egg": 2
    }

    optionals = ["egg"]

    total_price = piece_of_cake(prices, optionals, **ingredients)
    print(f"Total recipe price: ${total_price:.2f}")
