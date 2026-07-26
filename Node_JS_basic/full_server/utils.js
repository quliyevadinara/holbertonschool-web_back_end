const fs = require("fs");

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, "utf-8", (err, fileContent) => {
      if (err) {
        reject(new Error("Cannot load the database"));
        return;
      }

      const lines = fileContent
        .split("\n")
        .filter((line) => line.trim().length > 0);
      const studentLines = lines.slice(1);

      const fields = {};
      studentLines.forEach((line) => {
        const [firstname, , , field] = line.split(",");
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      });

      resolve(fields);
    });
  });
}

module.exports = readDatabase;
