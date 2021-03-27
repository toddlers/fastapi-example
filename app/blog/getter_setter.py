#!/usr/bin/env python

class Name:
    """ Name Class """
    def __init__(self, fname, mname, lname):
        self.first_name = fname
        self.middle_name = mname
        self.last_name = lname
    
    @property
    def first_name(self):
        return self._first_name
    

    @first_name.setter
    def first_name(self, fname):
        if fname:
            self._first_name = fname
        else:
            ValueError('First name can not be none')

    @property
    def middle_name(self):
        return self._middle_name
    

    @middle_name.setter
    def middle_name(self, mname):
        self._middle_name = mname

    @property
    def last_name(self):
        return self._last_name
    

    @last_name.setter
    def middle_name(self, lname):
        self._last_name = lname