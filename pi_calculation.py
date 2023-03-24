from mpi4py import MPI
import random
import sys

def calculate_pi(num_points):
    count_inside_circle = 0
    for _ in range(num_points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x * x + y * y
        if distance <= 1:
            count_inside_circle += 1
    return count_inside_circle

if __name__ == "__main__":
    num_points = int(sys.argv[1])
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    local_count = calculate_pi(num_points // size)

    global_count = comm.reduce(local_count, op=MPI.SUM, root=0)

    if rank == 0:
        pi = 4 * global_count / num_points
        print("Calculated value of Pi:", pi)

