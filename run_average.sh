#! /usr/bin/bash

declare -a commands=(
    "echo 'C'"
    "echo --------"
    "gcc ./C/Arrays/average.c -o ./C/Arrays/average.out && ./C/Arrays/average.out"
    "echo ''"
    "echo 'Go'"
    "echo --------"
    "go run ./Go/Arrays/average.go"
    "echo ''"
    "echo 'Javascript'"
    "echo --------"
    "node ./JavaScript/Arrays/average.js"
    "echo ''"
    "echo 'Python'"
    "echo --------"
    "python3 ./Python/Arrays/average.py"
    "echo ''"
    "echo 'Rust'"
    "echo --------"
    "cargo build --manifest-path ./Rust/Arrays/Cargo.toml --release && ./Rust/Arrays/target/release/average"
    "echo ''"
    "echo 'TypeScript'"
    "echo --------"
    "tsc ./TypeScript/Arrays/average.ts && node ./TypeScript/Arrays/average.js"
    "echo ''"
)

for ((i = 0; i < ${#commands[@]}; i++)) do
    eval "${commands[$i]}"
done

