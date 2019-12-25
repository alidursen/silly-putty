# Quantum Key Distribution: An Introduction

This work collects and expands "Kuantum Anahtar Dağıtımı: Bir Giriş",
which is the 3rd place project from [Quantum Programming Hackathon](https://www.qturkey.org/hackathon)
held by QTurkey in Ankara, 14-15 December 2019.

Said project, developed by Ali Durşen and Yusuf Behzat ([@yusufbehzat](https://github.com/yusufbehzat)),
is a Turkish teaching material attempting to present a visual demonstration
of BB84 quantum key distribution protocol. This expansion aims to add English language support,
as well as formatting improvements.

Original submission can be found at
[Yusuf Behzat's GitHub](https://github.com/yusufbehzat/QKD_giris/blob/9989f4c88f5b70f9d96e5003d92071b8b9b9a3fa/QAD-demo.ipynb),
as well as in this folder (with minor changes) as `QAD_demo.ipynb`.

## How To

### Requirements

Developed using IBM's `qiskit` library for Python3, version `0.13.0`. Depending on backwards compatibility,
newer versions may work, no guarentees are given. Older versions fail due to backend incompatabilities.

No other external libraries are required.

### For Students

On `Demo-[LANGUAGE]` notebook, run the first cell which imports necessary libraries and defines functions.
When you're done studying the text, you can run the next cell with custom inputs if desired.

### For Developers/Instructors

If you're extending language support, on `DemoLanguages` simply add translations of lines to each dictionary:

* `a_lines`: Lines by first party (Alice)
* `b_lines`: Lines by second party (Bob)
* `c_lines`: Common lines and explanations
* `g_names`: Global names variable, allowing for customization
* `supported_languages`: Set of supported languages.

For example, for creating French version, I'd need to add a list with index `FR` to all 4 dictionaries above,
as well as adding `'FR'` element to `supported_languages`. Note that lists are ordered.
Where names are uttered, keep them enclosed in curly brackets, eg. `{Bob}`.
In `supported_languages`, elements must be all capitalized and using ISO 639-1 language codings is recommended.

If you're extending protocol support, you can define new functions in `DemoBasis` and call them in your `Demo-[LANGUAGE]`
notebook.

You can notify your students of customization options, or go with default values.

Support: alidursen@gmail.com
