# Conan Playground (project)

Provides a way to test some conan.io features I'm interested in.

# Features under test

I'm looking at:
- Capturing the package version from Git.
  - Check if its possible to capture it from a Git tag.
- Lockfiles for discovering the correct (re) build order of a set of conan packages
- Possible integration of this build order with a CI system (either generic of Jenkins CI)

# Compiling the project
`conan create -s compiler.cppstd=11 . logger/0.0`

# Decription of the conan packages
- logger: base package, likely used by all other packages.
- pkg1 to pkg6 - generic sample packages, all depending on logger and depending on each other in a acyclical graph

Requirements of each package:

![Alt text](https://g.gravizo.com/source/custom_mark10?https%3A%2F%2Fraw.githubusercontent.com%2Fruipires%2Fconan-playground%2Fmaster%2FREADME.md)

<details>
<summary></summary>
custom_mark10
  digraph G {
    size ="4,4";
    pkg1 -> logger;

    pkg2 -> logger;
    pkg2 -> pkg1;

    pkg3 -> pkg2;
    pkg3 -> logger;

    pkg4 -> pkg5;
    pkg4 -> logger;

    pkg5 -> pkg1;

    pkg6 -> pkg5;
    pkg6 -> pkg4;
    pkg6 -> logger;
  }
custom_mark10
</details>
