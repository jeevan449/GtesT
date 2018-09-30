from Finder import Test_Finder
import pdb
class Runner:
    def __init__(self):
        obj = Test_Finder(['Test_Chaitu','Test_jeevan'])
        cases = obj()
        self.execute(cases)

    def executor(self,fun):
        print(fun,type(fun))
        def __executor(*args,**kargs):
            print('in _ex')
            fun(*args,**kargs)
            print('function executed',args)
        return __executor


    def execute(self,cases):
        for class_ in cases:
            for test in cases[class_]:
                self.executor(test)
                



obj = Runner()