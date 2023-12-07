# pycalphad-v.0.10.3-examples
- Note 1: If part of the figure is missing, please use "Configure subplots".
- Note 2: Try rewriting the "XXX" part of "v.T: XXX," and changing the temperature and plotting. For example, in ternary-AlCuY.py, try changing "v.T: 830," to "v.T: 1273,".


## Installation (ubuntu 22.04 LTS or WSL2 (win))
1. pip3 install -U pip setuptools
2. pip3 install -U pycalphad==0.10.3


## Examples
1. git clone https://github.com/pycalphad/pycalphad.git
2. cd pycalphad
3. cd examples


## Examples (this page)
1. git clone https://github.com/by-student-2017/pycalphad-v.0.10.3-examples.git
2. cd pycalphad-v.0.10.3-examples


## Example: Al-Mg (Binary phase diagram)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Mg
3. python3 binary-AlMg.py
- https://github.com/pycalphad/pycalphad/blob/develop/examples/BinaryExamples.ipynb


## Example: Nb-Re (Gibbs energy surface)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Nb-Re
3. python3 binary-NbRe-gibbs_free_energy.py
- https://github.com/pycalphad/pycalphad/blob/develop/examples/BinaryExamples.ipynb


## Example: Al-Cu-Y (Phase diagram and Mixing enthalpy )
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cu-Y
3. python3 ternary-AlCuY.py
4. python3 Ref_ternary-AlCuY-enthalpy.png
- https://github.com/pycalphad/pycalphad/blob/develop/examples/TernaryExamples.ipynb


## Example: Cr-Fe-Mo
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Cr-Fe-Mo
3. python3 ternary-CrFeMo.py


## Example: Cr-Fe-Ni
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Cr-Fe-Ni
3. python3 ternary-CrFeNi.py


## Example: Al-Cr-Ni
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cr-Ni
3. (You can get alcrni_dup.tdb from CPDDB (Multicomponent Systems))
4. python3 ternary-AlCrNi.py


## TDB files
- NIMS: CPDDB: https://cpddb.nims.go.jp/ (There are some files that cannot be read properly. It takes some time to register, but it is free to use.)
- TDBDB: https://avdwgroup.engin.brown.edu/ 
- Available open databases: https://www.opencalphad.com/databases.html
-   https://github.com/pycalphad/pycalphad/tree/develop/examples


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
+ Please, see "Installation_note_WSL2.txt"
