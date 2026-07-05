# ES6 Classes

This project explores ES6 classes in JavaScript: constructors, getters/setters,
static methods, inheritance, abstract classes, computed/well-known symbol
methods (`Symbol.toStringTag`, `Symbol.toPrimitive`, `Symbol.species`), and
common hoisting pitfalls.

## Repository

- GitHub repository: `holbertonschool-web_back_end`
- Directory: `ES6_classes`

## Requirements

- All files are interpreted/compiled on Ubuntu 20.04 LTS using Node.js (14.x+)
- Code follows the Airbnb JavaScript style guide (checked with `eslint`)
- All files must end with a new line
- A `README.md` file at the root of the project is mandatory
- Every file should be run with `npm run dev <file>`

## Setup

```bash
npm install
```

Typical `package.json` scripts used throughout the project:

```json
{
  "scripts": {
    "lint": "./node_modules/.bin/eslint",
    "check-lint": "lint [0-9]*.js",
    "dev": "npx babel-node",
    "test": "jest",
    "full-test": "./node_modules/.bin/eslint [0-9]*.js && jest"
  }
}
```

## Files

| File                   | Description                                                                                    |
| ---------------------- | ---------------------------------------------------------------------------------------------- |
| `0-classroom.js`       | `ClassRoom` class holding a `_maxStudentsSize` attribute                                       |
| `1-make_classrooms.js` | `initializeRooms` function returning 3 `ClassRoom` instances (19, 20, 34)                      |
| `2-hbtn_course.js`     | `HolbertonCourse` class with typed getters/setters for `name`, `length`, `students`            |
| `3-currency.js`        | `Currency` class with getters/setters and a `displayFullCurrency` method                       |
| `4-pricing.js`         | `Pricing` class using `Currency`, with `displayFullPrice` and a static `convertPrice` method   |
| `5-building.js`        | Abstract `Building` class that forces subclasses to implement `evacuationWarningMessage`       |
| `6-sky_high.js`        | `SkyHighBuilding` extends `Building`, overrides `evacuationWarningMessage`                     |
| `7-airport.js`         | `Airport` class using `Symbol.toStringTag` for a custom string description                     |
| `8-hbtn_class.js`      | `HolbertonClass` using `Symbol.toPrimitive` to control `Number()`/`String()` casting           |
| `9-hoisting.js`        | Fixed version of a broken script (class hoisting, `this` vs `self`, recursive getter bugs)     |
| `10-car.js`            | `Car` class with a `cloneCar` method using `Symbol.species` to clone into the correct subclass |

## Task Details

### 0. Classrooms

`ClassRoom` is a minimal class that stores a single `_maxStudentsSize`
attribute passed into the constructor.

### 1. Let's make some classrooms

`initializeRooms` imports `ClassRoom` and returns an array of three
`ClassRoom` objects with sizes `19`, `20`, and `34`.

### 2. A Course, Getters, and Setters

`HolbertonCourse` validates the type of each constructor argument
(`name` must be a string, `length` a number, `students` an array of
strings) and stores them as underscore-prefixed attributes with
matching getters/setters. Setting an attribute to an invalid type
throws a `TypeError`.

### 3. Methods, static methods, computed method names — MONEY

`Currency` stores `code` and `name`, exposes getters/setters for both,
and implements `displayFullCurrency()` which returns `"name (code)"`.

### 4. Pricing

`Pricing` wraps an `amount` and a `Currency` instance. It implements
`displayFullPrice()` (`"amount currency_name (currency_code)"`) and a
static `convertPrice(amount, conversionRate)` helper that returns
`amount * conversionRate`.

### 5. A Building

`Building` is treated as an abstract class: it stores `sqft` (with a
getter only) and throws an `Error` — `Class extending Building must
override evacuationWarningMessage` — if a subclass does not override
`evacuationWarningMessage`. Instantiating `Building` directly works
fine since there's no subclass to enforce.

### 6. Inheritance

`SkyHighBuilding` extends `Building`, forwarding `sqft` to `super()`
and adding its own `floors` attribute (with a getter). It overrides
`evacuationWarningMessage()` to return
`"Evacuate slowly the NUMBER_OF_FLOORS floors"`.

### 7. Airport

`Airport` stores `name` and `code`. It uses `Symbol.toStringTag` so
that logging the instance shows `Airport [CODE] { ... }` and calling
`.toString()` returns `[object CODE]`.

### 8. Primitive - Holberton Class

`HolbertonClass` stores `size` and `location`. It implements
`[Symbol.toPrimitive](hint)` so that `Number(instance)` returns
`size` and `String(instance)` returns `location`.

### 9. Hoisting

The original script had several bugs:

- Classes were used before being declared — ES6 classes are not
  hoisted the way function declarations are, so declarations were
  moved above their usage.
- `StudentHolberton`'s constructor referenced an undefined
  `holbertonClass` variable instead of its own parameter.
- The `holbertonClass` getter recursively called itself
  (`return this.holbertonClass`) instead of returning
  `this._holbertonClass`.
- `fullStudentDescription` referenced an undefined `self` instead of
  `this`.
- The default export needed to be `listOfStudents` to match how it's
  imported in `9-main.js`.

### 10. Vroom

`Car` stores `brand`, `motor`, and `color`. `cloneCar()` uses
`Symbol.species` (via a static getter returning `this`) combined with
`this.constructor[Symbol.species]` so that cloning a subclass instance
(e.g. `TestCar`) produces a new instance of that same subclass with
uninitialized attributes, rather than a plain `Car`.

## Usage

```bash
npm run dev 0-main.js
npm run dev 1-main.js
npm run dev 2-main.js
npm run dev 3-main.js
npm run dev 4-main.js
npm run dev 5-main.js
npm run dev 6-main.js
npm run dev 7-main.js
npm run dev 8-main.js
npm run dev 9-main.js
npm run dev 10-main.js
```

## Author

Holberton School / ALX Web Back-End specialization.
