if __name__ == '__main__':
    import sys
    print(sys.path)

    sys.path.insert(0, 'ZStandardLibrary')
    sys.path.insert(0,'ZCodeSnippets')
    sys.path.insert(0,'ZZProject')

    print('-----------------------')
    print(sys.path)

    from KMean.k_means import distance
    print(distance((0, 0), (3,4)))
    # >>> 5.0

def foo_to_be_imported(x):
    return x*10
