import numpy as np
import matplotlib.pyplot as plt

# simple DLA simulation
def simple_DLA(grid_size, particle_count, walk_length, stickiness, extra_growth):
    # Create a grid to represent the environment
    grid = np.zeros((grid_size, grid_size), dtype=int)

    #create 10 starting points along a line going horizontally in the grid in the middle
    for i in range(5):
        grid[grid_size//2, i*(grid_size//5)+grid_size//10] = 1

    # Define possible movement directions
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for i in range(extra_growth):
        directions.append((-1, 0))

    # Simulation loop
    for _ in range(particle_count):
        x, y = np.random.randint(0, grid_size), np.random.randint(0, grid_size)

        for _ in range(walk_length):
            dx, dy = random_direction = directions[np.random.randint(0, 4+extra_growth)]
            x2, y2 = x + dx, y + dy

            if 0 <= x2 < grid_size and 0 <= y2 < grid_size:
                if grid[x2, y2] == 1:
                    # Attach the particle
                    grid[x, y] = 1
                    # Sometimes we branch out a new particle
                    if np.random.rand() < 0.4:
                        grid[x2, y2] = 1
                    break
                elif np.random.rand() < stickiness:
                    # Particle sticks, but doesn't become part of the cluster
                    break
                else:
                    x, y = x2, y2

    # Display the result
    plt.imshow(grid, cmap='gray', origin='lower')
    # draw a line to represent a ground (in the middle of the grid)
    plt.plot([0, grid_size-1], [grid_size//2, grid_size//2], color='white')
    plt.show()

#define a particle which can either be sticky or not
class Particle:
    def __init__(self, x, y, is_sticky):
        self.x = x
        self.y = y
        self.is_sticky = is_sticky
        self.x2 = 0
        self.y2 = 0

    def move(self, grid_size, grid):
        # Define possible movement directions
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dx, dy = directions[np.random.randint(0, 4)]
        self.x2, self.y2 = self.x + dx, self.y + dy
        if 0 <= self.x2 < grid_size and 0 <= self.y2 < grid_size:
            if grid[self.x2, self.y2] == 1: 
                self.attach(grid)
                self.stick()
            else: 
                self.x, self.y = self.x2, self.y2
            

    def attach(self, grid):
        # Attach the particle
        grid[self.x, self.y] = 1

    def stick(self):
        # Particle sticks, but doesn't become part of the cluster
        self.is_sticky = True

def falling_DLA(grid_size, particles_count):
    # Create the grid
    grid = np.zeros((grid_size, grid_size), dtype=int)
    
    # Define the possible directions of a falling particle

    # Create a line of class particles which are sticky in between the bottom and middle of the grid
    particles = [Particle(0, i, True) for i in range(grid_size)]
    for particle in particles:
        particle.attach(grid)
    
    # Simulation loop
    for _ in range(particles_count):
        print("im running the loop")
        # Create a new particle at the top of the falling down
        particle = Particle(np.random.randint(0, grid_size), grid_size-50 , False)
        # Let it fall until it sticks to another particle
        while not particle.is_sticky:
            particle.move(grid_size, grid)
            if particle.y2 < 0 or particle.x2 < 0 or particle.x2 >= grid_size or particle.y2 >= grid_size:
                break
    # Display the result
    plt.imshow(grid, cmap='gray', origin='lower')
    plt.show()
    # draw a line to represent a ground (in the middle of the grid)


# Main loop
if __name__ == '__main__':
    # Parameters
    grid_size = 100
    particle_count = 1000

    # Run the simulation
    falling_DLA(grid_size, particle_count)