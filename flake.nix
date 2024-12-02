{
  description = "Advent of Code 2024 in python";

  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils, ... }:
  let name = "aoc2024";
  in utils.lib.eachSystem
    [ utils.lib.system.x86_64-linux ]
    (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };
        buildInputs = with pkgs; [];
        nativeBuildInputs = with pkgs; [
          (pkgs.python3.withPackages (python-pkgs: with python-pkgs; [
            # select Python packages here
            requests
            numpy
          ]))
        ];
      in rec { 
        devShell = pkgs.mkShell {
          inherit buildInputs nativeBuildInputs;
        };
      }
    );
}