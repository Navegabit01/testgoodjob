function mergeSort<T>(arr: T[]): T[] {
  if (!Array.isArray(arr)) {
    throw new Error('Input is not an array');
  }

  if (arr.length <= 1) {
    return arr;
  }

  const mid = Math.floor(arr.length / 2);
  const leftHalf = arr.slice(0, mid);
  const rightHalf = arr.slice(mid);

  return merge(mergeSort(leftHalf), mergeSort(rightHalf));
}

function merge<T>(leftHalf: T[], rightHalf: T[]): T[] {
  if (!Array.isArray(leftHalf) || !Array.isArray(rightHalf)) {
    throw new Error('Input is not an array');
  }

  const result: T[] = [];
  let leftIndex = 0;
  let rightIndex = 0;

  while (leftIndex < leftHalf.length && rightIndex < rightHalf.length) {
    if (leftHalf[leftIndex] < rightHalf[rightIndex]) {
      result.push(leftHalf[leftIndex]);
      leftIndex++;
    } else {
      result.push(rightHalf[rightIndex]);
      rightIndex++;
    }
  }

  return result.concat(leftHalf.slice(leftIndex)).concat(rightHalf.slice(rightIndex));
}

// Pruebas
const arr1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5];
const arr2 = ['c', 'a', 't', 'd', 'o', 'g'];
const arr3 = [true, false, true, true, false];
const arr4 = [];

console.log(mergeSort(arr1)); // [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
console.log(mergeSort(arr2)); // ['a', 'c', 'd', 'g', 'o', 't']
console.log(mergeSort(arr3)); // [false, false, true, true, true]
console.log(mergeSort(arr4)); // []