function tank(input) {
    let length = Number(input[0]);
    let width = Number(input[1]);
    let hight = Number(input[2]);
    let percent = Number(input[3]);
    let full = length * width * hight;
    let water = full * (100 - percent) / 100000;
    console.log(water);
}

tank(["105 ",
"77 ",
"89 ",
"18.5 "]
);