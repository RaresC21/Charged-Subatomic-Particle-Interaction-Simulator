import electricField as efield

def draw(plt, field) :
    minx, maxx, miny, maxy = plt.axis()
    objects_draw(plt, field)
    field_draw(plt, field, minx, maxx, miny, maxy)

def objects_draw (plt, field) :
    for p in field.particle :
        if p.charge > 0 :
            plt.plot(p.x, p.y, "ro")
        else :
            plt.plot(p.x, p.y, "go")
        
        
def field_draw (plt, field, minx, maxx, miny, maxy) :
    for x in range((int)(minx), (int)(maxx)+1) :
        for y in range((int)(miny), (int)(maxy)+1) :
            
            Ex, Ey, too_close = field.force_vec(x, y)
        
            if too_close :
                continue
            
            # we don't want an arrow if there's no force
            if Ex != 0 or Ey != 0 :
     	        draw_arrow(plt, x, y, Ex, Ey, 0.2)
                
def draw_arrow(plt, x, y, dx, dy, h) :
    if abs(dx + dy) < 0.2 : 
        h = dx + dy + 0.00001
    plt.arrow( x - dx/2, y - dy/2, dx, dy, fc="k", ec="k", head_width=h/2, head_length=h)
