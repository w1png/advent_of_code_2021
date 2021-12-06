fn main() {
    let mut fish_list = Vec::new();
    fish_list.push(1);
    for i in 0..256 {
        let mut gen = Vec::new();
        for fish in fish_list {
            if fish == 0 {
                gen.push(6);
                gen.push(8);
            } else {
                gen.push(fish - 1);
            }
        }
        fish_list = gen;
        println!("{:?}", (i));
    }
    println!("{:?}", (fish_list.len()));
}

