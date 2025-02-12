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
- CoCrFeNiV.TDB-R3.txt: A thermodynamic description of the Co-Cr-Fe-Ni-V system for high-entropy alloy (HEA) design


## Example: Mo-Ni-Re (easier user input)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Mo-Ni-Re
3. (You can get mmc1.TDB from TDBDB (https://avdwgroup.engin.brown.edu/)
4. mv mmc1.TDB Cri_2015.TDB
5. python3 ternary-MoNiRe.py
- An example of changing the order of element descriptions.


## Example: B-Fe-Nd (easier user input + output png)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd B-Fe-Nd
3. (You can get bfend_hal.tdb from CPDDB (Multicomponent Systems))
4. python3 ternary-BFeNd.py
- An example of changing the order of element descriptions.


## Example: Al-Cr-Ni (easier user input + output png (not show graph))
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Al-Cr-Ni
3. (You can get alcrni_dup.tdb from CPDDB (Multicomponent Systems))
4. python3 ternary-AlCrNi.py
- An example of changing the order of element descriptions.


## Example: V-Li (V=Vacancy) (LiCoO2-CoO2 Pseudo-binary phase diagram)
1. cd ~/pycalphad-v.0.10.3-examples
2. cd LiCoO2-CoO2
3. python3 binary-LiCoO.py


## Example: Cs-Li-fix-Cl_test
1. cd ~/pycalphad-v.0.10.3-examples
2. cd Cs-Li-fix-Cl_test
3. python3 phase-diagram.py
- see Gitter: https://app.gitter.im/#/room/#pycalphad_pycalphad:gitter.im


## TDB files
- NIMS: CPDDB: https://cpddb.nims.go.jp/ (There are some files that cannot be read properly. It takes some time to register, but it is free to use.)
- TDBDB: https://avdwgroup.engin.brown.edu/ , https://www.sciencedirect.com/science/article/pii/S0364591618300099 (Open Access)
- MatCalc, Open free databases: https://www.matcalc-engineering.com/index.php/databases , https://doi.org/10.1016/j.calphad.2023.102531 (Open Access)
- MatCalc6: https://www.matcalc.at/index.php/databases/open-databases
- Available open databases: https://www.opencalphad.com/databases.html
-   https://github.com/pycalphad/pycalphad/tree/develop/examples
- NIST (Solder Systems): https://www.metallurgy.nist.gov/phase/solder/solder.html
-   https://www.nist.gov/mml/materials-science-and-engineering-division/thermodynamics-and-kinetics-group/published-diffusion
-   Computational File Repository (TDB, Mobility Database): https://materialsdata.nist.gov/handle/11256/2
- JAEA: https://migrationdb.jaea.go.jp/cgi-bin/db_menu.cgi?ej=1&title=TDB
- Computational Thermodynamics, Free databases: http://www.met.kth.se/~bosse/BOOK/databases/databases.html
- nanocem CemGEMS: https://cemgems.org/cemdata/about-cemdata/
- GEMS: https://gems.web.psi.ch/TDB/?forprint
- MINES: https://geoinfo.nmt.edu/mines-tdb/
- Thermo-Chimie: https://www.thermochimie-tdb.com/
- SGTE Pure: https://www.sgte.net/en/free-pure-substance-database
- ATAT: https://www.brown.edu/Departments/Engineering/Labs/avdw/atat/
- TDB-6: https://www.oecd-nea.org/jcms/pl_22166/thermochemical-database-tdb-project


## Widom Alloy Database
- https://alloy.phys.cmu.edu/


## CAMP databases (CAMP Homepage)
- https://databases.fysik.dtu.dk/


## 2NN MEAM Interatomc Potential
- https://cmse.postech.ac.kr/home_2nnmeam


## Usage (TDBDB: https://avdwgroup.engin.brown.edu/)
1. Elements : Mo Ni Re
2. (click) Search
3. Use interactive 3D: [(check)]
4. (click) Preview(experimental!)
5. (Compare graphe and pycalphad results)
- Paper: https://www.sciencedirect.com/science/article/pii/S0364591618300099 (Open Access)


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
- Issues: https://github.com/pycalphad/pycalphad/issues
- Gitter: https://app.gitter.im/#/room/#pycalphad_pycalphad:gitter.im
- Package: https://pycalphad.org/docs/latest/api/pycalphad.html
- Phases research lab: https://phaseslab.com/pycalphad/
- ResearchGate: https://www.researchgate.net/publication/311959120_pycalphad_CALPHAD-based_Computational_Thermodynamics_in_Python


## Note
- Al-Mg-Zn (Qiu et al. (2015)) from TDBDB (https://avdwgroup.engin.brown.edu/)
```
mv mmc1.TDB Qiu_2015.TDB
sudo apt -y install nkf
nkf -w Qiu_2015.TDB > Qiu_2015_en.TDB
python3 ternary-AlMgZn.py
# need "nkf" for "UnicodeDecodeError: 'utf-8' codec can't decode byte 0xfc in position 193546: invalid start byte"
```
- Al-Mg-Zn (almgzn_hay.tdb from CPDDB at 15:00 Dec/08/2023): read error
```
Line 170: "3000 Unary5.0 N !" => "3000 N  Unary5 !"
Line 205: Remove "6000 N 2019Hay", i.d., => "CONSTITUENT ALMG_G  :MG : AL,MG,ZN : AL,MG,ZN : !"
```
- Fe-Nb-Ni_test folder (Enriched_dataseTDB_V2.txt)
```
Line 79: => "$ FUNCTION GNIBCC  298.15 +8715.084-3.556*T+GHSERNI#; 6000 N !"
Line 175: => "+GHSERCO#; 1768 Y"
Line 985: => "+2*GHSERWW#+4*GHSERFE#;   6.00000E+03   N REF:12 !"
Line 1183: => "+12*GHSERCR#;   6000   N REF:211 !"
```
- Fe-Nb-Ni_test folder (CORRECTdatabase.txt)
```
Line 96: => "$ FUNCTION GCOBCC 298.14 +2938-.7138*T+GHSERCO#; 6000 N !"
Line 100: => "$ FUNCTION GNIBCC  298.15 +8715.084-3.556*T+GHSERNI#; 6000 N !"
Line 1061: => "+2*GHSERWW#+4*GHSERFE#;   6.00000E+03   N REF:12 !"
Line 1310: => "+12*GHSERCR#;   6000   N REF:211 !"
Line 1358-1373: Write "$" at the beginning of the line.
```
- conds: 0 => 1e-4 for ZeroDivisionError: float division (Sometimes the problem can be solved by changing the temperature to be calculated.)
- Regarding "C_S", I looked at the Thermo-Calc manual but couldn't understand it well. I would like to request that readers provide information to correct this issue. Currently, the "C_S" part in the test folder has been deleted with a comment. It would be fine if it had the same state diagram as the paper, but please be careful when handling it.
- Folders related to hydrogen storage material: Mg-Mn-Ni, H-La-Ni, H-Nd-Ni
- The test folder is a check to see if a ternary phase diagram can be drawn (including simple TDB file modifications). Normally, I would like to check whether the figure matches the figure in the paper, but since research funding in Japan is extremely uneven (therefore, the paper must be ordered based on copyright law), it is not easy to check. Another reason is that I don't have any achievements, so it's not easy to apply for research funding.


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
