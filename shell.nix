{ pkgs ? import <nixpkgs> { } }:

with pkgs;

mkShell {
  buildInputs = [ python3 poetry python-language-server chromium chromedriver ];
}
