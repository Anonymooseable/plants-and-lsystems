import lsys.example.fern as fern
import lsys.example.tree as tree
import imp

while True:
    choice = input("Which example? [t]ree or [f]ern?")
    if choice == "t":
        imp.reload(tree)
        tree.main()
    elif choice == "f":
        imp.reload(fern)
        fern.main()
