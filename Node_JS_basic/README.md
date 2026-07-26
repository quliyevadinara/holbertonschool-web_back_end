# Node JS Basic

Back-end project exploring core Node.js concepts: standard I/O, reading files
(sync and async), building HTTP servers with the raw `http` module and with
Express, and finally organizing a small Express app into controllers and
routes.

## Requirements

- Node.js (developed against Node 22, but compatible with Node 12+)
- npm

## Setup

```bash
npm install
```

This installs `express` (used from task 6 onward) plus the dev dependencies
used to run ES6 syntax through Babel (`babel-cli`, `babel-preset-env`,
`nodemon`).

Babel config is provided both as `.babelrc` and `babel.config.js` (either one
is enough — VS Code's file explorer may show both if you created them while
following the instructions).

## Files

| File | Description |
|---|---|
| `0-console.js` | `displayMessage(message)` — prints a message to STDOUT. |
| `1-stdin.js` | Small CLI program that reads a name from stdin and greets the user. |
| `2-read_file.js` | `countStudents(path)` — reads `database.csv` **synchronously** and logs student counts per field. Throws if the file can't be read. |
| `3-read_file_async.js` | Same as above but **asynchronous**, returns a `Promise`. |
| `4-http.js` | Plain `http` server on port 1245. Every route returns `Hello Holberton School!`. |
| `5-http.js` | Plain `http` server on port 1245 with `/` and `/students` routes. Database path comes from `process.argv[2]`. |
| `6-http_express.js` | Minimal Express server, `/` route only. |
| `7-http_express.js` | Express server with `/` and `/students` routes (same behavior as `5-http.js`). |
| `full_server/` | The same server logic split into `controllers/`, `routes/`, and a shared `utils.js`, wired together in `server.js`. Adds `/students/:major` (`CS` or `SWE` only). |
| `database.csv` | Sample student database (10 students: 6 in `CS`, 4 in `SWE`). |

## Running the scripts

Basic scripts (0–3) can be run directly with `node`:

```bash
node 2-read_file.js
```

Servers (4, 5, 6, 7) listen on port **1245**:

```bash
node 4-http.js
# in another terminal
curl localhost:1245
```

Servers that read the database (5 and 7) take the CSV path as an argument:

```bash
node 5-http.js database.csv
curl localhost:1245/students
```

### full_server

Run it directly with `node`:

```bash
node full_server/server.js database.csv
```

Or, using the ES6-friendly `dev` script (Babel + nodemon, auto-restarts on
file changes):

```bash
npm run dev
```

Endpoints:

```bash
curl localhost:1245                    # Hello Holberton School!
curl localhost:1245/students           # full report, all fields
curl localhost:1245/students/CS        # List: <CS first names>
curl localhost:1245/students/SWE       # List: <SWE first names>
curl localhost:1245/students/French    # 500 - Major parameter must be CS or SWE
```

## Notes

- CSV parsing ignores trailing empty lines — they don't count as students.
- If the database file can't be read, the `/students` routes return HTTP 500
  with `Cannot load the database`.
- Field names in `getAllStudents` (task 8.3 / `full_server`) are sorted
  alphabetically, case-insensitively.

## Author

Holberton School — `Node_JS_basic` project.