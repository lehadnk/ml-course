def get_classification_parameters(tn, tp, fn, fp):
    accuracy = (tn + tp) / (tn + tp + fn + fp)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)

    return accuracy, precision, recall