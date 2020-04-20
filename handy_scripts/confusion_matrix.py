output = torch.randn(batch_size, n_classes) # refer to output after softmax
target = torch.randint(0, n_classes, (batch_size,)) # labels

def confusion_matrix(preds, labels):

    preds = torch.argmax(preds, 1)
    conf_matrix = torch.zeros(n_classes, n_classes)
    for p, t in zip(preds, labels):
        conf_matrix[p, t] += 1

    print(conf_matrix)
    TP = conf_matrix.diag()
    for c in range(n_classes):
        idx = torch.ones(n_classes).byte()
        idx[c] = 0
        TN = conf_matrix[idx.nonzero()[:,None], idx.nonzero()].sum()
        FP = conf_matrix[c, idx].sum()
        FN = conf_matrix[idx, c].sum()

        sensitivity = (TP[c] / (TP[c]+FN))
        specificity = (TN / (TN+FP))

        print('Class {}\nTP {}, TN {}, FP {}, FN {}'.format(
            c, TP[c], TN, FP, FN))
        print('Sensitivity = {}'.format(sensitivity))
        print('Specificity = {}'.format(specificity))
    
confusion_matrix(output, target) 
