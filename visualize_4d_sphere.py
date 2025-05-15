import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot_3d_sphere(ax, center, radius, color, alpha=0.6):
    u, v = np.mgrid[0:2*np.pi:30j, 0:np.pi:15j]
    x = center[0] + radius * np.cos(u) * np.sin(v)
    y = center[1] + radius * np.sin(u) * np.sin(v)
    z = center[2] + radius * np.cos(v)
    ax.plot_surface(x, y, z, color=color, alpha=alpha, linewidth=0)

# Parameters
r_4d = 1.0  # 4D sphere radius
num_frames = 60
num_kissing = 24

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
ax.set_box_aspect([1,1,1])
ax.set_xlim([-2.5,2.5])
ax.set_ylim([-2.5,2.5])
ax.set_zlim([-2.5,2.5])
ax.axis('off')

def update(frame):
    ax.cla()
    ax.set_xlim([-2.5,2.5])
    ax.set_ylim([-2.5,2.5])
    ax.set_zlim([-2.5,2.5])
    ax.axis('off')
    w = np.linspace(-r_4d, r_4d, num_frames)[frame]
    # Central sphere (remains at origin)
    r_3d = np.sqrt(max(0, r_4d**2 - w**2))
    if r_3d > 0:
        plot_3d_sphere(ax, [0,0,0], r_3d, 'purple', alpha=0.7)
    # "Quantum" kissing spheres: random centers each frame
    for _ in range(num_kissing):
        center = np.random.uniform(-2, 2, size=3)
        # Random radius as cross-section of 4D sphere at random w0
        w0 = np.random.uniform(-2, 2)
        d = w - w0
        if abs(d) <= r_4d:
            r_kiss = np.sqrt(max(0, r_4d**2 - d**2))
            plot_3d_sphere(ax, center, r_kiss, 'orange', alpha=0.5)
    ax.set_title(f"Quantum superposition: frame {frame+1}/{num_frames}")

ani = FuncAnimation(fig, update, frames=num_frames, interval=100)
plt.show()