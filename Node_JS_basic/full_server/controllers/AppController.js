class AppController {
  static getHomepage() {
    return {
      status: 200,
      body: 'Hello Holberton School!',
    };
  }
}

module.exports = AppController;
