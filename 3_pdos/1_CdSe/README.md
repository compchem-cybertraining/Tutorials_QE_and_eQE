
1.  Run QE calculations 

    sbatch submit.slm

2.  Move the "x.pdos_atm# files to a separate folder

    mkdir pdos
    mv x.pdos_atm#* pdos

3. Edit the `compute_pdos.py` as needed

   * Make sure to correct the E_f parameter in the `compute_pdos.py` script. 
     You can take it from the x.scf.out

   * Define the projections and smearing options as needed

4. Make sure you have the needed environment:

    module load jupyter
    eval "$(/projects/academic/cyberwksp21/Software/Conda/Miniconda3/bin/conda shell.bash hook)"
    conda activate libra

5.  Run `compute_pdos.py` script

    python compute_pdos.py


   This script is exmplained in: https://github.com/compchem-cybertraining/Tutorials_Libra/tree/master/11_program_specific_methods/2_qe_methods/1_pdos/1_CdSe



