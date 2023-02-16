# Fix Bugs with kPAR automatically

kPAR: a straightforward fix pattern-based APR system.

I. Requirement
----------------
 - Java 1.7
 - [Defects4J(v1.2.0)](https://github.com/rjust/defects4j)
 - kPAR

 II. Prepare Defects4J Bugs
--------------------
 1. Download and Install Defects4J.
 - `./installD4J.sh`

 2. Check out and compile each bug.
 - `./checkoutD4JBugs.sh`

III. Compile & Run kPar
--------------------
 1. Compile kPar with `compile.sh` file

 2. Fixing Defects4J bugs with fault localization.
 - `./KParFixRunner.sh <Bug_Data_Path> <Bug_ID> <defects4j_Home> <outputh_path>`

   Example: `./KParFixRunner.sh $(pwd)/D4J/projects/ Chart_8 $(pwd)/D4J/defects4j/ $(pwd)/results/`.

IV. Structure of output directory
 ---------------------------
 ```powershell
 |--- <output_path>/                      : Output directory
 |------ <proj_id>/                       : D4Js project ID; Example: Chart_8
 |---------- ..._<template_name1>/        : Patch Template identifier
 |-------------- <patch_file>.java        : Generated patch by kBar
 |----------.
 |----------.
 |----------.
 |---------- switch-info.json             : Json file with context information regarding patch space
 ```
----