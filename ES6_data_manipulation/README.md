# ES6 Data Manipulation

This project explores advanced ES6 features for manipulating data structures in JavaScript: arrays, typed arrays, `Set`, and `Map`. It covers the standard `map`, `filter`, and `reduce` array methods, along with the newer `Set` and `Map` data structures introduced in ES6.

## Resources

Read or watch:

* [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
* [Typed Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypedArray)
* [Set data structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Set)
* [Map data structure](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map)

## Learning Objectives

At the end of this project, you should be able to explain, without the help of Google:

* How to use `map`, `filter`, and `reduce` on arrays
* Typed arrays
* The `Set`, `Map`, and `WeakMap` data structures

## Requirements

* All code is compatible with Ubuntu 20.04 LTS using Node 20.x.x
* Allowed editors: `vi`, `vim`, `emacs`, `Visual Studio Code`
* All files should end with a new line
* A `README.md` file at the root of the project folder is mandatory
* Code should use the `.js` extension
* Code will be verified against `ESLint`
* All functions must be exported: `export default myFunction;`

## Setup

### Install NodeJS 20.x.x

```bash
$ curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
$ sudo apt install nodejs -y
```

Verify the installation:

```bash
$ nodejs -v
v20.x.x
$ npm -v
9.x.x
```

### Install project dependencies

In the project folder, run:

```bash
$ npm install
```

## Configuration files

* `package.json`
* `babel.config.js` (or `.babelrc`)
* `.eslintrc.js`

Don't forget to run `$ npm install` before running the tests, or any tasks.

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-get_list_students.js` | Returns an array of student objects (`id`, `firstName`, `location`) |
| 1 | `1-get_list_student_ids.js` | Returns an array of student ids using `map` |
| 2 | `2-get_students_by_loc.js` | Filters students by city using `filter` |
| 3 | `3-get_ids_sum.js` | Sums all student ids using `reduce` |
| 4 | `4-update_grade_by_city.js` | Updates student grades for a city, combining `filter` and `map` |
| 5 | `5-typed_arrays.js` | Creates an `ArrayBuffer` with an `Int8` value at a given position |
| 6 | `6-set.js` | Creates a `Set` from an array |
| 7 | `7-has_array_values.js` | Checks if all elements of an array exist in a `Set` |
| 8 | `8-clean_set.js` | Builds a string from `Set` values sharing a common prefix |
| 9 | `9-groceries_list.js` | Returns a `Map` of grocery items and quantities |
| 10 | `10-update_uniq_items.js` | Updates quantities of `1` to `100` in a `Map` |

## Usage

Each task can be run with its corresponding main test file, using `babel-node`:

```bash
$ npm run dev 0-main.js
```

## Author

Holberton School / ALX Software Engineering program.