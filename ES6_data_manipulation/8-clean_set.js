export default function cleanSet(set, startString) {
  let result = '';

  if (startString && startString.length) {
    const size = startString.length;
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
