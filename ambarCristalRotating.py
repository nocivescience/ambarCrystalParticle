from manim import *
import itertools as it
class Ambar(Scene):
    conf={
        'n_part':50,
        'colors':[YELLOW,BLUE,TEAL,GREEN,RED],
        'radio':0.2,
        'side_length':3
    }
    def construct(self):
        square=Square(side_length=self.conf['side_length'])
        self.play(Create(square))
        dots=self.get_dots(square)
        DOTS=self.get_anim(dots)
        self.add(DOTS)
        self.wait(10)
    def get_dots(self,square):
        positions=np.array([
            [-square.side_length/2*np.random.uniform(-.8,.8),square.side_length/2*np.random.uniform(-.8,.8),0]
            for _ in range(self.conf['n_part'])
        ])
        signatures=np.random.choice(['+','-'],size=len(positions))
        dots=VGroup()
        myColors=it.cycle(self.conf['colors'])
        for pos,sign in zip(positions,signatures):
            dot=Dot(radius=self.conf['radio']).move_to(pos).set_color(next(myColors))

            if sign=='-':
                texto=Tex(sign).move_to(dot.get_center()).set_width(dot.get_width()-0.05).set_color(BLACK)
            else:
                texto=Tex(sign).move_to(dot.get_center()).match_width(dot).set_color(BLACK)
            dot.add(texto)
            dots.add(dot)
        return dots
    def get_anim(self,dots):
        DOTS=VGroup()
        for dot in dots:
            dot.add_updater(self.update_particle)
            DOTS.add(dot)
        return DOTS
    def update_particle(self,particle,dt):
        posicion=rotate_vector(0.08*RIGHT,2*np.pi*np.random.random())+particle.get_center()+0.001*RIGHT
        if posicion[0]>self.conf['side_length']/2-self.conf['radio']:
            posicion[0]=-1
        if posicion[0]<-self.conf['side_length']/2+self.conf['radio']:
            posicion[0]=1
        if posicion[1]>self.conf['side_length']/2-self.conf['radio']:
            posicion[1]=-1
        if posicion[1]<-self.conf['side_length']/2+self.conf['radio']:
            posicion[1]=1
        particle.move_to(posicion)
        particle.rotate(TAU*.02*np.random.random())