# Avatar
This is a modified Avatar to generate and save all patch candidates.

Since this tool does not run patch validation step, execution time is usually quite short (~1h).
However, you need a lot of disk space to save all candidates.

## How to run  
First, compile this project:
```
$ ./compile.sh
```
  
Next, run script to generate patch candidates:
```
./FLFix.sh <bug_id>
```
Note that `<bug_id>` should be `<subject>_<id>` (e.g. `Chart_4`)
Before run `FLFix.sh`, You should change paths in `FLFix.sh`, especially `d4jData` (it should be `./buggy` as absolute path) and `d4jPath`(path where defects4j is installed).

### Output
Output will be saved in `d4j/<bug_id>`.

`d4j/<bug_id>/switch-info.json` file contains meta-information about patch space. `SimAPR` will read and parse this file.

Other directories are actual patch candidates.