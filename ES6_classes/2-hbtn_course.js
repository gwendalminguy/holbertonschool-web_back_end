export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw new TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw new TypeError('Length must be a number');
    }
    if (typeof students !== 'object') {
      throw new TypeError('Students must be an array of strings');
    }
    for (const element of students) {
      if (typeof element !== 'string') {
        throw new TypeError('Students must be an array of strings');
      }
    }

    this._name = name;
    this._length = length;
    this._students = students;
  }

  // Name
  get name() {
    return this._name;
  }

  set name(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Length
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'string') {
      throw new TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Students
  get students() {
    return this._students;
  }

  set students(value) {
    if (typeof value !== 'object') {
      throw new TypeError('Students must be an array of strings');
    }
    for (const element of value) {
      if (typeof element !== 'string') {
        throw new TypeError('Students must be an array of strings');
      }
    }
    this._students = value;
  }
}
