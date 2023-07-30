import os

from Core.Game import DMGame
################################################################################

src_path = "./src"
current_pypath = os.environ.get("PYTHONPATH", "")
updated_pypath = f"{src_path}:{current_pypath}"
os.environ["PYTHONPATH"] = updated_pypath

################################################################################
def main() -> None:

    game = DMGame()
    game.run()

################################################################################
if __name__ == '__main__':
    main()
