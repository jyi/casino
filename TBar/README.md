
# TBar
Template-based automated program repair


I. Requirement
--------------
 - [Java 1.7](https://www.oracle.com/technetwork/java/javase/downloads/java-archive-downloads-javase7-521261.html)
 - [Defects4J](https://github.com/rjust/defects4j)
 - [GZoltar](https://github.com/SerVal-DTF/TBar/tree/master/lib)
 - [SVN >= 1.8](https://subversion.apache.org/packages.html)
 - [perl >= 5.0.10](https://www.perl.org/get.html)

II. Prepare Defects4J Bugs
---------------------------
 1. Download and Install Defects4J.
 - `./installD4J.sh`

 2. Check out and compile each bug.
 - `./checkoutD4JBugs.sh`

  If you fail to install defects4j, checkout or compile defects4j bugs, please reference these [introductions](https://github.com/rjust/defects4j#steps-to-set-up-defects4j).

 III. Compile & Run TBar
 ------------
 1. Compile TBar with `compile.sh` file

 2. Fixing Defects4J bugs with fault localization.
 - `./TBarFixRunner.sh <Bug_Data_Path> <Bug_ID> <defects4j_Home> <outputh_path>`

   Example: `./TBarFixRunner.sh $(pwd)/D4J/projects/ Chart_8 $(pwd)/D4J/defects4j/ $(pwd)/results/`.

 If it executes failed because of the paths of <Bug_Data_Path> and <defects4j_Home>, please use their absolute paths.

 IV. Structure of output directory
 ---------------------------
 ```powershell
 |--- <output_path>/                      : Output directory
 |------ <proj_id>/                       : D4Js project ID; Example: Chart_8
 |---------- ..._<template_name1>/        : Patch Template identifier
 |-------------- <patch_file>.java        : Generated patch by TBar
 |----------.
 |----------.
 |----------.
 |---------- switch-info.json             : Json file with context information regarding patch space
 ```
----
