/*
Cargo.toml exists in root, source in /src subdirectory.
cargo build --release
./target/release/hello

You can compile with rustc or cargo. cargo abstracts/wraps rustc
Generally, cargo is nicer to use. 

https://doc.rust-lang.org/cargo/getting-started/first-steps.html

Create a Cargo.toml file to define
options. https://doc.rust-lang.org/cargo/reference/manifest.html

VS Code has an extension named 'Even Better TOML' for syntax highlighting
and linting.
*/
fn main() {
    println!("Hello, World!")
}