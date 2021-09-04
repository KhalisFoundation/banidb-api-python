import banidb

if __name__ == '__main__':
    print("Code snippets BaniDB Python API")

    # [Start] Retrieve any shabad
    print("\nRetrieve a \"Random\" Shabad")
    shabad = banidb.random()
    print(shabad)
    # [End] Retrieve any shabad

    # [Start] Search a shabad
    print("\nSearch shabad by first letters")
    print("\tSearching Bandhana Har Bandhana ....")
    shabad = banidb.search("bhbgggr")
    print(shabad)
    # [End] Search a shabad

    # [Start] Retrieve by Shabad Id
    print("\nRetrieve Shabad by Shabad Id")
    shabad_id = 1111
    print(f"\tFetching shabad id = {shabad_id}")
    shabad = banidb.shabad(shabad_id)
    print(f"\n{shabad}")
    # [End ] Retrieve by Shabad Id

    # [Start] Retrieve by Shabad Id (Larivaar)
    print("\nRetrieve Shabad by Shabad Id in Larivaar mode")
    shabad_id = 1111
    print(f"\tFetching shabad id = {shabad_id}")
    shabad = banidb.shabad(1111, larivaar=True)
    print(f"\n{shabad}")
    # [End ] Retrieve by Shabad Id (Larivaar)

    # [Start] Amrit Kirtan Index
    print("\nRetrieve Index of Amrit Kirtan Pothi")
    ak_index = banidb.amritkeertan_index()
    print(f"Total Entries in Amrit Kirtan : {len(ak_index)}")
    print(ak_index[0])
    # [End] Amrit Kirtan Index

    # [Start] Retrieve history of searches
    print("\nRetrieve search history")
    hist = banidb.history()
    print(hist)
    # [End] Retrieve history of searches

    # [Start] Clear Cache
    print("\nClear search history")
    banidb.clear()
    hist = banidb.history()
    print(hist)
