const readDatabase = require('../utils');

const DB_PATH = process.argv[2];

class StudentsController {
  static getAllStudents(request, response) {
    readDatabase(DB_PATH)
      .then((fields) => {
        const lines = ['This is the list of our students'];

        const sortedFields = Object.keys(fields).sort((a, b) => a.localeCompare(b, 'en', { sensitivity: 'base' }));

        sortedFields.forEach((field) => {
          const names = fields[field];
          lines.push(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
        });

        response.status(200).send(lines.join('\n'));
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(DB_PATH)
      .then((fields) => {
        const names = fields[major] || [];
        response.status(200).send(`List: ${names.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

module.exports = StudentsController;