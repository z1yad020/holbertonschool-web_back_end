export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString === '') return '';

  const list = [];

  for (const str of set) {
    if (str.startsWith(startString)) list.push(str.slice(startString.length));
  }
  return list.join('-');
}