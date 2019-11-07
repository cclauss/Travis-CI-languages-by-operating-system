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
    | language:    | os: linux       | os: osx         | os: windows     | linux: python3 --version  |
    | ------------ | --------------- | --------------- | --------------- |                           |
    | android      |                 |                 | NEVER STARTS    | Python 3.4.3 with no pip3 |
    | c            |                 |                 |                 | Python 3.5.2 with no pip3 |
    | csharp       |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | cpp          |                 |                 |                 | Python 3.5.2 with no pip3 |
    | clojure      |                 |                 | NEVER STARTS    | Python 3.5.2 with no pip3 |
    | crystal      |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | d            |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | dart         |                 |                 |                 | Python 3.5.2 with no pip3 |
    | elixir       |                 | FAILS           | FAILS           | Python 3.5.2 with no pip3 |
    | elm          |                 |                 | NEVER STARTS    | Python 3.4.3 with no pip3 |
    | erlang       | FAILS           | FAILS           | FAILS           |                           |
    | generic      | no language set | no language set | FAILS           | Python 3.5.2 with no pip3 |
    | go           |                 |                 |                 | Python 3.5.2 with no pip3 |
    | groovy       | no language set | no language set | FAILS           | Python 3.5.2 with no pip3 |
    | haskell      |                 | FAILS           | FAILS           | Python 3.5.2 with no pip3 |
    | haxe         |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | java         |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | julia        |                 |                 |                 | Python 3.5.2 with no pip3 |
    | minimal      | no language set | no language set | NEVER STARTS    | Python 3.5.2 with no pip3 |
    | nix          |                 |                 | NEVER STARTS    | Python 3.5.2 with no pip3 |
    | node_js      |                 |                 |                 | Python 3. with no pip3    |
    | objective-c  | Runs on macOS!! | no language set | no language set | Python 3.6.5, pip3 10.0.1 |
    | perl         |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | perl6        |                 |                 |                 | Python 3.5.2 with no pip3 |
    | php          |                 | FAILS           | FAILS           | Python 3.5.2 with no pip3 |
    | python       |                 | FAILS           | FAILS           | language: python: 3.8 pip |
    | r            |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | ruby         |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | rust         |                 |                 |                 | Python 3.5.2 with no pip3 |
    | scala        |                 |                 | FAILS           | Python 3.5.2 with no pip3 |
    | smalltalk    |                 |                 | NEVER STARTS    | Python 3.4.3 with no pip3 |

To convert the comments in the [.travis.yml](.travis.yml) file into this markdown table, run:
```python
with open(".travis.yml") as in_file:
    print("\n".join(line.rstrip().replace("# ", "").replace("- language: ", "| ")
        for line in in_file if line.startswith(" " * 4)))
```
