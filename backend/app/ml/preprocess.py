def split_features_target(dataset):

    X = dataset.drop("label", axis=1)

    y = dataset["label"]

    return X, y
