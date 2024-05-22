export default function getStudentsByLocation(list, city) {
  return list.filter((ob) => ob.location === city);
}
