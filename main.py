import random

def main():
    arr_data    = readFile("data.txt", "r")
    data_test   = readFile("data-testing.txt", "r")

    result_array    = setDataToArray(arr_data)
    arr_datatest    = setTestingToArray(data_test)

    targets     = result_array['target']
    attributes  = result_array['attribute']

    first_hypothesis = getFirstHypothesis(targets, arr_data)
    final_hypothesis = getFinalHypothesis(targets, arr_data, first_hypothesis)

    print("Data testing : ", arr_datatest)
    showHypothesis(targets, final_hypothesis)
    analyzeData(targets, final_hypothesis, arr_datatest)

def readFile(filename, permission):
    data = []
    with open(filename, permission) as file:
        for line in file:
            data.append(line.strip('\n'))
    return data

def setDataToArray(arr_data):
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

def setTestingToArray(data_test):
    result = []
    for i in range(len(data_test)):
        data_words = data_test[i].split(',')
        result.append(data_words)
    return result

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
    print()

def analyzeData(targets, final_hypothesis, data_test):
    for testing in data_test:
        status_target = {}
        print(testing, " : ",end='')
        for target in targets:
            # print(target,": ", end='')
            status_target[target] = True
            for i in range(len(testing)):
                if final_hypothesis[target][i] == '?': break
                if testing[i] != final_hypothesis[target][i]: status_target[target] = False
            # print(status_target[target])

        value_available = False
        for target in targets:
            if status_target[target] == True:
                print(target)
                value_available = True
                break
        if value_available == False:
            for target in targets:
                print("Bukan", target, " ", end='')
            print()
        # break


if __name__ == "__main__":
    main()