process.stdout.write('Welcome to Holberton School, what is your name?\n', () => {
  process.stdin.on('data', (name) => {
    process.stdout.write(`Your name is: ${name}`);
    if (!process.stdin.setRawMode) {
      process.stdout.write('This important software is now closing\n');
    }
  });
});
