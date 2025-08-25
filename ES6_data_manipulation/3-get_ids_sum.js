export default function getStudentIdsSum(array) {
  return array.reduce((accumulator, object) => accumulator + object.id, 0);
}
