import csv
import math
import random

class DecisionTree():
    tree = {}

    def learn(self, training_set, attributes, target):
        self.tree = build_tree(training_set, attributes, target)

class Node():
    value = ""
    children = []

    def __init__(self, val, dictionary):
        self.value = val
        if (isinstance(dictionary, dict)):
            self.children = dictionary.keys()

def get_class(line):
    return line[0]

def get_parametros(line):
    line.pop(0)
    return line

def entropy(atributos, data, atributo):
    freq = {}
    dataEntropy = 0.0

    i = 0
    for entry in atributos:
        if (atributo == entry):
            break
        i = i + 1

    i = i - 1

    for entry in data:
        if (entry[i] in freq):
            print(entry[i])
            freq[entry[i]] += 1.0
        else:
            print(entry[i])
            freq[entry[i]]  = 1.0

    for freq in freq.values():
        dataEntropy += (-freq/len(data)) * math.log(freq/len(data), 2) 
    
    print(dataEntropy)
    return dataEntropy

def get_list():
    lista = []
    with open('risco.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            lista.append(row) 
        return lista
        
def id3(lista):
    classe = get_class(lista[0])
    atributos  = get_parametros(lista[0])
    result = entropy(atributos, lista , random.choice(atributos))

def main():
    lista = get_list()
    id3(lista)

if __name__ == "__main__":
    main()