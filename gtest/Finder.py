from importlib import import_module
from collections import defaultdict as dft
from inspect import isfunction,isclass,ismethod
from pdb import set_trace
from traceback import print_exc
#TODO - WoRk
'''
-> Need to define @Test,@aftertest,@beforetest ... functions
-> Need to execute function which are having @
-> inherite unittest class and impliment some methods
-> write cli commond for execution 
-> Prepare our reports and logs.
'''

class Test_Finder:
    def __init__(self,test_class):
        self.classes = test_class
        self.store_funs = dft(list)

    def __call__(self):
        try:
            for _class_ins in self.classes:
                __class_ins = import_module(_class_ins)
                self.test_classes = self._get_class_obj(__class_ins)
                self.test_funs = self._get_unittests(self.test_classes)
            return self.store_funs
        except Exception as e:
            print(e)
            print_exc(chain=True)

    def _get_class_obj(self,obj):
        #Function returns class objects
        test_functions = []
        for _obj in dir(obj):
            class_obj = getattr(obj,_obj)
            if (isclass(class_obj)):
                test_functions.append(class_obj)
        return test_functions

    def _get_unittests(self,obj):
        #Function return unittest functions
        for class_obj in obj:
            instance = class_obj()
            for _obj in dir(instance):
                if '__' in _obj:
                    continue
                _fun = getattr(instance,_obj)
                if ismethod(_fun):
                    self.store_funs[class_obj].append(_fun)


# print(__name__)
if __name__ == '__main__':
    obj = Test_Finder(['Test_Chaitu'])
    obj()