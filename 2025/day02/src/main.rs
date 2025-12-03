fn main() {
    let input: String =
        std::fs::read_to_string("day02/test.txt").expect("Failed to load input file");

    println!("{}", part1(&input));
}

fn part1(input: &str) -> i32 {
    let mut invalid_id_sum: i32 = 0;

    for range in input.split(",") {
        // Split the range into its start and end
        let (range_start, range_end) = range.split_once("-").unwrap();

        // Parse the strs
        let start: i32 = range_start.parse().unwrap();
        let end: i32 = range_end.parse().unwrap();

        invalid_id_sum = 0;
        for i in start..end {
            let invalid_id = invalid_id(&i);
            invalid_id_sum += invalid_id;

            println!("{}, {}", invalid_id, invalid_id_sum)
        }
    }

    return invalid_id_sum;
}

fn invalid_id(id: &i32) -> i32 {
    let s = id.to_string();
    let bytes = s.as_bytes();
    let len = bytes.len();

    // Look for any block length L where some substring of length L
    // is immediately followed by the same substring.
    //
    // That is: exists i, L such that:
    //   bytes[i..i+L] == bytes[i+L..i+2*L]
    //
    for block_len in 1..=len / 2 {
        for i in 0..=len - 2 * block_len {
            let first = &bytes[i..i + block_len];
            let second = &bytes[i + block_len..i + 2 * block_len];

            if first == second {
                // Found a repeated consecutive block → invalid → return the number
                return *id;
            }
        }
    }

    // No repeated consecutive block found → valid → return 0
    0
}
