# Travis-CI-languages-by-operating-system

os:
  - linux
  #- osx
  #- windows
jobs:
  include:  # https://docs.travis-ci.com/user/languages
  
| language:                    | os: linux       | os: osx         | os: windows     |
| ---------------------------- | --------------- | --------------- | --------------- |
|   - language: android      # |                 |                 | NEVER STARTS    |
|   - language: c            # |                 |                 |                 |
|   - language: csharp       # |                 |                 | FAILS           |
|   - language: cpp          # |                 |                 |                 |
|   - language: clojure      # |                 |                 | NEVER STARTS    |
|   - language: crystal      # |                 |                 | FAILS           |
|   - language: d            # |                 |                 | FAILS           |
|   - language: dart         # |                 |                 |                 |
|   - language: elixir       # |                 | FAILS           | FAILS           |
|   - language: elm          # |                 |                 | NEVER STARTS    |
|   - language: erlang       # | FAILS           | FAILS           | FAILS           |
|   - language: generic      # | no language set | no language set | FAILS           |
|   - language: go           # |                 |                 |                 |
|   - language: groovy       # | no language set | no language set | FAILS           |
|   - language: haskell      # |                 | FAILS           | FAILS           |
|   - language: haxe         # |                 |                 | FAILS           |
|   - language: java         # |                 |                 | FAILS           |
|   - language: julia        # |                 |                 |                 |
|   - language: minimal      # | no language set | no language set | NEVER STARTS    |
|   - language: nix          # |                 |                 | NEVER STARTS    |
|   - language: nodejs       # | no language set | no language set | NEVER STARTS    |
|   - language: objective-c  # | no language set | no language set | no language set |
|   - language: perl         # |                 |                 | FAILS           |
|   - language: perl6        # |                 |                 |                 |
|   - language: php          # |                 | FAILS           | FAILS           |
|   - language: python       # |                 | FAILS           | FAILS           |
|   - language: r            # |                 |                 | FAILS           |
|   - language: ruby         # |                 |                 | FAILS           |
|   - language: rust         # |                 |                 |                 |
|   - language: scala        # |                 |                 | FAILS           |
|   - language: smalltalk    # |                 |                 | NEVER STARTS    |
