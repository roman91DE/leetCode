fn solve(nums: &[i32]) -> i32 {
    nums.iter().map(|x| (*x % 3)).filter(|x| *x != 0).count() as i32
}

fn main() {
    let v: Vec<i32> = vec![1, 2, 3, 4];
    let res = solve(&v);

    println!("Solution = {res}")
}
