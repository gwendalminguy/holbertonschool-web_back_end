export default function getStudentsByLocation(array, city) {
  return array.filter((object) => object.location === city);
}
