export default function cleanSet(set, startString) {
  let result = [];
  const size = startString.length;

  if (startString) {
    for (const element of set) {
      if (element.startsWith(startString)) {
        if (result.length) {
          result.push(`-${element.substring(size)}`);
        } else {
          result.push(element.substring(size));
        }
      }
    }
  }
  return result;
}
