# Fixminer
This is a modified Fixminer to generate and save all patch candidates.

Since this tool does not run patch validation step, execution time is usually quite short (~1h).
However, you need a lot of disk space to save all candidates.

Note: Original Fixminer uses sub-template, but we don't use them.

## How to run  
First, compile this project:
```
$ ./compile.sh
```

Then, checkout the project in `buggy/`:
```
$ defects4j checkout -p <subject> -v <id>b -w buggy/<project>
```
For example,
```
$ defects4j checkout -p Chart -v 4b -w buggy/Chart_4
```

Next, run script to generate patch candidates:
```
java -Xmx<memory-to-use> -cp ./lib/JavaCodeParser-1.0.jar:./target/FixMiner-0.0.1-SNAPSHOT-jar-with-dependencies.jar edu.lu.uni.serval.fixminer.main.Main [option] <test_info_dir> <FL_result_dir> <project_dir> <d4j_dir> <version>
```
#### Important: last character of every paths in arguments should be slash(/).
* ```<test_info_dir>```: Direcotry of test information of each version. Usually it may be ```./FailedTestCases/```.
* ```<FL_result_dir>```: Directory of fault localization result. Usually it may be ```./BugPositions/```.
* ```<project_dir>```: Location of projects. If your project is in ```./buggy/Chart_1/```, then it should be ```./buggy/```.
* ```<d4j_dir>```: Location of Defects4j. If Defects4j is installed in ```/defects4j```, then it should be ```/defects4j/```.
* ```<version>```: Version name to run. Format should be ```<project>_<version>```. (e.g. ```Chart_24```)
  
For example:
```
java -Xmx100G -cp ./lib/JavaCodeParser-1.0.jar:./target/FixMiner-0.0.1-SNAPSHOT-jar-with-dependencies.jar edu.lu.uni.serval.fixminer.main.Main  ./FailedTestCases/ ./BugPositions/ ./buggy/ /defects4j/ Chart_4
```
  
### Options
* ```--max-loc <loc_number>``` or ```-l <loc_number>```: Use only top-```<loc_number>``` ranked locations in FL result.

## Output
Output files are in ```./d4j/<version>/0/```.

In each directory:
* ```switch-info.json```: Meta-information of patch candidates
* ```<FL_rank>/<template>/<id>/<patched_file>```: Actual patched files. 

# Fix Templates
The fix templates are located in: ```src/main/java/edu/uni/lu/serval/fixminer/fixtemplate```
