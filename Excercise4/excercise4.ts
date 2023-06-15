const isAnagram = (str1: string, str2: string): boolean => {
  // Remove all non-letter characters and convert to lowercase
  str1 = str1.replace(/[^a-zA-Z]/g, "").toLowerCase();
  str2 = str2.replace(/[^a-zA-Z]/g, "").toLowerCase();

  // Check if the lengths of the strings are equal
  if (str1.length !== str2.length) {
    return false;
  }

  // Convert the strings to arrays and sort them alphabetically
  const arr1 = str1.split("").sort();
  const arr2 = str2.split("").sort();

  // Compare the sorted arrays
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }

  return true;
}

// Example usage:
console.log(isAnagram("listen", "silent")); // true
console.log(isAnagram("hello", "world")); // false