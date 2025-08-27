export default function cleanSet(set, startString) {
  let result = '';
  const size = startString.length;

  if (startString) {
    for (const element of set) {
      if (element.startsWith(startString)) {
        if (result) {
          result = `${result}-${element.substring(size)}`;
        } else {
          result = element.substring(size);
        }
      }
    }
  }
  return result;
}
