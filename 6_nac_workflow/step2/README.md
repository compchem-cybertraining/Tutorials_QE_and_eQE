
 1. Copy files

     cp -r ../step1/PP .
     cp ../step1/x0.scf.in .
     cp ../step1/x0.exp.in .
     cp ../step1/x0.md.out .

2. Edit files:

     Edit file `x0.scf.in`

   a)    `md`  -> `scf`

   b) Remove the ATOMIC_POSITIONS section
 
   c) Ensure the k-points are listed as 1 1 1 0 0 0


  
     Edit files `x0.scf.in` and `x0.exp.in` to provide the ABSOLUTE path 
     to the pseudopotential dirs


3.  Open and run the DO_NACS notebook


4.  Open and run the ANALYZE_NACS notebook


5.  Open and run the DO_SPECTRUM notebook 



NOTE: there may be problems with running QE in the terminal, if you have Jupyter notebook running.

 
