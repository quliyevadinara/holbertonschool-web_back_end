const fs = require("fs");

function countStudents(path) {
  let fileContent;
  try {
    fileContent = fs.readFileSync(path, "utf-8");
  } catch (err) {
    throw new Error("Cannot load the database");
  }

  const lines = fileContent
    .split("\n")
    .filter((line) => line.trim().length > 0);
  // First line is the header
  const studentLines = lines.slice(1);

  const fields = {};
  studentLines.forEach((line) => {
    const [firstname, , , field] = line.split(",");
    if (!fields[field]) {
      fields[field] = [];
    }
    fields[field].push(firstname);
  });

  const total = studentLines.length;
  console.log(`Number of students: ${total}`);

  Object.keys(fields).forEach((field) => {
    const names = fields[field];
    console.log(
      `Number of students in ${field}: ${names.length}. List: ${names.join(", ")}`,
    );
  });
}

module.exports = countStudents;
