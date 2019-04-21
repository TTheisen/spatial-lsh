import utils

if __name__ == "__main__":

    paths = []
    for i in range(10):
        paths.append(utils.random_path())
    
    hashes = utils.hash_all(paths)
    convolutions = utils.convolution_all(hashes, 5)