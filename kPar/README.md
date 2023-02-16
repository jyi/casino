# kPar
This is a modified kPAr to generate and save all patch candidates.

Since this tool does not run patch validation step, execution time is usually quite short (~1h).
However, you need a lot of disk space to save all candidates.

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
$ ./KParFixRunner.sh <project_dir> <version> <d4j_dir> <output_dir>
```
#### Important: last character of every paths in arguments should be slash(/).
* ```<project_dir>```: Location of projects. If your project is in ```./buggy/Chart_1/```, then it should be ```./buggy/```.
* ```<version>```: Version name to run. Format should be ```<project>_<version>```. (e.g. ```Chart_24```)
* ```<d4j_dir>```: Location of Defects4j. If Defects4j is installed in ```/defects4j```, then it should be ```/defects4j/```.
* `<output_dir>`: Location of output. This should be `d4j/`.
  
For example:
```
$ ./KParFixRunner.sh buggy/ Chart_4 /defects4j/ d4j/
```

## Output
Output files are in ```./d4j/<version>/```.

In each directory:
* ```switch-info.json```: Meta-information of patch candidates.
* The other directories: Actual patch candidates (patched files).