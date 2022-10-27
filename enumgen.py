def gen_enum(input_items: [str]):
    for item in set(input_items):
        print(f"\t{item} = '{item}'")