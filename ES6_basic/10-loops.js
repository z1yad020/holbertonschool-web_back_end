export default function appendToEachArrayValue(array, appendString) {
  const arr = [...array];
  for (const idx of arr) {
    const value = arr.indexOf(idx);
    arr[value] = appendString + idx;
  }

  return arr;
}
