from map import Mapping

if __name__ == "__main__":
    mapping = Mapping()
    built_map = mapping.create_map()
    mapping.save_map(built_map)