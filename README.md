# pycalphad-v.0.10.3-examples
- Note: If part of the figure is missing, please use "Configure subplots".


## Installation (ubuntu 22.04 LTS or WSL2 (win))
0. sudo apt update
1. sudo apt -y install python3-pip
2. pip3 install -U pip setuptools
3. pip3 install -U pycalphad==0.10.3


## Examples (official)
1. git clone https://github.com/pycalphad/pycalphad.git
2. cd pycalphad
3. cd examples


## Examples (python3)
1. git clone https://github.com/by-student-2017/pycalphad-v.0.10.3-examples.git
2. cd pycalphad-v.0.10.3-examples


## Example: Al-Mg (Binary phase diagram)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Mg
3. python3 binary-AlMg.py
- https://github.com/pycalphad/pycalphad/blob/develop/examples/BinaryExamples.ipynb


## Example: Nb-Re (Gibbs energy surface [J/mol])
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Nb-Re
3. python3 binary-NbRe-gibbs_free_energy.py
- https://github.com/pycalphad/pycalphad/blob/develop/examples/BinaryExamples.ipynb


## Example: Al-Cu-Y (Phase diagram and Mixing enthalpy [J/mol])
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cu-Y
3. python3 ternary-AlCuY.py
4. python3 ternary-AlCuY-enthalpy.py
- https://github.com/pycalphad/pycalphad/blob/develop/examples/TernaryExamples.ipynb


## Example: Cr-Fe-Mo (easier user input)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Cr-Fe-Mo
3. python3 ternary-CrFeMo.py
- It would be good to compare the results with OpenCALPHAD.


## Example: Cr-Fe-Ni (easier user input)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Cr-Fe-Ni
3. python3 ternary-CrFeNi.py
- It would be good to compare the results with OpenCALPHAD.


## Example: Mo-Ni-Re (easier user input)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Mo-Ni-Re
3. (You can get mmc1.TDB from TDBDB (https://avdwgroup.engin.brown.edu/)
4. python3 ternary-MoNiRe.py
- An example of changing the order of element descriptions.


## Example: B-Fe-Nd (easier user input + output png)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd B-Fe-Nd
3. (You can get alcrni_dup.tdb from CPDDB (Multicomponent Systems))
4. python3 ternary-BFeNd.py
- An example of changing the order of element descriptions.


## Example: Al-Cr-Ni (easier user input + output png (not show graph))
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cr-Ni
3. (You can get alcrni_dup.tdb from CPDDB (Multicomponent Systems))
4. python3 ternary-AlCrNi.py
- An example of changing the order of element descriptions.


## TDB files
- NIMS: CPDDB: https://cpddb.nims.go.jp/ (There are some files that cannot be read properly. It takes some time to register, but it is free to use.)
- TDBDB: https://avdwgroup.engin.brown.edu/ 
- Available open databases: https://www.opencalphad.com/databases.html
-   https://github.com/pycalphad/pycalphad/tree/develop/examples


## Usage (TDBDB: https://avdwgroup.engin.brown.edu/)
1. Elements : Mo Ni Re
2. (click) Search
3. Use interactive 3D: [(check)]
4. (click) Preview(experimental!)
5. (Compare graphe and pycalphad results)


## Learn more
- Workshop 2021: https://www.youtube.com/watch?v=RuqtvRHQML4
- Workshop 2020/12/08: https://www.youtube.com/watch?v=S-iOcrQlsnU
- Workshop 2020/11/11: https://www.youtube.com/watch?v=FeITSRUhHQs
- Workshop 2020/08/24: https://www.youtube.com/watch?v=cDGX5XOeWJQ&t
- SciPy 2015/07/16: https://www.youtube.com/watch?v=30oiHIPjSJI, https://www.youtube.com/watch?v=iT1qeGg6Qbs&t
- ESPEI: https://www.youtube.com/watch?v=4mSRpLFtMps
- ESPEI: https://www.youtube.com/watch?v=T8oAnV8gZmQ
- Examples: https://pycalphad.org/docs/latest/examples/index.html
- FAQ: https://github.com/pycalphad/pycalphad/blob/1563bc4cc7754d2925a73d6e4aa76bb22abbb7d4/docs/faq.rst#L50
- Package: https://pycalphad.org/docs/latest/api/pycalphad.html
- Phases research lab: https://phaseslab.com/pycalphad/
- ResearchGate: https://www.researchgate.net/publication/311959120_pycalphad_CALPHAD-based_Computational_Thermodynamics_in_Python


Acknowledgment
=======
- This project (modified version) is/was partially supported by the following :
- meguREnergy Co., Ltd.
- ATSUMITEC Co., Ltd.
- RIKEN
- Without the support of "meguREnergy Co., Ltd." and "ATSUMITEC Co., Ltd.", I would not have been able to develop the examples to the level shown on this github. I would like to express my sincere gratitude. 


PC specs used for test
=======
+ OS: Microsoft Windows 11 Home 64 bit
+ BIOS: 1.14.0
+ CPU： 12th Gen Intel(R) Core(TM) i7-12700
+ Base Board：0R6PCT (A01)
+ Memory：32 GB
+ GPU: NVIDIA GeForce RTX3070
+ WSL2: VERSION="22.04.1 LTS (Jammy Jellyfish)"
+ Python 3.10.12
