/*
2154. Keep Multiplying Found Values by Two

You are given an array of integers nums.
You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.
*/

fn find_final_value(nums: Vec<i32>, original: i32) -> i32 {
    solve(&nums, original).expect("Can only occur with Overflow Multiplication")
}

fn solve(nums: &[i32], original: i32) -> Option<i32> {
    match nums.contains(&original) {
        false => Some(original),
        true => {
            let new = original.checked_mul(2)?;
            solve(nums, new)
        }
    }
}

fn main() {
    let nums = [5, 3, 6, 1, 12];
    let original = 3;

    let res = solve(&nums, original).expect("Error!!!");

    println!("{res}")
}
