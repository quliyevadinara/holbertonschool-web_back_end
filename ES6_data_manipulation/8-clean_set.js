export default function cleanSet(set, startString) {
  if (typeof startString !== "string" || startString === "") {
    return "";
  }

  let result = "";

  set.forEach((value) => {
    if (typeof value === "string" && value.startsWith(startString)) {
      result += `${value.slice(startString.length)}-`;
    }
  });

  return result.slice(0, -1);
}
