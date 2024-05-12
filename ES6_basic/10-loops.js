export default function appendToEachArrayValue(array, appendString) {
  const arr = [...array];
  for (const idx of arr) {
    const value = arr[idx];
    arr[idx] = appendString + value;
  }

  return arr;
}
