#!/bin/bash
#SBATCH --job-name=square_job_array
#SBATCH --output=output_%A_%a.out
#SBATCH --error=error_%A_%a.err
#SBATCH --array=1-10
#SBATCH --time=00:01:00
#SBATCH --mem-per-cpu=100M

module load python

python square.py ${SLURM_ARRAY_TASK_ID}

