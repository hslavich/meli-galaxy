import matplotlib.pyplot as plt
import numpy as np

from model.Galaxy import Galaxy


class GalaxyPlot:
    def __init__(self, day=1):
        self.fig, self.ax = plt.subplots()
        self.galaxy = Galaxy()
        self.galaxy.advance(day - 1)
        self.draw_items()
        self.set_title('Meli galaxy - usar scroll para navegar')
        self.config()

    def draw_items(self):
        theta = np.linspace(0, 2 * np.pi, 100)
        [self.ax.plot(pl.distance * np.cos(theta), pl.distance * np.sin(theta), ':', color='#B4B4B4') for pl in self.galaxy.planets]
        self.planet_plots = [self.ax.add_artist(plt.Circle(planet.position, 100, color='b')) for planet in self.galaxy.planets]
        planet_positions = np.array(self.galaxy.planet_positions())
        self.area = plt.Polygon(planet_positions, color='#B4B4B4', alpha=0.5)
        plt.gca().add_patch(self.area)
        self.ax.add_artist(plt.Circle((0, 0), 200, color='#FFFF14'))
        self.status = self.ax.annotate(self.galaxy.status, xy=(0.86, 0.95), xycoords='axes fraction', bbox=dict(fc='w'))
        self.day = self.ax.annotate('Dia: ' + str(self.galaxy.current_day), xy=(0.025, 0.025), xycoords='axes fraction', bbox=dict(fc='w'))

    def config(self):
        self.ax.set_aspect(1)
        self.ax.set_facecolor('k')
        self.fig.canvas.mpl_connect('scroll_event', self.on_scroll)
        self.fig.tight_layout()

    def set_title(self, title):
        self.ax.set_title(title)

    def show(self):
        plt.ylim(-2000, 2000)
        plt.show()

    def on_scroll(self, event):
        if event.button == 'up':
            self.galaxy.advance(1)
        else:
            self.galaxy.advance(-1)
        self.update()

    def update(self):
        for i, planet in enumerate(self.galaxy.planets):
            self.planet_plots[i].center = planet.position
        self.status.set_text(self.galaxy.status)
        self.day.set_text('Dia: ' + str(self.galaxy.current_day))
        self.area.set_xy(self.galaxy.planet_positions())
        self.fig.canvas.draw()


if __name__ == '__main__':
    GalaxyPlot().show()
