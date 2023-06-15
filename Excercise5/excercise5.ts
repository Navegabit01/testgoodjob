function findCommonElements<T>(lists: T[][]): T[] {
  if (!Array.isArray(lists) || 0 === lists.length) {
    throw new Error('Invalid input: expected a non-empty array of arrays');
  }

  const [firstList, ...restLists] = lists;

  if (!firstList || 0 === firstList.length) {
    return [];
  }

  return firstList.filter((element) =>
      restLists.every((list) => list.includes(element))
  );
}

try {
  const lists = [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
  ];

  const commonElements = findCommonElements(lists);

  console.log(commonElements); // Output: [3, 4]
} catch (error: any) {
  console.error(error.message);
}

