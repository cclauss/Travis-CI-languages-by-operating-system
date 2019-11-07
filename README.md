# Travis CI: languages by operating system

Try running each of the languages on each of the operating systems

[`.travis.yml`](.travis.yml)
```yaml
os:
  - linux
  #- osx
  #- windows
jobs:
  include:  # https://docs.travis-ci.com/user/languages
    - language: android  # ...

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

To convert the comments in the [.travis.yml](.travis.yml) file into this markdown table, run:
```python
with open(".travis.yml") as in_file:
    print("\n".join(line.rstrip().replace("# ", "").replace("- language: ", "| ")
        for line in in_file if line.startswith(" " * 4)))
```
