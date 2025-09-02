class AppController {
  static getHomepage(req, res) {
    res.set('Content-Type', 'application/json');
    res.status(200).send('Hello Holberton School!');
  }
}

export default AppController;
