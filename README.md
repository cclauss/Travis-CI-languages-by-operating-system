# Travis-CI-languages-by-operating-system

os:
  - linux
  #- osx
  #- windows
jobs:
  include:  # https://docs.travis-ci.com/user/languages
  
| language:                  | os: linux              | os: osx              | os: windows           |
| ---                        | ---                    | ---                  | ---                   |
|   - language: android      |                        |                      | windows: NEVER STARTS |
|   - language: c            |                        |                      |                       |
|   - language: csharp       |                        |                      | windows: FAILS        |
|   - language: cpp          |                        |                      |                       |
|   - language: clojure      |                        |                      | windows: NEVER STARTS |
|   - language: crystal      |                        |                      | windows: FAILS        |
|   - language: d            |                        |                      | windows: FAILS        |
|   - language: dart         |                        |                      |                       |
|   - language: elixir       |                        | osx: FAILS           | windows: FAILS        |
|   - language: elm          |                        |                      | windows: NEVER STARTS |
|   - language: erlang       | linux: FAILS,          | osx: FAILS           | windows: FAILS        |
|   - language: generic      | linux: no language set | osx: no language set | windows: FAILS        |
|   - language: go           |                        |                      |                       |
|   - language: groovy       | linux: no language set | osx: no language set | windows: FAILS        |
|   - language: haskell      |                        | osx: FAILS,          | windows: FAILS        |
|   - language: haxe         |                        |                      | windows: FAILS        |
|   - language: java         |                        |                      | windows: FAILS        |
|   - language: julia        |                        |                      |                       |
|   - language: minimal      | linux: no language set | osx: no language set | windows: NEVER STARTS |
|   - language: nix          |                                               | windows: NEVER STARTS |
|   - language: nodejs       | linux: no language set | osx: no language set | windows: NEVER STARTS |
|   - language: objective-c  | linux: no language set | osx: no language set |                       |
|   - language: perl         |                                               | windows: FAILS        |
|   - language: perl6        |                        |                      |                       |
|   - language: php          |                        | osx: FAILS           | windows: FAILS        |
|   - language: python       |                        | osx: FAILS           | windows: FAILS        |
|   - language: r            |                        |                      | windows: FAILS        |
|   - language: ruby         |                        |                      | windows: FAILS        |
|   - language: rust         |                        |                      |                       |
|   - language: scala        |                        |                      | windows: FAILS        |
|   - language: smalltalk    |                        |                      | windows: NEVER STARTS |
