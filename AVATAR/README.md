# Avatar
This is a modified Avatar to generate and save all patch candidates. 

I. Requirement
--------------
 - Java 1.7
 - [Defects4J](https://github.com/rjust/defects4j)
 - GZoltar 0.1.1
 
 
 II. Run AVATAR
 --------------
 1. Clone the PatchParser:
  - `git clone https://github.com/SerVal-DTF/AVATAR.git`
  
1. Compile this project.
  - `./compile.sh`
  
1. Fix bugs with perfect fault localization, which means that the bug positions at line level are known and the fault localization technique is not needed. 
  - `./LineFix.sh <BugID>`

1. Fix bugs with restricted fault localization, which means that the bug positions at method level are known that will help increase the accuracy of fault localization.
  - `./MethodFix.sh <BugID>`
  
1. Fix bugs with normal fault localization, which means that AVATAR directly uses off-the-shelf fault localization techniques (such as GZoltar + Ochiai) to localize the faulty code positions.
  - `./FLFix.sh <BugID>`


III. Run Casino
----------------
 1. Run `script/casino-setup.py` for patch candidate generation.
 ```
 python3 script/casino-setup.py
 ```

 2. Run `script/casino-run.py` for run Casino.
 ```
 python3 script/casino-run.py
 ```