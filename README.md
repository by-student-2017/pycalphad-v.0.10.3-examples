# pycalphad-v.0.10.3-examples


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


## Example: Al-Cu-Y
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cu-Y
3. python3 ternary-AlCuY.py


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
- NIMS: CPDDB: https://cpddb.nims.go.jp/ (There are some files that cannot be read properly.)
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
