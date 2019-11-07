with open(".travis.yml") as in_file:
    print("\n".join(line.rstrip().replace("# ", "").replace("- language: ", "| ")
        for line in in_file if line.startswith(" " * 4)))
