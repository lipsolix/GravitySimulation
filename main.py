from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class Dot:
    def __init__(self, mass=10, pos=[0, 0, 0], acc=[0, 0, 0]):
        self.position = pos
        self.mass = mass
        self.acceleration = acc

    def getPosition(self):
        return self.position

    def getAcc(self):
        return self.acceleration

    def setAcc(self, acc=[0, 0, 0]):
        self.acceleration = acc

    def getMass(self):
        return self.mass

    def makeMove(self):
        for _i in range(3):
            self.position[_i] += self.acceleration[_i]/2


dot1 = Dot(pos=[0, 0, 0], acc=[3, 3, 3], mass=100)
dot2 = Dot(pos=[0, 0, 10], acc=[-3, -3, -3], mass=100)
dot3 = Dot(pos=[10, 0, 10], acc=[-3, 0, 0], mass=100)
dot4 = Dot(pos=[10, 0, -10], acc=[3, 0, 0], mass=100)


def calcGravity(a=dot1, b=dot2):
    _G = 0.0001
    _k = 0.0001
    x1, y1, z1 = a.getPosition()
    x2, y2, z2 = b.getPosition()

    _R = (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 + 10E-20

    m1 = a.getMass()
    m2 = b.getMass()

    _F = _G*m1*m2/_R

    vector = [x2 - x1, y2 - y1, z2 - z1]
    acc1 = a.getAcc()
    acc2 = b.getAcc()
    for _i in range(3):
        acc1[_i] += _k*vector[_i]*m2
        acc2[_i] -= _k*vector[_i]*m1

    a.setAcc(acc1)
    b.setAcc(acc2)



fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(30, 30)

plt.ion()



for i in range(1000):
    #ax.clear()

    x, y, z = dot1.getPosition()
    ax.scatter(x, y, z, color="red")

    x, y, z = dot2.getPosition()
    ax.scatter(x, y, z, color="green")

    x, y, z = dot3.getPosition()
    ax.scatter(x, y, z, color="blue")

    x, y, z = dot4.getPosition()
    ax.scatter(x, y, z, color="yellow")


    ax.scatter(0, 0, 0, color="black")


    def lim():
        minmax = (-25, 25)
        ax.set_xlim(minmax)
        ax.set_ylim(minmax)
        ax.set_zlim(minmax)

    lim()

    calcGravity(dot1, dot2)
    calcGravity(dot1, dot3)
    calcGravity(dot1, dot4)

    calcGravity(dot2, dot3)
    calcGravity(dot2, dot4)

    calcGravity(dot3, dot4)


    dot1.makeMove()
    dot2.makeMove()
    dot3.makeMove()
    dot4.makeMove()


    plt.show()
    plt.pause(0.0001)





