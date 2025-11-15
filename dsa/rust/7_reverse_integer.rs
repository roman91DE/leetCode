fn reverse(n: i32) -> i32 {
    reverse_checked(n).unwrap_or(0)
}

fn reverse_checked(n: i32) -> Option<i32> {
    let mut current = n.checked_abs()?;
    let base: i32 = 10;
    let sign = n.signum();
    
    let mut digits = Vec::new();
    while current > 0 {
        digits.push(current % 10);
        current /= 10;
    }
    
    let mut result = 0i32;
    let len = digits.len();
    
    for (i, &digit) in digits.iter().enumerate() {
        let power = (len - 1 - i) as u32;
        let multiplier = base.checked_pow(power)?;
        let term = digit.checked_mul(multiplier)?;
        result = result.checked_add(term)?;
    }
    
    result.checked_mul(sign)
}

pub fn main() {
    let input = 123;
    let output = reverse(input);
    println!("{input} -> {output}")
}

// test cases
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_easy_cases() {
        assert_eq!(reverse(123), 321);
        assert_eq!(reverse(-123), -321);
        assert_eq!(reverse(0), 0);
    }

    #[test]
    fn test_overflow_cases() {
        assert_eq!(reverse(1534236469), 0);
        assert_eq!(reverse(2147483647), 0);
        assert_eq!(reverse(-2147483648), 0);
    }

    #[test]
    fn test_cases_with_zero_in_digit() {
        assert_eq!(reverse(120), 21);
        assert_eq!(reverse(1200), 21);
        assert_eq!(reverse(100), 1);
        assert_eq!(reverse(-120), -21);
    }
}
