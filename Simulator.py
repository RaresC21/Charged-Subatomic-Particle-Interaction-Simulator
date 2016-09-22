import matplotlib.pyplot as plt
import numpy as np

# Create 'size' of plot
sz = 10
minx = -sz
miny = -sz
maxx = sz
maxy = sz
plt.axis((minx,maxx,miny,maxy))
#plt.plot([-10,-10,10],[-10,10,10])
plt.ion()

class Obj (object) :  
    def __init__ (self, x,y, charge) :
        self.x = x
        self.y = y
        self.charge = charge
        
        self.mass = 1      
        
        self.ax = 0     #acceleration
        self.ay = 0
    
        self.vx = 0     #velocity
        self.vy = 0        
        
        self.xs = [x]
        self.ys = [y]

class Electric_Field (object) :
    
    def __init__ (self, objs) :
        self.objs = objs     # Array of objects to put in our field.
        self.l = 0.5         # how long each arrow should be

        self.objects_draw()
        self.field_draw()
        
    def objects_draw (self) :
        for o in self.objs :
            if o.charge > 0 :
                plt.plot(o.x, o.y, "ro")
            else :
                plt.plot(o.x, o.y, "go")

    
    def field_draw (self) :
        
        for x in range(minx, maxx+1) :
            for y in range(miny, maxy+1) :
                
                Ex, Ey, no_count = self.force_vec(x, y)
                
                if no_count == False :
                    h = 0.2
                    if (Ex == 0 and Ey == 0): 
                        h = 0.00001 # we don't want an arrow if there's no force
                    draw_arrow(x, y, Ex, Ey, h)   
                    
    def force_vec (self, x, y) :
        Ex=0.0
        Ey=0.0
        no_count = False
        for ob in self.objs :
            test = Obj(x,y, 0)
            d = distance(ob, test)
            if d <= 0.1 : 
                no_count = True                    
            else :
                e = E(ob, test)
                
                # components
                ex = e * (x - ob.x) / d
                ey = e * (y - ob.y) / d
                
                Ex = Ex + ex
                Ey = Ey + ey

        return (Ex, Ey, no_count)
             
def draw_arrow(x, y, dx, dy, h) :
    if np.abs(dx + dy) < 0.2 : 
        h = dx + dy + 0.00001
    plt.arrow( x - dx/2, y - dy/2, dx, dy, fc="k", ec="k", head_width=h/2, head_length=h)
    
def distance(ob1, ob2) :
    return np.power((ob1.x - ob2.x), 2) + np.power((ob1.y - ob2.y), 2)

def E (ob, test) :
    r = distance(ob, test)
    r = np.sqrt(r)
    
    return ob.charge / r

ef = Electric_Field(objects)
#plt.show()

def simulate (cur_objs, lmbda, iterations) :    
    
    Ex = []; Ey = []; Fx = []; Fy = [];
    for i in range(len(cur_objs)) :    
        ex, ey, s = ef.force_vec(cur_objs[i].x, cur_objs[i].y)
        Ex.append(ex)
        Ey.append(ey)
        Fx.append(0)
        Fy.append(0)

    
    k = 0
    while (k < iterations) :
    
        i = 0
        for obj in cur_objs :    

            cur_objs[i].xs.append(cur_objs[i].xs[-1] + 
                                    cur_objs[i].vx * lmbda + 
                                    0.5* cur_objs[i].ax *lmbda**2)
            cur_objs[i].ys.append(cur_objs[i].ys[-1] +
                                    cur_objs[i].vy * lmbda + 
                                    0.5* cur_objs[i].ay *lmbda**2)            
                        
            Ex[i], Ey[i], s = ef.force_vec(obj.x, obj.y) 
            Fx[i] = Ex[i] * obj.charge; Fy[i] = Ey[i] * obj.charge
            
            cur_objs[i].vx += cur_objs[i].ax * lmbda
            cur_objs[i].vy += cur_objs[i].ay * lmbda       
            
            cur_objs[i].ax = Fx[i] / obj.mass
            cur_objs[i].ay = Fy[i] / obj.mass
            
            i+=1
            
        for i in range(len(cur_objs)) :
            cur_objs[i].x = cur_objs[i].xs[-1]
            cur_objs[i].y = cur_objs[i].ys[-1]

        k += 1
    
    
    animate_it(cur_objs, iterations)

def animate_it(cur_objs, iterations) :
        
    xs = []; ys = []; colr = []
    for o in cur_objs :
        xs.append(o.xs[0])
        ys.append(o.ys[0])
        if o.charge > 0:
            colr.append('red')
        else :
            colr.append('green')
        
    plt.ion()    
    
    plt.scatter(xs, ys, color = colr)
    plt.show()
    
    for c in range(0, iterations, 20) :
        xs,ys=[],[]
        for o in cur_objs :
            xs.append(o.xs[c])
            ys.append(o.ys[c])
                
        plt.scatter(xs, ys, color=colr)
        plt.axis((minx,maxx,miny,maxy))
        #ef.objects_draw()
        #plt.plot(ef.objs[1].xs[c], ef.objs[1].ys[c], 'ro')
        #plt.plot(ef.objs[2].xs[c], ef.objs[2].ys[c], 'go')
    
        plt.draw()
        plt.pause(0.000000000001)
        plt.clf()

simulate(ef.objs, 0.01, 2000)

"""
plt.plot(ef.objs[0].xs, ef.objs[0].ys, color = 'red')
plt.plot(ef.objs[1].xs, ef.objs[1].ys, color = 'green')
plt.plot(ef.objs[2].xs, ef.objs[2].ys, color = 'blue')
"""
