# Avatar
This is a modified Avatar to generate and save all patch candidates.

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
./FLFix.sh <bug_id>
```
Note that `<bug_id>` should be `<subject>_<id>` (e.g. `Chart_4`)
Before run `FLFix.sh`, You should change paths in `FLFix.sh`, especially `d4jData` (it should be `./buggy` as absolute path) and `d4jPath`(path where defects4j is installed).

## Output
Output files are in ```./d4j/<version>/0/```.

In each directory:
* ```switch-info.json```: Meta-information of patch candidates.
* ```<FL_rank>/<template>/<id>/<patched_file>```: Actual patched files. 
