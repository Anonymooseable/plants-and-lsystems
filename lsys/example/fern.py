#Ceci est le fichier qui contient le L-Systeme spécifique de la fougère.

import lsys.core as core
import random


class FernDrawer:
    def __init__(self, renderer, depth=7):
        # ceci sert seulement à l'écriture plus efficace de ce qui suit
        branch = ["push", "muchsmaller", "turn", "fw", "branch", "pop"]

        ## 1. Définition des règles du système

        # Règles qui définissent des branches.
        # Une branche ressemble grosso modo à cela:
        #   *
        #   |/
        #  \|
        #   |/
        #  \|
        #   |/
        #  \|
        #   |
        root_result = lambda context: (branch + ["flip", "fw", "smaller"]) * 3 + ["root"]
        branch_result = lambda context: (branch + ["flip", "fw", "smaller"]) * 3 + ["smaller", "branch"]

        # Créer un L-système
        # rules = règles du L-Système: seulement les symboles
        #         "root" et "branch" sont des variables, le reste sont des
        #         constantes. Pour comprendre les règles, on conseille de
        #         comprendre les fonctions auxquelles sont associés les symboles.
        # axiom = axiome du système: symboles initiaux qui engendreront
        #         tout le système
        self.system = core.System(rules={
            "root": root_result,
            "branch": branch_result
        }, axiom=["fw", "root"])

        #Dictionnaire qui associe chaque symbole à une fonction
        #qui contribuera au dessin
        self.actions = {
            "fw": self.fw,
            "push": self.push,
            "pop": self.pop,
            "turn": self.turn,
            "branch": self.branch,
            "smaller": self.smaller,
            "muchsmaller": self.muchsmaller,
            "flip": self.flip,
        }

        self.renderer = renderer
        self.depth = depth

        # pile qui contiendra l'information de la longueur de la
        # la ligne que dessinera le "stylo"
        # 10 est la valeur initiale
        self.length_stack = [10]

        #correspond au basculement de gauche à droite et vice versa entre chaque
        #branche.
        self.flipped = False

    def fw(self):
        """Dessiner un segment d'une branche.

        Se comporte d'une façon qui ressemble au fw() du turtle, mais tourne
        un petit peu de manière aléatoire (l'angle de rotation suit une
        distribution normale d'espérance 2 et d'écart type 2.
        Ceci correspond à une rotation qui aura la tendance d'être vers le haut
        (dans la direction de la branche "mère") mais pourra aller dans
        l'autre sens (angle négatif)."""
        self.renderer.draw_segment(self.length_stack[-1])
        self.renderer.turn((-1 if self.flipped else 1) * random.gauss(2, 2))

    def branch(self):
        """Dessine un segment au bout d'une branche.
        """
        self.renderer.draw_segment(self.length_stack[-1] * 4)

    def smaller(self):
        """Diminue la taille des segments qui suivent."""
        self.length_stack[-1] *= 0.9
        #correspond au rapetissement progressive de la longueur de chaque
        #section d'une branche

    def muchsmaller(self):
        """Diminue fortement la taille des segments qui suivent.

        Utilisé lors d'une ramification, pour faire en sorte que la branche
        soit plus petite que sa "mère"."""
        self.length_stack[-1] *= 0.4

    def turn(self):
        """Rotation. Comme left(80) ou right(80) du turtle, selon l'état."""
        self.renderer.turn(80 if self.flipped else -80)

    def push(self):
        """Enregistre l'état actuel pour le placer sur la pile."""
        self.renderer.push()

        # Pile longueur des segments
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

    def draw(self):
        actions = self.system.construct(depth=self.depth)
        for action in actions:
            self.actions.get(action, lambda: None)()
        self.renderer.display()
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
    s = FernDrawer(depth=4, renderer=r)
    s.draw()

if __name__ == "__main__":
    main()
