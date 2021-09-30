import csv
import sys
import collections

def __main__ ():
    input_name = 'simple_test3'
    # for i in range(5):
        # Read_graph(google_test_small)
    Make_scaph().Make_graph(input_name)



class Make_scaph:
    def __init__(self):

        self.name = []
        self.graph = []


    def Make_graph(self, name):
        self.name = name
        path = './%s.csv'%name
        r=open(path)
        data=csv.reader(r)
        header = next(data)
        graph = []
        Udlist = []
        Pudlist = []
        for rr in data:
            graph.append(rr)
        print(graph)

        for i in range(len(graph)):
            graph[i].append(-1)
            if i == 0 or i == (len(graph)//2) or i == (len(graph)-1) or graph[i][0] == graph[0][0] or graph[i][0] == graph[len(graph)//2][0] or graph[i][0] == graph[len(graph)-1][0]:
                graph[i][2] = 1
                Udlist.append(graph[i][1])

        print(graph)
        print(Udlist)

        counter = collections.Counter(Udlist)
        for key in counter:
            if counter[key] == 3:
                Pudlist.append(key)
        print(Pudlist)

        for k in Pudlist:
            for n in range(len(graph)):
                if graph[n][0] == k:
                    graph[n][2] = 0
        print(graph)

        # for j in range(len(graph)):
        #     if



        return graph

    # def Scaph_VDDS(self):




__main__()

/////////////////////////////////////////////////////////////
import csv
import sys
import collections

def __main__ ():
    input_name = 'simple_test3'
    # for i in range(5):
        # Read_graph(google_test_small)
    Make_scaph(input_name).Make_graph()



class Make_scaph:
    def __init__(self,name):

        self.name = name
        # self.graph = []


    def Make_graph(self):
        name = self.name
        path = './%s.csv'%name
        r=open(path)
        data=csv.reader(r)
        header = next(data)
        graph = []
        Udlist = []
        Pudlist = []
        for rr in data:
            graph.append(rr)
        print(graph)

        for i in range(len(graph)):
            graph[i].append(-1)
            if i == 0 or i == (len(graph)//2) or i == (len(graph)-1) or graph[i][0] == graph[0][0] or graph[i][0] == graph[len(graph)//2][0] or graph[i][0] == graph[len(graph)-1][0]:
                graph[i][2] = 1
                Udlist.append(graph[i][1])

        print(graph)
        print(Udlist)

        counter = collections.Counter(Udlist)
        for key in counter:
            if counter[key] == 3:
                Pudlist.append(key)
        print(Pudlist)

        for k in Pudlist:
            for n in range(len(graph)):
                if graph[n][0] == k:
                    graph[n][2] = 0
        print(graph)

        # for j in range(len(graph)):
        #     if



        return graph

    # def Scaph_VDDS(self):




__main__()

