
fn main() {

    // Read in input file 
    let input: String = std::fs::read_to_string("day01/input.txt")
        .expect("Failed to read in file");

    println!("{}", part1(&input));
    println!("{}", part2(&input));
}

fn part1(input: &str) -> i64 {
    
    let start = 50;
    let mut tmp = start;
    let mut count = 0;
    for (_i, line) in input.lines().enumerate() {

        // Split the line string at the first character 
        let (direction, num_str) = line.split_at(1);
        
        // Convert to int and char for comparison and maths operations
        let num: i64 = num_str.parse().unwrap();

        tmp = match direction {
            "R" => modulo(tmp + num, 100),
            "L" => modulo(tmp - num, 100),
            _ => panic!("Invalid direction")
        };
        

        if tmp == 0 {
            count += 1;
        }

        // println!("{}, {} -- {}, {}", direction, num, tmp, count);
    }

    return count
}

fn part2(input: &str) -> i64 {
    
    let mut tmp = 50;
    let mut count_zero = 0;


    for line in input.lines() {

        let (direction, num_str) = line.split_at(1);

        let num: i64 = num_str.parse().unwrap();

        if direction == "R" {
            // Count number of rolls -> integer division -> find k in tmp + num = k * 100 + rem
            count_zero += (tmp + num) / 100;
            tmp = modulo(tmp + num, 100);
        } else {
            // Map left from tmp to right from s_prime = (100 - tmp) % 100
            let s_prime = (100 - tmp).rem_euclid(100);
            count_zero += (s_prime + num) / 100;

            tmp = (tmp - num).rem_euclid(100);
        }

        println!("{}, {} -- {}, {}", direction, num, tmp, count_zero);
    }

    return count_zero 
}

fn modulo(a: i64, m:i64) -> i64 {
    ((a % m) + m) % m
}
