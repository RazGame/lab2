from Canvas import Canvas
from vispy import app
from surfaces import CircularWaves


if __name__ == '__main__':
    c = Canvas(CircularWaves.CircularWavesSurface(max_height=0.05), size=(700, 700))
    print("Press:")
    print("Space - for show lattice vertices")
    print("1 - for show sun diffused light")
    print("2 - for show refracted image of seabed")
    print("3 - for show ambient light in water")
    print("4 - for show reflected image of sky")
    print("5 - for show reflected image of sun:")
    print("b - for change shape of bed")
    print("r - randomize surface")
    print("p - for pause")
    app.run()
