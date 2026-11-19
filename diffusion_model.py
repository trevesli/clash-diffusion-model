import numpy as np
import matplotlib.pyplot as plt


def plot_profile(grid, elevation, colour="r", title="None", output="None"):
    plt.figure()  # set up a figure window
    plt.plot(grid, elevation, colour)
    plt.xlabel("x")
    plt.ylabel("z")
    if title is not None:
        plt.title(title)
    if output is not None:
        plt.savefig(output)


def calculate_stable_time_step(grid_spacing, diffusivity):
    return 0.5 * grid_spacing**2 / diffusivity


if __name__ == "__main__":

    D = 100  # diffusivity
    Lx = 300  # model domain

    dx = 0.5  # grid spacing
    x = np.arange(start=0, stop=Lx, step=dx)
    nx = len(x)  # number of grid nodes

    z = np.zeros_like(x)
    z_left = 500
    z_right = 0
    z[x <= Lx / 2] = z_left
    z[x > Lx / 2] = z_right

    plot_profile(x, z, title="Initial hillslope profile", output="initial-profile.png")

    nt = 5000  # number of time steps
    dt = calculate_stable_time_step(dx, D)

    for t in range(0, nt):
        z[1:-1] += D * dt / dx**2 * (z[:-2] - 2 * z[1:-1] + z[2:])

    plot_profile(
        x, z, colour="b", title="Final hillslope profile", output="final-profile.png"
    )
