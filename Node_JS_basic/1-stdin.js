process.stdout.write("Welcome to Holberton School, what is your name?\n");

process.stdin.setEncoding("utf8");

process.stdin.on("readable", () => {
  const input = process.stdin.read();
  if (input !== null) {
    const name = input.toString().trim();
    if (name.length > 0) {
      process.stdout.write(`Your name is: ${name}\n`);
    }
  }
});

process.stdin.on("end", () => {
  process.stdout.write("This important software is now closing\n");
});
