def findMedianSortedArrays(nums1: List[int], nums2: list[int]) -> float:
	m = len(nums1)
	n = len(nums2)
	if m > n:
		nums1, nums2, m, n = nums2, nums1, n, m
	if n == 0:
		raise ValueError
