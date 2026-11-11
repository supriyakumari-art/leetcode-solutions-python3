# Best Time to Buy and Sell Stock

## Problem Description
You are given an array `prices` where `prices[i]` represents the price of a stock on the `i-th` day.

You want to maximize your profit by choosing one day to buy and another day in the future to sell the stock.

Return the maximum profit you can achieve. If no profit is possible, return `0`.

## Approach: Greedy Algorithm

We use a **Greedy Approach** to solve this problem efficiently.

1. Initialize `min_price` with the first day's stock price.
2. Initialize `max_profit` as `0`.
3. Traverse the array starting from the second day.
4. Calculate the current profit by subtracting `min_price` from the current price.
5. Update `max_profit` if the current profit is greater.
6. Update `min_price` whenever a lower stock price is found.
7. Return `max_profit`.

## Example

**Input:**
```python
prices = [7, 1, 5, 3, 6, 4]
```

**Output:**
```python
5
```

**Explanation:**

- Buy the stock at price `1`.
- Sell the stock at price `6`.
- Maximum Profit = `6 - 1 = 5`.

## Complexity Analysis

- **Time Complexity:** O(n) – We traverse the prices array only once.
- **Space Complexity:** O(1) – We use only two extra variables (`min_price` and `max_profit`).

## Key Concepts

- Arrays
- Greedy Algorithm
- Single Pass
- Minimum Value Tracking

## LeetCode

[Best Time to Buy and Sell Stock – LeetCode 121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

---

**Author:** Supriya Kumari
