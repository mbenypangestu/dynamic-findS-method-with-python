import random

def main():
    sample_datas     = {}

    arr_data    = readFile("data.txt", "r")
    result_array= setToArray(arr_data)

    targets     = result_array['target']
    attributes  = result_array['attribute']

    first_hypothesis = getFirstHypothesis(targets, arr_data)
    final_hypothesis = getFinalHypothesis(targets, arr_data, first_hypothesis)

    showHypothesis(targets, final_hypothesis)

def readFile(filename, permission):
    data = []
    with open(filename, permission) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data

def setToArray(arr_data):
    target      = []
    attribute   = []

    for d in arr_data:
        line_words = d.split(',')
        if arr_data.index(d) == 0:
            for x in line_words:
                target.append(x)
        elif arr_data.index(d) == 1:
            for x in line_words:
                attribute.append(x)
    return {'target' : target, 'attribute' : attribute}

def getFirstHypothesis(targets, arr_data):
    first_hypothesis = {}
    for target in targets:
        first_hypothesis[target] = None

        for data in arr_data:
            data_words = data.split(',')
            if arr_data.index(data) > 1:
                if data_words[-1] == target:
                    data_words.pop()
                    first_hypothesis[target] = data_words
                    break
    return first_hypothesis

def getFinalHypothesis(targets, arr_data, hypothesis):
    for target in targets:
        for data in arr_data:
            data_words = data.split(',')
            if arr_data.index(data) > 1:
                if data_words[-1] == target:
                    data_words.pop()
                    for i in range(len(hypothesis[target])):
                        if hypothesis[target][i] != data_words[i]:
                            hypothesis[target][i] = '?'
    return hypothesis

def showHypothesis(targets, final_hypothesis):
    for target in targets:
        print("Hipotesa ", target, " \t: ", final_hypothesis[target])


if __name__ == "__main__":
    main()