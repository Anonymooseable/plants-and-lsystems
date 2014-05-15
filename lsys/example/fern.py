import lsys.core as core
import random


class FernSystem(core.System):
    def __init__(self, *args, **kwargs):
        branch = ["push", "muchsmaller", "turn", "fw", "branch", "pop"]
        super().__init__(rules={
            "root": (branch + ["flip", "fw", "smaller"] + branch +
                     ["flip", "fw", "smaller"]) * 3 + ["root"],
            "branch": (branch + ["flip", "fw", "smaller"] + branch +
                       ["flip", "fw", "smaller"]) * 3 + ["smaller","branch"],
            #cela correspond au règles
        }, actions={
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "turn": self.turn,
            "branch": self.branch,
            "smaller": self.smaller,
            "muchsmaller": self.muchsmaller,
            "flip": self.flip,
        }, axiom=["fw", "root"], **kwargs)
        self.length_stack = [10]
        self.flipped = False

    def fw(self):
        self.renderer.draw_segment(self.length_stack[-1])
        #correspond au dessin d'une section d'une branche
        
        self.renderer.turn((-1 if self.flipped else 1) * random.gauss(2, 2))
        #correspond au plie progressive de la fougère
        #(c'est une petite rotation du "stylo" progressive)

    def branch(self):
        self.renderer.draw_segment(self.length_stack[-1] * 4)
        #correspond au dessin du tige au bout d'une branche

    def smaller(self):
        self.length_stack[-1] *= 0.9
        #correspond au rapetissement progressive de la longueur de chaque
        #section d'une branche

    def muchsmaller(self):
        self.length_stack[-1] *= 0.4
        #correspond au définition la longueur de chaque nouvelle branche

    def turn(self):
        self.renderer.turn(80 if self.flipped else -80)
        #correspond au rotation du "stylo" qui dessine la fougère

    def push(self):
        self.renderer.push()
        #correspond à l'enregistrement de l'état du "stylo" (direction,
        #coordonnées) et le placement de cette information en haut de la pile 
        #qui stocke cette information ("renderer")
        
        self.length_stack.append(self.length_stack[-1])
        #correspond à l'enregistrement de la longueur de la ligne que dessine
        #le "stylo" et le placement de cette information en haut de la pile qui 
        #stocke cette information ("length_stack")

    def pop(self):
        self.renderer.pop()
        #correspond a l'appel au dernier état du "stylo", c'est-à-dire, prendre
        #les informations qui sont en haut de la pile "renderer"
        
        self.length_stack.pop()
        #correspond a l'appel au dernier la longueur de la ligne que dessine le
        #"stylo", c'est-à-dire, prendre les informations qui sont en haut de la
        #pile "length_stack"

    def flip(self):
        self.flipped = not self.flipped
        #correspond au basculement de gauche à droite et vice versa entre chaque
        #branche

def main():
    #mode = "opengl"
    mode = "turtle"

    if mode == "opengl":
        from lsys.render.gl_renderer import GLRenderer
        r = GLRenderer(
            scale=4,
            size=(800, 800),
            fg=(0.0, 0.4, 0.0, 1.0),
            bg=(1.0, 1.0, 1.0, 1.0)
        )
    elif mode == "turtle":
        from lsys.render.turtle_renderer import TurtleRenderer
        r = TurtleRenderer()
    s = FernSystem(renderer=r)
    s.construct(depth=4, debug=False)
    print(len(s.expanded), "instructions")
    s.render()

if __name__ == "__main__":
    main()
