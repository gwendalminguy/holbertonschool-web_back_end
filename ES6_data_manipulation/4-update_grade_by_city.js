/* eslint no-param-reassign: ["error", { "props": false }] */
function addGrade(object, array) {
  for (const element of array) {
    if (object.id === element.studentId) {
      object.grade = element.grade;
    }
  }
  if (!('grade' in object)) {
    object.grade = 'N/A';
  }
  return object;
}

export default function updateStudentGradeByCity(students, city, newGrades) {
  return students.filter(
    (element) => element.location === city,
  ).map(
    (object) => addGrade(object, newGrades),
  );
}
