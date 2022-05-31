from os import system as sy
sy('cls')

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class Favgirl:
    def __init__(self):
        self.headval = None

    def pg(self):
        printg = self.headval
        while printg is not None:
            print(printg.dataval, end='->')
            printg = printg.nextval

    def addgirl(self, girlname):
        girlname = Node(girlname)
        girlname.nextval = self.headval
        self.headval = girlname

    def insertf(self, newdata):
        newdataa = Node(newdata)
        newdataa.nextval = self.headval
        self.headval = newdataa

    def deletenode(self, girlname):
        a = self.headval
        if (a is not None):
            if (a.dataval == girlname):
                self.headval = a.nextval
                a = None
                return
                
gb = Favgirl()
gb.headval = Node('Asri')
g2 = Node('Lastri')
g3 = Node('Lisa')
g4 = Node('Livy')
g5 = Node('Mikasa')

gb.headval.nextval = g2
g2.nextval = g3
g3.nextval = g4
g4.nextval = g5
print('- Menambahkan node')
gb.pg()
print('\n- Insert Node')
gb.insertf('Rahel')
gb.pg() 
print('\n- Menghapus Node')
gb.deletenode('Rahel')
gb.pg() 
