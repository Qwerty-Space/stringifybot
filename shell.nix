{ pkgs ? import <nixpkgs> {} }:
let
  bprint = { lib, buildPythonPackage, fetchFromGitHub }:
    buildPythonPackage rec {
      pname = "beauty-print";
      version = "0.6.1";

      src = fetchFromGitHub {
        owner = "Lonami";
        repo = "bprint";
        rev = "fada746c3010d2a3c82a0fa12304559d69f9b896";
        sha256 = "0x4srav3xvng061qfps15icnfj445yy8l72ljljqj0zvcadwrrwv";
      };

      doCheck = false;
    };
in
pkgs.mkShell {
  name = "stringify-bot-shell";
  buildInputs = [
    (pkgs.python39.withPackages (ps: with ps; [
      (callPackage bprint {})
      telethon
    ]))
  ];
}