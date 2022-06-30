# Tutorial: NACs for Adamantane

## 1. Inputs

  * ada_0.in - the main input file

  * `*.UPF` - the pseudopotential files

  * submit.slm - the SLURM submit file

## 2. How to run

     sbatch submit.slm


## 3. Important 

### 3.1. 

To turn on the NAC calculations add in the `&control` section the following keyword

    nonadiabatic = .true.


### 3.2.

To define the active space of orbitals for which the time-overlaps will be computed
add in the `&system` section the following keywords

    fde_nba_beg = 28 !homo=28
    fde_nba_end = 29 !lumo=29

### 3.3.

Make sure that for each fragment you define the following parameters such that the 
indicated fractions of the total cell size are sufficient to enclose the corresponding fragments.

    fde_cell_split(1) = 1.0
    fde_cell_split(2) = 1.0
    fde_cell_split(3) = 1.0


### 3.4.

The time-overlaps are computed only for the first fragment (with index 0, that is the input file that
ends with "_0.in" )


## 4. Outputs

The key results are stored in the "NAD" directory as following:

  * E_t_f_k_re - energies of orbitals in a.u.

  * occupations_t_f_k_re - occupation numbers for these orbitals

  * S_t_f_k_re  - real component of the raw time-overlaps

  * S_t_f_k_im  - imaginary component of the raw time-overlaps

  * S_t_f_k_tre - phase-corrected time-overlaps, real component


   Here, the numbers  `t`, `f`, and `k` are the indices indicating  
   time, fragment index (starting from 0), k-point index (starting from 1), respectively


