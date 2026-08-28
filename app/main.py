def get_human_age(cat_age: int, dog_age: int) -> list:

    result = []
    cat_human_age = 0
    dog_human_age = 0
    if not isinstance(cat_age, int):
        raise TypeError("cat_age must be an integer")
    if not isinstance(dog_age, int):
        raise TypeError("dog_age must be an integer")
    if cat_age >= 15 and cat_age < 24:
        cat_human_age = 1
    elif cat_age >= 24 and cat_age < 28:
        cat_human_age = 2
    elif cat_age >= 28:
        cat_human_age = ((cat_age - 24) // 4) + 2
    if dog_age >= 15 and dog_age < 24:
        dog_human_age = 1
    elif dog_age >= 24 and dog_age < 30:
        dog_human_age = 2
    elif dog_age >= 29:
        dog_human_age = ((dog_age - 24) // 5) + 2

    result.append(cat_human_age)
    result.append(dog_human_age)
    return result
