import utils

if __name__ == "__main__":

    paths = []
    for i in range(100):
        paths.append(utils.random_path())
    
    utils.hash_all(paths)
    
