# Travis-CI-languages-by-operating-system
```yaml
os:
  - linux
  #- osx
  #- windows
jobs:
  include:  # https://docs.travis-ci.com/user/languages
```
| language:    | os: linux       | os: osx         | os: windows     |
| ------------ | --------------- | --------------- | --------------- |
| android      |                 |                 | NEVER STARTS    |
| c            |                 |                 |                 |
| csharp       |                 |                 | FAILS           |
| cpp          |                 |                 |                 |
| clojure      |                 |                 | NEVER STARTS    |
| crystal      |                 |                 | FAILS           |
| d            |                 |                 | FAILS           |
| dart         |                 |                 |                 |
| elixir       |                 | FAILS           | FAILS           |
| elm          |                 |                 | NEVER STARTS    |
| erlang       | FAILS           | FAILS           | FAILS           |
| generic      | no language set | no language set | FAILS           |
| go           |                 |                 |                 |
| groovy       | no language set | no language set | FAILS           |
| haskell      |                 | FAILS           | FAILS           |
| haxe         |                 |                 | FAILS           |
| java         |                 |                 | FAILS           |
| julia        |                 |                 |                 |
| minimal      | no language set | no language set | NEVER STARTS    |
| nix          |                 |                 | NEVER STARTS    |
| nodejs       | no language set | no language set | NEVER STARTS    |
| objective-c  | no language set | no language set | no language set |
| perl         |                 |                 | FAILS           |
| perl6        |                 |                 |                 |
| php          |                 | FAILS           | FAILS           |
| python       |                 | FAILS           | FAILS           |
| r            |                 |                 | FAILS           |
| ruby         |                 |                 | FAILS           |
| rust         |                 |                 |                 |
| scala        |                 |                 | FAILS           |
| smalltalk    |                 |                 | NEVER STARTS    |
