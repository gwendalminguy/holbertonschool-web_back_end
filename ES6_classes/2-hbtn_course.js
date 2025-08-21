/* eslint no-underscore-dangle: 0 */
export default class HolbertonCourse {
  constructor(name, length, students) {
    if (typeof name !== 'string') {
      throw TypeError('Name must be a string');
    }
    if (typeof length !== 'number') {
      throw TypeError('Length must be a number');
    }
    if (!Array.isArray(students)) {
      throw TypeError('Students must be an array of strings');
    }
    for (const element of students) {
      if (typeof element !== 'string') {
        throw TypeError('Students must be an array of strings');
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
      throw TypeError('Name must be a string');
    }
    this._name = value;
  }

  // Length
  get length() {
    return this._length;
  }

  set length(value) {
    if (typeof value !== 'string') {
      throw TypeError('Length must be a number');
    }
    this._length = value;
  }

  // Students
  get students() {
    return this._students;
  }

  set students(value) {
    if (!Array.isArray(value)) {
      throw TypeError('Students must be an array of strings');
    }
    for (const element of value) {
      if (typeof element !== 'string') {
        throw TypeError('Students must be an array of strings');
      }
    }
    this._students = value;
  }
}
