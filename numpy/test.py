class Greater(object):
    def __init__(self, name):
        self.name = name
    
    def greater(self, loud = False):
        if loud:
            print('Hello, %s' % self.name.upper())
        else:
            print('Hello, %s' % self.name)
            
if __name__ == "__main__":
    g = Greater('Fred')
    g.greater()
    g.greater(True)
    