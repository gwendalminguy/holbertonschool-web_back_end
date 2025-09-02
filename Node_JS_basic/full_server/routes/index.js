import Router from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const router = new Router();

router.get('/', (req, res) => {
  res.set('Content-Type', 'application/json');
  const data = AppController.getHomepage(req, res);
  res.status(data.status).send(data.body);
});

router.get('/students', (req, res) => {
  res.set('Content-Type', 'application/json');
  StudentsController.getAllStudents(req, res)
    .then((data) => res.status(data.status).send(data.body));
});

router.get('/students/:major', (req, res) => {
  res.set('Content-Type', 'application/json');
  StudentsController.getAllStudentsByMajor(req, res, req.params.major)
    .then((data) => res.status(data.status).send(data.body));
});

module.exports = router;
